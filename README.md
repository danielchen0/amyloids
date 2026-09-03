# Amyloids

Combinatorial analysis of fluorescence in amyloids composed of split-YFP, Sup35p, and CFP using generating functions.

## Bulletin of Mathematical Biology submission manuscript

`main.tex` uses the official Springer Nature `sn-jnl` template (version 3.1,
December 2024), the journal's author--year reference style, double spacing, and
continuous line numbering. Compile with:

```
./build.sh
```

The build script uses `pdflatex` and `bibtex` when available, or `tectonic` as a
local fallback.

To build the PDF and a flat upload archive containing the manuscript, figures,
bibliography, class, and bibliography style, run:

```
./make_submission.sh
```

This creates:

- `output/pdf/bulletin-of-mathematical-biology-submission.pdf`
- `output/bulletin-of-mathematical-biology-submission.zip`

The upload archive includes the editable LaTeX source and `abstract.txt`, a
plain-text version of the abstract suitable for the submission form. The author
affiliation is Independent Researcher, San Francisco, United States. The
original arXiv source bundle remains in `arxiv_submission/`.

## Simulation scripts

Each script computes the expected percentage of proteins involved in fluorescence, R(n), for increasing amyloid length n:

| Script | Section | System | Asymptote |
|--------|---------|--------|-----------|
| `split_yfp_simulation.py` | 2 | Split-YFP only | 2/3 |
| `sup35_simulation.py` | 3 | Split-YFP + Sup35p | 1/3 |
| `fret_sup35_simulation.py` | 4 | FRET YFP/CFP + Sup35p | TBD |

## Plot scripts

Each generates the corresponding figure included in the paper:

| Script | Output |
|--------|--------|
| `plot_split_yfp.py` | `SplitYFPamyloids.png` |
| `plot_sup35.py` | `splityfpandsup35.png` |
| `plot_fret_sup35.py` | `FretandSup35.png` |
| `plot_submission_figures.py` | `Fig1.png`--`Fig4.png` (600 dpi, journal submission) |

Requires matplotlib:

```
python3 -m venv .venv
source .venv/bin/activate
pip install matplotlib
```

Then run any plot script, e.g. `python plot_split_yfp.py`.
