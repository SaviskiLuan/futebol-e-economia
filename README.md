# Futebol e economia

Projeto final da unidade curricular **Visualização de Dados** · SENAI CIC · Turma Bosch · Profa. Lívia Stein Freitas

Investigamos se a diferença de renda e de desenvolvimento humano entre dois países influencia o resultado dos jogos entre suas seleções em Copas do Mundo (1990–2018).

## Equipe

| Integrante | GitHub |
| --- | --- |
| Luan Saviski | @SaviskiLuan
| Miguel Gradella | @miguel-gradella
| Gabriel Wendt | @GabrielWendt

## Perguntas

1. Em jogos de Copa (1990–2018), a seleção do país com maior renda per capita vence com mais frequência?
2. A diferença de renda per capita entre os dois times é maior quando o mais rico vence do que quando empata ou perde?
3. A vantagem do país mais rico mudou de 1990 a 2018?
4. Onde estão os países que mais venceram jogos de Copa desde 1990?
5. Seleções de países com IDH maior marcam mais gols por jogo em Copas?

## Fontes dos dados

| Dataset | Arquivos usados | Período |
| --- | --- | --- |
| [World Cup · Maven Analytics](https://mavenanalytics.io/data-playground/world-cup) | `world_cup_matches.csv`, `world_cups.csv` | 1930–2018 (placar) |
| [World Economic Indicators · Maven Analytics](https://mavenanalytics.io/data-playground) | `HDI.csv` | 1990–2021 |

## Estrutura

```
futebol-e-economia/
├── README.md
├── requirements.txt
├── data/            # datasets originais
│   └── limpos/      # dados limpos gerados pelo notebook 01
├── notebooks/       # 01_limpeza.ipynb
├── src/             # paises.py (correspondência seleção -> iso3)
├── images/          # gráficos em PNG
└── docs/            # documentação técnica e slides
```

## Como executar

```bash
git clone https://github.com/USUARIO/futebol-e-economia.git
cd futebol-e-economia
pip install -r requirements.txt
jupyter notebook notebooks/01_limpeza.ipynb
```

Rode todas as células (*Run All*). Os arquivos limpos são gravados em `data/limpos/`.
