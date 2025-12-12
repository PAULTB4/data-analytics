import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def set_style():
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update({
        "figure.figsize": (11, 6),
        "axes.titlesize": 14,
        "axes.labelsize": 12,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
    })


def format_millions(x, _):
    return f"{x/1_000_000:.1f} M"
