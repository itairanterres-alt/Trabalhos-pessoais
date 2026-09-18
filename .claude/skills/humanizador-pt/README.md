# Humanizador PT (adaptado)

Skill de revisão que detecta e elimina padrões de escrita artificial em português brasileiro.

## Instalação e uso

A skill já está no lugar certo: `.claude/skills/humanizador-pt/`. Qualquer sessão do Claude Code aberta neste repositório a reconhece automaticamente. Para deixá-la disponível em todos os projetos, copie a pasta para `~/.claude/skills/humanizador-pt/` na máquina local.

Acionamento por linguagem natural, sem comando fixo:

```
humanize este texto
remova os padrões de IA
reescreva em tom mais natural
está soando muito de chatbot, corrija
só o diagnóstico, não reescreva
```

O contexto de voz em `contexts/itair-terres.md` é carregado automaticamente. Para desligá-lo numa revisão específica, peça "humanize usando só os 24 padrões, sem contexto de voz".

## Arquivos

| Arquivo | Função |
| --- | --- |
| `SKILL.md` | Definição da skill: regra crítica dos travessões, 24 padrões, três passagens, regras de preservação |
| `contexts/itair-terres.md` | Contexto de voz pessoal: registro por domínio, nomenclatura clínica e bioética preservada, expressões a evitar, notas por gênero textual |
| `contexts/CONTEXT-TEMPLATE.md` | Template em branco para criar outros perfis de voz |
| `LICENSE` | MIT, do repositório de origem |

## O que mudou em relação ao original

O repositório de origem anuncia 24 padrões, mas a numeração salta do 17 para o 19: são 23 na prática. O padrão 18, que o README original descrevia como "travessões longos em excesso", tinha sido promovido a regra crítica e sumiu da lista.

Nesta versão:

1. O padrão 18 foi reescrito como **pontuação de efeito e simetria tipográfica**, cobrindo dois-pontos dramáticos, reticências, aspas de ironia e pares de frases espelhados, que a regra crítica não alcança. A lista volta a ter 24 itens.
2. O carregamento do contexto de voz virou etapa explícita antes da Passagem 1, em vez de depender de o usuário citar o arquivo a cada pedido.
3. As regras de preservação ganharam referências bibliográficas, normas e dispositivos legais, citações diretas literais e a instrução de preservar a precisão técnica quando ela colidir com a humanização.
4. Os padrões 23 e 24 passaram a proibir explicitamente inventar referência ou análise ausente: a lacuna é sinalizada ao autor.
5. O padrão 4 (disclaimer) ganhou ressalva para avisos exigidos por norma ou pelo gênero, como bula, laudo, parecer e material de orientação a pacientes.
6. O padrão 20 incorporou a variação de extensão das frases, não só a subordinação.
7. Foram acrescentadas exceções legítimas: travessão de diálogo em texto literário e voz passiva na descrição de método em texto científico.
8. A skill passou a definir o formato da resposta, com texto humanizado primeiro e nota de revisão depois, e a suportar o pedido de diagnóstico sem reescrita.

## Créditos

Adaptado de [opaulomarcondes/humanizador-pt](https://github.com/opaulomarcondes/humanizador-pt) (MIT, Paulo Marcondes), derivado de [blader/humanizer](https://github.com/blader/humanizer) (MIT), apoiado no guia [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
