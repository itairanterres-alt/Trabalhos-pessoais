# aa_crop_tool.py — guia rápido

Substitui o pipeline anterior (painel de navegador → canvas → ponte base64
→ decode.py) por um script Python simples, para correr no Claude Code
local, no seu computador. Resolve três atritos concretos que estavam a
consumir rodadas na conversa:

1. O sandbox em nuvem tem a rede bloqueada para este domínio (testado agora
   mesmo: `403`, `CONNECT tunnel failed`). No seu computador isso
   normalmente não acontece.
2. A ponte de recorte tinha um limite de ~800.000 caracteres por resultado,
   obrigando a escalas reduzidas e a várias idas e vindas.
3. Cada recorte exigia adivinhar a caixa `(sx,sy,sw,sh)` por tentativa e
   erro — foi o que aconteceu com a palavra "seis/oito annos" no fólio 21
   (três tentativas até acertar).

O que não muda: a leitura da letra continua a ser feita por si ou pelo
Claude Code a olhar para o ficheiro `.jpg` gerado. O script só busca e
recorta — não lê nem interpreta.

## Instalação

```
pip install requests pillow
```

## Uso

```bash
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
```

Todas as imagens descarregadas ficam em `./cache/<LIVRO>/<LIVRO>_<NNNN>.jpg`
— apague essa pasta se quiser forçar um novo download.

## O que este script NÃO faz

Não lê a letra manuscrita. Continua a ser necessário que o Claude Code
(visão multimodal) — ou o senhor — olhe para o ficheiro `.jpg` gerado e
transcreva/leia a data ou o texto. Não há aqui nenhum OCR para cursiva
seiscentista; isso seria "completar por contexto", que é exatamente o que
o protocolo do senhor proíbe.
