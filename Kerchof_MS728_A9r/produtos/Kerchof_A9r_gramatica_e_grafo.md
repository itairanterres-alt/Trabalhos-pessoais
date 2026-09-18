# Kerchof MS 728 — A9r — A gramática dos colchetes e o grafo reconstruído
## Versão 0.3

---

## 1. A REGRA

Derivada dos dois calibradores fornecidos, verificada em 7 colchetes independentes e
confirmada uma vez pelo **próprio texto do manuscrito**.

> **G1.** Um colchete é um traço vertical longo e contínuo desenhado **sobre a divisa** entre a
> coluna Cᵢ e a coluna Cᵢ₊₁. Não há linhas de descendência: o colchete é o único conector.
>
> **G2.** O colchete **abraça a fratria em Cᵢ₊₁** — todas as entradas de Cᵢ₊₁ cuja faixa vertical
> cai dentro do seu *span*. A extensão vertical do colchete é, por construção, a extensão do
> conjunto de irmãos.
>
> **G3.** O **progenitor** está em Cᵢ e é identificado por uma **saliência lateral esquerda
> (cusp)** — um desvio de 30–100 px da haste, com 18–70 px de altura — que Kerchof desenha
> **na metade inferior do colchete** (medido: 47 %, 50 %, 54 %, 60 %, 62 %, 76 %, 81 %, 83 %, 90 %
> do span). O verbete de Cᵢ que contém a altura desse cusp é o progenitor.
>
> **G4.** Não há contato de tinta entre colchete e verbete, em nenhum ponto do fólio. A relação é
> **posicional e marcada pelo cusp**, nunca por continuidade de traço.
>
> **G5.** Entradas sem colchete à direita são **terminais gráficos**: Kerchof não lhes desenha
> descendência.
>
> **G6.** Numa mesma divisa, os colchetes **particionam** o espaço vertical quase sem
> sobreposição (lacunas de 10–40 px entre colchetes consecutivos). Cada partição = uma fratria.

### Por que o cusp, e não a sobreposição

Sobreposição simples **falha** no calibrador BR-C: o span (y2052–3130) cobre três verbetes de C05
— V07, V08 e V09 — e o progenitor calibrado é V09, que é o que tem *menor* sobreposição (32 %).
O cusp resolve: BR-C tem saliência esquerda em **y2922–2950**, dentro de V09. A sobreposição
elegeria V07 ou V08, ambos errados.

V07 e V08 não podem ser progenitores porque são, eles próprios, a fratria abraçada por **BR-A**
(span 2159–2790), que os cobre exatamente e termina 11 px antes de V09 começar. G6 em ação.

---

## 2. VALIDAÇÃO

**Calibrador 1 — BR-B** (id38682, C04/C05, y2801–3687)
cusp y3331–3361 (60 % do span) → progenitor **C04-V09**; fratria **C05-V09**.
C05-V09 é o bloco que contém Jan × Barbe Fertyns. ✔ reproduz o calibrador.

**Calibrador 2 — BR-C** (id32531, C05/C06, y2052–3130)
cusp y2922–2950 (81 %) → progenitor **C05-V09** (Jan × Barbe); fratria **C06-V07, V08, V09**.
Esses três blocos contêm exatamente quatro indivíduos: Nicolas, Pierre, Petronelle,
Anne × Jan Bave. ✔ reproduz o calibrador.

**Núcleo 3 — o manuscrito valida a si próprio.** id35593 (C02/C03, y2450–3953), cusp y3161–3193
(47 %) → progenitor **C02-V07** (Bernard); fratria **C03-V10, V11, V12**.
Ora, C03-V10 contém o verbete que diz **«fut tuteur des infans de Simon son frere»**, e C03-V11
contém **Simon**. A regra, aplicada só à geometria, põe os dois na mesma fratria — e o texto
declara, independentemente, que são irmãos. **Esta é a validação mais forte disponível: não vem
de mim nem de Gailliard, vem do próprio Kerchof.**

**Núcleos 4–9** — a regra do cusp dispara e resolve sem ambiguidade em: id23957 (C05/C06),
id33336 (C04/C05), id23752 (C06/C07), id20965 (C07/C08), id37464 (C08/C09), id28471 (C09/C10).

**Cobertura:** 32 colchetes no fólio. **9 resolvidos por cusp** (alta confiança).
**23 resolvidos por sobreposição** (fallback, confiança média) — nestes o progenitor é
provisório, e onde o span cobre mais de um verbete de Cᵢ a atribuição fica em aberto.

---

## 3. GRAFO — mapa completo dos colchetes

`→` = progenitor → fratria. Blocos V são unidades gráficas; alguns contêm mais de um verbete.

| divisa | colchete | span | progenitor | via | fratria |
|---|---|---|---|---|---|
| C01/C02 | id21311 | 867–3774 | C01-V01 | sobrep. | C02-V02…V07 |
| C02/C03 | id19566 | 703–1247 | C02-V02 | sobrep. | C03-V04, V05 |
| C02/C03 | id25436 | 1244–2007 | **C02-V04 (Gillis)** | sobrep. | C03-V06, V07 |
| C02/C03 | id33013 | 2115–2366 | C02-V05 | sobrep. | C03-V08 |
| C02/C03 | id35593 | 2450–3953 | **C02-V07 (Bernard)** | **cusp** | C03-V10, V11, V12 |
| C03/C04 | id14213 | 172–2146 | C03-V02 | sobrep. | C04-V02…V06 |
| C03/C04 | id33360 | 2162–3289 | C03-V08 *(ou V10 — ambíguo)* | sobrep. | C04-V07, V08 |
| C03/C04 | id43058 | 3301–3574 | **C03-V11** | sobrep. | **C04-V09** |
| C03/C04 | id45249 | 3575–3764 | C03-V11 | sobrep. | — |
| C04/C05 | id17168 | 457–637 | C04-V02 | sobrep. | — |
| C04/C05 | id19158 | 660–2128 | **C04-V03 (Tillegem I)** | sobrep. | C05-V03…V06 |
| C04/C05 | id33336 | 2159–2790 | **C04-V08** | **cusp** | C05-V07, V08 |
| C04/C05 | id38682 | 2801–3687 | **C04-V09** | **cusp** | **C05-V09** |
| C05/C06 | id15827 | 325–545 | C05-V02 | sobrep. | — |
| C05/C06 | id20651 | 802–1052 | C05-V03 | sobrep. | C06-V04 |
| C05/C06 | id23957 | 1106–1570 | C05-V04 | **cusp** | C06-V05 |
| C05/C06 | id28679 | 1594–1854 | C05-V05 | sobrep. | C06-V06 |
| C05/C06 | id32531 | 2052–3130 | **C05-V09 (Jan × Barbe)** | **cusp** | **C06-V07, V08, V09** |
| C06/C07 | id14248 | 175–491 | C06-V02 | sobrep. | C07-V02, V03 |
| C06/C07 | id23752 | 1087–2213 | C06-V07 | **cusp** | C07-V04 |
| C06/C07 | id34313 | 2285–2703 | C06-V07 | sobrep. | C07-V05 |
| C07/C08 | id20965 | 833–1280 | C07-V04 | **cusp** | C08-V02 |
| C07/C08 | id26997 | 1413–1691 | C07-V04 | sobrep. | C08-V03 |
| C07/C08 | id29976 | 1745–2192 | C07-V04 | sobrep. | — |
| C07/C08 | id33885 | 2230–2420 | C07-V05 | sobrep. | — |
| C07/C08 | id35437 | 2427–3463 | C07-V05 | sobrep. | C08-V05, V06 |
| C08/C09 | id19593 | 705–940 | C08-V02 | sobrep. | C09-V02 |
| C08/C09 | id22064 | 935–1123 | C08-V02 | sobrep. | — |
| C08/C09 | id37464 | 2658–2912 | C08-V05 | **cusp** | C09-V05 |
| C08/C09 | id39773 | 2923–3194 | C08-V06 | sobrep. | — |
| C09/C10 | id19340 | 682–1089 | C09-V02 | sobrep. | — |
| C09/C10 | id28471 | 1571–2062 | C09-V03 | **cusp** | C10-V02 |

**Ressalva sobre os três colchetes gigantes** (id21311 h=2907, id14213 h=1974, id19158 h=1468):
nenhum tem cusp. Podem ser réguas de coluna e não colchetes. Onde não há cusp, a leitura
«fratria» é hipótese, não resultado.

---

## 4. A CADEIA PEDIDA

### 4.1 Gillis/Gilles — **corrigindo a v0.2**

**C02-V04 = Gillis, bourgmestre de Bruges, 1333.**
Tem colchete à direita: **id25436 (y1244–2007) → fratria C03-V06, C03-V07.**

Na v0.2 respondi que Gillis **não tinha filhos desenhados**. **Estava errado.** Eu procurava uma
linha de tinta; a gramática mostra um colchete. Gillis tem descendência gráfica.

Mas: **nem C03-V06 nem C03-V07 são progenitores de qualquer colchete C03/C04.** Logo a linha de
Gillis é **terminal na 3ª coluna** e **não alcança o século XV**. A resposta 5 da Etapa 7
continua «não», agora por razão demonstrada e não por ausência de conector.

### 4.2 Bernard — o tronco que efetivamente desce

**C02-V07 = Bernard × Marie Bonin (2ª Cecilie de Rechteberghe)**
→ id35593 → **C03-V10, V11, V12**
 · C03-V10 = Jan, trésorier de Bruges + **Georges** («tuteur des infans de Simon son frere»)
 · C03-V11 = Jan (ob. 1355) + **Simon** (ob. 1371)
 · C03-V12 = Catherine × Jan van Rechteberghe

### 4.3 Até os ramos do século XV

**C03-V11** → id43058 → **C04-V09**
**C04-V09** → id38682 (BR-B, cusp) → **C05-V09**
**C05-V09** → id32531 (BR-C, cusp) → **C06-V07, V08, V09**

Isto é: a descendência que chega a 1441 e a 1461 vem de **Bernard**, pela fratria de
C03-V11, e **não de Gillis**.

### 4.4 Os Jans senhores de Tillegem

**C04-V03** (o primeiro verbete que traz o título «s. de Tillegem») → id19158 →
**C05-V03…V06**. C05-V03 é o verbete que traz de novo o título «s. de Tilleghem».
Portanto Kerchof **desenha** sucessão entre os dois senhores de Tillegem: são pai e filho,
em colunas consecutivas.

Ressalva: id19158 não tem cusp (é um dos três gigantes). A cadeia Tillegem é, por isso,
a parte **menos segura** de toda a reconstrução. As duas cadeias fortes — Bernard→XV e
Jan×Barbe→4 filhos — repousam em cusps.

---

## 5. TESTE CEGO CONTRA GAILLIARD

Feito **depois** de fechar a reconstrução, sem usar Gailliard em nenhum passo acima.

| Reconstrução Kerchof (cega) | Gailliard/AT-01 | Veredicto |
|---|---|---|
| id33336 (cusp): **C04-V08 → C05-V07 (Jacques, eschevin 1416) + C05-V08 (Georges, 1413)**. C04-V08 é o verbete de Georges × Cornelie, eschevin 1378. | AL-106: «Gailliard atribui a **Georges** ativo em 1374 e **Cornélie Alsoens** filhos **Jacques ativo em 1416** e **Georges ativo em 1413**» | **ACERTO CEGO.** A geometria, sozinha, produziu pai, mãe e os dois filhos com os dois anos. Divergência só na data do pai: Kerchof 1378, Gailliard 1374. |
| id32531 (cusp): **Jan × Barbe → Nicolas, Pierre, Petronelle, Anne × Jan Bave** | H1 do AT-01: prole Petronelle, Anne, Barbele, Margriete, **Pieter**, **Nicolas** | **ACERTO PARCIAL.** Quatro dos seis coincidem. Barbele e Margriete **não** estão na fratria de BR-C. |
| id38682 (cusp): **C04-V09 → C05-V09**, e C04-V09 é Jacques × Marie van de Walle, mort **1400** | AL-110: Claeys, «Jacob × Maria van de Walle, nº 71 de 1393, morto **1405**» | **Estrutura confirmada, data diverge** (1400 × 1405). |
| id35593 (cusp): **Bernard → {Jan, Georges}, {Jan, Simon}, {Catherine}** | AL-101: Franck, fundação de 1355 — filhos do falecido Bernard: **Jan, Joris, Jacop** | **Parcial.** Jan ✓ e Joris/Georges ✓. **Jacop não aparece** na fratria; no lugar dele Kerchof desenha um segundo Jan, um Simon e uma Catherine. |

### Consequência para a divergência 10b do confronto anterior

Na v0.2 registrei que a prole desenhada sob Jan × Barbe não batia com H1. **A gramática resolve
a divergência e ela era minha, não do manuscrito:** o grupo que eu tomara por filhos
(Georges religioso, duas Marguerite, Barbe, Catherine †1429) é a **fratria de Jan × Barbe** —
são seus **irmãos**, abraçados com ele por BR-B. Os filhos dele são os quatro de BR-C, e esses
sim batem com H1. **A linha 10b do arquivo de confronto deve ser reclassificada de E para A parcial.**

---

## 6. O QUE ESTA VERSÃO NÃO ENTREGA

- O grafo K001…Kn indivíduo a indivíduo. A segmentação gráfica resolve **blocos** (V), e vários
  blocos contêm 2–5 verbetes. Descer de V para K exige um passo de leitura que esta rodada não fez.
- Os 23 colchetes sem cusp. Onde o span cobre mais de um verbete de Cᵢ, o progenitor fica
  em aberto — e é o caso, entre outros, da cadeia de Tillegem.
- Verificação de que os três traços gigantes são colchetes e não réguas.

Nada disto foi integrado ao AT-01.
