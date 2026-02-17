# Amyloids

Combinatorial analysis of fluorescence in amyloids composed of split-YFP, Sup35p, and CFP using generating functions.

## Paper

`main.tex` — the main LaTeX document. Compile with:

```
./build.sh
```

Requires `pdflatex` and `bibtex`.

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

Requires matplotlib:

```
python3 -m venv .venv
source .venv/bin/activate
pip install matplotlib
```

Then run any plot script, e.g. `python plot_split_yfp.py`.
