#!/usr/bin/env python3
"""
aa_crop_tool.py — Ferramenta de download e recorte para o arquivo digital
CulturAçores (culturacores.azores.gov.pt), pensada para uso com Claude Code
LOCAL (no seu computador), substituindo o pipeline anterior via painel de
navegador + canvas + ponte base64.

Porque este script existe
--------------------------
No ambiente em nuvem (sandbox) a rede é filtrada por uma lista branca e o
domínio culturacores.azores.gov.pt está bloqueado (testado: CONNECT tunnel
failed, HTTP 403 através do proxy). O contorno usado até agora — abrir a
imagem no painel de navegador, recortar com canvas, e trazer o recorte de
volta por uma "ponte" — tem um limite de ~800.000 caracteres por resultado,
o que obriga a escalas reduzidas, múltiplas idas e vindas, e descodificação
manual de cada recorte a partir de um ficheiro de resultado.

A correr localmente (fora do sandbox), a rede do seu computador não passa
por essa lista branca, e este script pode:
  - descarregar cada imagem uma única vez, em resolução nativa, e guardá-la
    em cache (nunca a torna a descarregar);
  - gerar quantos recortes ampliados quiser, em qualquer coordenada,
    instantaneamente, como ficheiros .jpg normais no disco — sem limite de
    tamanho de resultado, sem precisar de decode.py;
  - sobrepor uma grelha de coordenadas nativas sobre a página inteira, para
    escolher a caixa de recorte por leitura direta em vez de tentativa e
    erro (o maior desperdício de rodadas no método anterior).

O que este script NÃO faz
--------------------------
Não lê a letra manuscrita. Continua a ser necessário que o Claude Code
(visão multimodal) — ou o senhor — olhe para o ficheiro .jpg gerado e
transcreva/leia a data ou o texto. Não há aqui nenhum OCR para cursiva
seiscentista; isso seria "completar por contexto", que é exatamente o que
o protocolo do senhor proíbe.

Instalação
----------
    pip install requests pillow

Uso
---
    # 1) baixar/cachear e exportar a página inteira, com grelha de
    #    coordenadas nativas sobreposta (essencial para escolher a caixa
    #    de recorte sem tentativa e erro)
    python3 aa_crop_tool.py full --livro FAL-HT-PEDROMIGUEL-C-1641-1712 \
        --image 0021 --out page_0021.jpg --grid

    # 2) depois de ver a grelha e decidir a região (em coordenadas
    #    NATIVAS, as mesmas que a grelha rotula), recortar e ampliar:
    python3 aa_crop_tool.py crop --livro FAL-HT-PEDROMIGUEL-C-1641-1712 \
        --image 0021 --box 1470,350,130,90 --scale 14 --out crop_word.jpg

    # 3) (opcional, nem todos os livros expõem isto) listar o manifesto
    #    pages.js do livro:
    python3 aa_crop_tool.py manifest --livro FAL-HT-PEDROMIGUEL-C-1641-1712

Todas as imagens descarregadas ficam em ./cache/<LIVRO>/<LIVRO>_<NNNN>.jpg
— apague essa pasta se quiser forçar um novo download.
"""
import argparse
import json
import re
import sys
import time
from pathlib import Path

import requests
from PIL import Image, ImageDraw, ImageFont

BASE = "https://culturacores.azores.gov.pt/biblioteca_digital"
CACHE_DIR = Path(__file__).resolve().parent / "cache"
TIMEOUT = 30
RETRIES = 3


def master_url(livro: str, image_num: str) -> str:
    return f"{BASE}/{livro}/{livro}_master/{livro}_JPG/{livro}_{image_num}.jpg"


def manifest_url(livro: str) -> str:
    return f"{BASE}/{livro}/{livro}_item1/script/pages.js"


def fetch_bytes(url: str) -> bytes:
    last_err = None
    for attempt in range(1, RETRIES + 1):
        try:
            resp = requests.get(
                url,
                timeout=TIMEOUT,
                headers={"User-Agent": "Mozilla/5.0 (compatible; research-script/1.0)"},
            )
            resp.raise_for_status()
            return resp.content
        except Exception as e:
            last_err = e
            print(f"  tentativa {attempt}/{RETRIES} falhou: {e}", file=sys.stderr)
            if attempt < RETRIES:
                time.sleep(1.5 * attempt)
    raise RuntimeError(f"não foi possível obter {url}: {last_err}")


def get_page_image(livro: str, image_num: str) -> Image.Image:
    """Baixa (ou lê do cache) a imagem nativa da página e devolve um objeto PIL."""
    image_num = image_num.zfill(4)
    cache_dir = CACHE_DIR / livro
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_path = cache_dir / f"{livro}_{image_num}.jpg"
    if cache_path.exists():
        print(f"  (cache) {cache_path}")
    else:
        url = master_url(livro, image_num)
        print(f"  a descarregar {url}")
        data = fetch_bytes(url)
        cache_path.write_bytes(data)
        print(f"  guardado em {cache_path} ({len(data):,} bytes)")
    return Image.open(cache_path).convert("RGB")


def draw_grid(out_img: Image.Image, native_size, scale, step=100):
    """Sobrepõe uma grelha com rótulos em coordenadas NATIVAS (não nas
    coordenadas já escaladas da imagem de saída), para que o valor lido
    na grelha possa ser usado diretamente em --box."""
    img = out_img.copy()
    draw = ImageDraw.Draw(img)
    nw, nh = native_size
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 14)
    except Exception:
        font = ImageFont.load_default()
    for nx in range(0, nw, step):
        x = int(nx * scale)
        draw.line([(x, 0), (x, img.height)], fill=(255, 0, 0), width=1)
        draw.text((x + 2, 2), str(nx), fill=(255, 0, 0), font=font)
    for ny in range(0, nh, step):
        y = int(ny * scale)
        draw.line([(0, y), (img.width, y)], fill=(255, 0, 0), width=1)
        draw.text((2, y + 2), str(ny), fill=(255, 0, 0), font=font)
    return img


def cmd_full(args):
    img = get_page_image(args.livro, args.image)
    print(f"  tamanho nativo: {img.width}x{img.height}")
    out_img = img
    if args.scale != 1.0:
        out_img = img.resize(
            (max(1, int(img.width * args.scale)), max(1, int(img.height * args.scale))),
            Image.LANCZOS,
        )
    if args.grid:
        out_img = draw_grid(out_img, native_size=(img.width, img.height), scale=args.scale, step=args.grid_step)
    out_img.save(args.out, quality=90)
    print(f"  escrito: {args.out}  ({out_img.width}x{out_img.height})")


def cmd_crop(args):
    img = get_page_image(args.livro, args.image)
    try:
        sx, sy, sw, sh = (int(x) for x in args.box.split(","))
    except Exception:
        sys.exit("--box deve ser 'sx,sy,sw,sh' em coordenadas nativas (inteiros), ex: 1470,350,130,90")
    if sx < 0 or sy < 0 or sx + sw > img.width or sy + sh > img.height:
        print(
            f"  aviso: caixa ({sx},{sy},{sw},{sh}) excede os limites da imagem "
            f"({img.width}x{img.height}) — o recorte será cortado nos limites.",
            file=sys.stderr,
        )
        sx = max(0, sx)
        sy = max(0, sy)
        sw = min(sw, img.width - sx)
        sh = min(sh, img.height - sy)
    region = img.crop((sx, sy, sx + sw, sy + sh))
    if args.scale != 1.0:
        region = region.resize(
            (max(1, int(sw * args.scale)), max(1, int(sh * args.scale))), Image.LANCZOS
        )
    region.save(args.out, quality=92)
    print(
        f"  recorte nativo=({sx},{sy},{sw},{sh})  escala={args.scale}  "
        f"saída={region.width}x{region.height}  ficheiro={args.out}"
    )


def cmd_manifest(args):
    url = manifest_url(args.livro)
    print(f"  a descarregar manifesto {url}")
    try:
        raw = fetch_bytes(url).decode("utf-8", errors="replace")
    except Exception as e:
        sys.exit(
            f"não foi possível obter o manifesto: {e}\n"
            f"(nem todos os livros o expõem neste caminho; use 'full'/'crop' diretamente por número de imagem)"
        )
    m = re.search(r"=\s*(\[.*\])\s*;?\s*$", raw.strip(), re.S)
    if not m:
        m = re.search(r"(\[.*\])", raw, re.S)
    if not m:
        Path("manifest_raw.txt").write_text(raw)
        sys.exit("não consegui isolar o array JSON dentro de pages.js — conteúdo bruto em manifest_raw.txt")
    try:
        data = json.loads(m.group(1))
    except Exception as e:
        Path("manifest_raw.txt").write_text(raw)
        sys.exit(f"falha ao interpretar JSON ({e}); conteúdo bruto em manifest_raw.txt")
    print(f"  {len(data)} entradas.")
    limit = args.limit if args.limit else len(data)
    for i, entry in enumerate(data):
        if i >= limit:
            print(f"  ... (mais {len(data) - limit} entradas; use --limit 0 para ver todas)")
            break
        print(f"  [{i}] {entry}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    p_full = sub.add_parser("full", help="baixar/cachear e exportar a página inteira")
    p_full.add_argument("--livro", required=True)
    p_full.add_argument("--image", required=True, help="número da imagem, ex: 0021")
    p_full.add_argument("--out", required=True)
    p_full.add_argument("--scale", type=float, default=1.0)
    p_full.add_argument("--grid", action="store_true", help="sobrepor grelha de coordenadas nativas")
    p_full.add_argument("--grid-step", type=int, default=100, dest="grid_step")
    p_full.set_defaults(func=cmd_full)

    p_crop = sub.add_parser("crop", help="recortar região em coordenadas nativas e ampliar")
    p_crop.add_argument("--livro", required=True)
    p_crop.add_argument("--image", required=True)
    p_crop.add_argument("--box", required=True, help="sx,sy,sw,sh em coordenadas nativas")
    p_crop.add_argument("--scale", type=float, default=8.0)
    p_crop.add_argument("--out", required=True)
    p_crop.set_defaults(func=cmd_crop)

    p_man = sub.add_parser("manifest", help="listar o manifesto pages.js do livro (se existir)")
    p_man.add_argument("--livro", required=True)
    p_man.add_argument("--limit", type=int, default=20, help="0 = mostrar tudo")
    p_man.set_defaults(func=cmd_manifest)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
