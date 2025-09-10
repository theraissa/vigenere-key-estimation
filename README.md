
# Tarefa 3 – Estimativa de Chave no Cifrador de Vigenère


O Cifrador de Vigenère é uma cifra de substituição polialfabética: usa várias substituições de César em sequência, determinadas por uma palavra-chave.
Quebrá-lo exige identificar o tamanho da chave (com métodos como Índice de Coincidência) e depois aplicar análise de frequência em cada coluna.

### Referências externas:

* Stinson, D. – Cryptography: Theory and Practice, Capítulo 1.
* Técnicas de ataque: Kasiski Examination, Index of Coincidence.

## O que fazer

1. Escolha 2 textos claros (≥ 1200 caracteres).
2. Crie duas palavras-chave de 3–10 letras cada.
3. Implemente:
* Cifragem Vigenère.
* Ataque para estimar o tamanho da chave (IC/Kasiski).
* Decifração aproximada, tentando recuperar a chave completa.
4. Compare resultados: tamanho estimado vs real, taxa de acerto da chave, taxa de acerto da mensagem.

## Entrega

* Link para repositório público com código containerizado (use Docker Compose).
* Link para vídeo no youtube com apresentação e explicação:
    * explicação do Vigenère e da tabula recta,
    * descrição de IC/Kasiski,
    * experimentos com tabelas e gráficos.
    * demonstração do código em execução;