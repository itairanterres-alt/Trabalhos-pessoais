# Tutorial: instalar e usar o Humanizador PT

Guia passo a passo. Escolha o caminho conforme onde você usa o Claude. Se usa os dois, o app e o Claude Code, faça os dois: são instalações independentes e não conflitam.

---

## Caminho 1: no app do Claude (site, desktop ou celular)

É o caminho mais simples e não exige terminal. A skill passa a valer em qualquer conversa sua.

**Passo 1. Baixe o arquivo da skill.**
O arquivo é `humanizador-pt.skill`, que está nesta pasta do repositório. Abra o GitHub em
`itairanterres-alt/Trabalhos-pessoais` → `.claude/skills/humanizador-pt/` → clique em
`humanizador-pt.skill` → botão **Download** (ícone de seta para baixo). Ele vai para a
pasta de Downloads do seu computador.

**Passo 2. Abra as configurações de habilidades.**
No app do Claude, clique no seu nome ou avatar, no canto inferior esquerdo, e vá em
**Configurações → Capacidades → Habilidades** (em inglês, *Settings → Capabilities → Skills*).
Dependendo da versão, o caminho aparece como **Personalizar → Habilidades**.

**Passo 3. Adicione a skill.**
Clique em **+** (ou **Criar habilidade**) e escolha a opção de **carregar um arquivo ZIP**.
Selecione o `humanizador-pt.skill` que você baixou. O app lê o arquivo e mostra o nome da
skill na lista.

**Passo 4. Confirme que está ligada.**
A skill precisa aparecer na lista com o interruptor ativado. Se estiver desligada, clique
para ligar.

**Passo 5. Teste.**
Abra uma conversa nova e escreva: `humanize este texto:` e cole qualquer parágrafo.
O Claude deve devolver o texto reescrito, sem travessões longos.

> Se o app recusar o arquivo, renomeie `humanizador-pt.skill` para `humanizador-pt.zip`
> e tente de novo. É o mesmo formato por dentro; alguns navegadores e versões do app só
> aceitam a extensão `.zip`.

---

## Caminho 2: no Claude Code do seu computador

Assim a skill fica disponível em qualquer projeto que você abrir com o Claude Code.

**Passo 1. Abra o terminal.**
No Mac, aplicativo Terminal. No Windows, o PowerShell ou o terminal do próprio Claude Code.

**Passo 2. Copie a pasta da skill para a pasta pessoal de skills.**
Cole o comando abaixo e tecle Enter. Ele cria a pasta de skills, caso não exista, e baixa
o repositório para dentro dela:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/itairanterres-alt/Trabalhos-pessoais /tmp/trabalhos-pessoais
cp -r /tmp/trabalhos-pessoais/.claude/skills/humanizador-pt ~/.claude/skills/
rm -rf /tmp/trabalhos-pessoais
```

Traduzindo o que cada linha faz: a primeira cria a pasta onde o Claude Code procura skills;
a segunda baixa uma cópia temporária do repositório; a terceira copia só a pasta da skill
para o lugar definitivo; a quarta apaga a cópia temporária, que não serve mais.

**Passo 3. Reinicie o Claude Code.**
Feche e abra de novo. Skills são lidas na abertura da sessão.

**Passo 4. Confirme.**
Digite `/` na caixa de mensagem: `humanizador-pt` deve aparecer na lista de skills
disponíveis. Ou simplesmente escreva `humanize este texto:` e cole um parágrafo.

**Para atualizar depois**, quando houver mudança no repositório, repita o Passo 2. A cópia
nova substitui a antiga.

---

## Caminho 3: dentro deste repositório

Nada a fazer. A skill está em `.claude/skills/humanizador-pt/` e qualquer sessão do Claude
Code aberta na pasta `Trabalhos-pessoais` a reconhece sozinha. Este caminho só vale aqui
dentro, por isso existem os caminhos 1 e 2.

---

## Como usar no dia a dia

Não há comando fixo a decorar. Escreva o pedido em linguagem normal e cole o texto em
seguida:

```
humanize este texto:
[cole aqui]
```

Outras formas que funcionam igual: "remova os padrões de IA", "reescreva em tom mais
natural", "está soando muito de chatbot, corrija", "revise antes de eu enviar".

Variações úteis:

| O que você quer | O que escrever |
| --- | --- |
| Só apontar os problemas, sem reescrever | `só o diagnóstico, não reescreva` |
| Revisar sem o seu contexto de voz | `humanize usando só os 24 padrões, sem contexto de voz` |
| Revisar um arquivo inteiro (Claude Code) | `humanize o arquivo caminho/para/texto.md` |
| Só tirar os travessões | `aplique só a regra crítica dos travessões` |

O que a skill nunca faz: alterar dado, nome, data, dose, unidade, sigla clínica, referência
bibliográfica, número de norma ou citação direta. Se encontrar afirmação sem fonte, ela
avisa, mas não inventa a referência.

---

## Como ajustar o seu contexto de voz

O arquivo `contexts/itair-terres.md` guarda as regras da sua escrita: o que evitar, o que
preservar, como varia o tom entre saúde, educação e gestão. Ele é lido automaticamente
antes de cada revisão.

Para mudar alguma coisa, edite o arquivo direto no GitHub: abra
`.claude/skills/humanizador-pt/contexts/itair-terres.md`, clique no ícone de lápis, altere
e salve (*Commit changes*). Depois refaça a instalação do caminho que você usa, para a
versão nova chegar até lá.

O mais fácil, porém, é pedir aqui mesmo: "acrescente ao meu contexto de voz que eu nunca
uso a expressão X". Eu edito, faço o commit e gero o arquivo `.skill` atualizado.

Para criar um perfil diferente, por exemplo uma voz institucional do curso de medicina,
copie `contexts/CONTEXT-TEMPLATE.md` com outro nome, preencha e acione assim:
`humanize usando o contexto em contexts/curso-medicina.md`.

---

## Quando algo não funciona

**A skill não aparece na lista.** No app, confirme que o interruptor está ligado em
Configurações → Capacidades → Habilidades. No Claude Code, confirme que o arquivo está
exatamente em `~/.claude/skills/humanizador-pt/SKILL.md` e reinicie o programa.

**O texto voltou com travessões.** Responda "ainda há travessões longos, elimine todos".
A regra é explícita na skill e a terceira passagem existe justamente para isso.

**A revisão mexeu em termo técnico.** Avise qual termo. Isso indica lacuna no contexto de
voz, e a correção é acrescentar o termo à lista de preservação obrigatória.

**A revisão ficou fraca demais.** Peça "seja mais agressivo, o texto ainda soa como IA" e
indique o trecho. A skill reexecuta as passagens 2 e 3 sobre o que você apontou.
