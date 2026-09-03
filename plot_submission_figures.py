#!/usr/bin/env python3
"""Generate submission-quality figures for the Springer Nature manuscript."""

import matplotlib.pyplot as plt

from split_yfp_simulation import expected_value


def save_ratio_plot(filename, ns, values, limit, ylabel):
    """Save a monochrome, publication-ready ratio plot."""
    figure, axis = plt.subplots(figsize=(6.4, 4.8))
    axis.plot(ns, values, color="black", linewidth=1.6, label="Exact ratio")
    axis.axhline(
        y=limit,
        color="0.35",
        linestyle="--",
        linewidth=1.4,
        label="Limiting ratio",
    )
    axis.set_xlabel(r"Amyloid length $n$")
    axis.set_ylabel(ylabel)
    axis.legend(frameon=False)
    axis.grid(axis="y", color="0.88", linewidth=0.6)
    figure.tight_layout()
    figure.savefig(filename, dpi=600, bbox_inches="tight")
    plt.close(figure)
    print(f"Saved {filename}")


n_split = list(range(4, 404))
save_ratio_plot(
    "Fig1.png",
    n_split,
    [2 * expected_value(n) / n for n in n_split],
    2 / 3,
    r"$R_{\mathrm{SY}}(n)$",
)

n_sup35 = list(range(2, 402))
save_ratio_plot(
    "Fig2.png",
    n_sup35,
    [
        (4 * n - 3) / (12 * n) + ((-1) ** n) / (12 * n * 3 ** (n - 1))
        for n in n_sup35
    ],
    1 / 3,
    r"$R_{\mathrm{SY},S}(n)$",
)

n_fret = list(range(2, 402))
save_ratio_plot(
    "Fig3.png",
    n_fret,
    [(n - 1) / (2 * n) for n in n_fret],
    1 / 2,
    r"$R_{\mathrm{F}}(n)$",
)

save_ratio_plot(
    "Fig4.png",
    n_fret,
    [2 * (n - 1) / (9 * n) for n in n_fret],
    2 / 9,
    r"$R_{\mathrm{F},S}(n)$",
)
