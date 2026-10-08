"""
Estilo comum a todos os gráficos do projeto.

Um único lugar define cores, título, subtítulo, fonte e o salvamento em PNG.
Assim todos os gráficos ficam com a mesma cara, e a mesma coisa tem sempre a mesma cor
(ex.: "vitória do mais rico" é sempre azul).
"""

import os

import matplotlib.pyplot as plt

# Paleta: uma cor de destaque e tons de cinza para o resto (sem vermelho x verde).
AZUL = "#2a78d6"        # destaque: o que importa no gráfico
AZUL_CLARO = "#a9c8ee"
CINZA = "#c4c4c4"       # contexto
CINZA_ESCURO = "#6b6b6b"
TEXTO = "#222222"
TEXTO_SUAVE = "#666666"

# Cores fixas por resultado do país mais rico (mesmas em todos os gráficos)
CORES_RESULTADO = {"vitoria": AZUL, "empate": CINZA, "derrota": CINZA_ESCURO}
NOMES_RESULTADO = {"vitoria": "Vitória", "empate": "Empate", "derrota": "Derrota"}

FONTE_PADRAO = ("Fonte: Maven Analytics · World Cup e World Economic Indicators (PNUD) · "
                "Copas de 1990 a 2018")


def aplicar_estilo():
    """Remove bordas e grades desnecessárias e define fontes legíveis."""
    plt.rcParams.update({
        "figure.dpi": 110,
        "font.size": 11,
        "axes.edgecolor": CINZA,
        "axes.labelcolor": TEXTO_SUAVE,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": False,
        "xtick.color": TEXTO_SUAVE,
        "ytick.color": TEXTO_SUAVE,
        "legend.frameon": False,
    })


def _caixa(fig):
    """Retângulo (em polegadas) ocupado pelo conteúdo do gráfico."""
    fig.canvas.draw()
    return fig.get_tightbbox(fig.canvas.get_renderer())


def titulo(fig, texto, subtitulo):
    """Título-conclusão em negrito e subtítulo com medida e período, acima do gráfico."""
    caixa = _caixa(fig)
    larg, alt = fig.get_size_inches()
    x = caixa.x0 / larg
    fig.text(x, (caixa.y1 + 0.12) / alt, subtitulo, ha="left", va="bottom",
             fontsize=10.5, color=TEXTO_SUAVE)
    fig.text(x, (caixa.y1 + 0.42) / alt, texto, ha="left", va="bottom",
             fontsize=14, fontweight="bold", color=TEXTO)


def fonte(fig, texto=FONTE_PADRAO):
    """Fonte dos dados no rodapé, logo abaixo do gráfico."""
    caixa = _caixa(fig)
    larg, alt = fig.get_size_inches()
    fig.text(caixa.x0 / larg, (caixa.y0 - 0.12) / alt, texto, ha="left", va="top",
             fontsize=8.5, color=TEXTO_SUAVE)


def num(valor, casas=2):
    """Número no formato brasileiro (vírgula decimal): num(0.53) -> '0,53'."""
    return f"{valor:.{casas}f}".replace(".", ",")


def salvar(fig, nome, pasta="../images"):
    """Salva em PNG na pasta images/ com nome numerado (ex.: '01_resultado_mais_rico')."""
    os.makedirs(pasta, exist_ok=True)
    caminho = os.path.join(pasta, f"{nome}.png")
    fig.savefig(caminho, dpi=150, bbox_inches="tight", facecolor="white")
    print("Salvo:", caminho)
