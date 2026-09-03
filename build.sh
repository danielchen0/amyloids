#!/bin/bash
set -euo pipefail

if command -v pdflatex >/dev/null 2>&1 && command -v bibtex >/dev/null 2>&1; then
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    bibtex main
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
elif command -v tectonic >/dev/null 2>&1; then
    tectonic main.tex --keep-logs --keep-intermediates
else
    echo "Error: install pdflatex and bibtex, or install tectonic." >&2
    exit 1
fi
