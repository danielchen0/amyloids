#!/bin/bash
set -euo pipefail

script_dir="$(cd "$(dirname "$0")" && pwd)"
stage_dir="$script_dir/output/submission/bulletin-of-mathematical-biology"
pdf_dir="$script_dir/output/pdf"
archive="$script_dir/output/bulletin-of-mathematical-biology-submission.zip"

cd "$script_dir"
./build.sh

mkdir -p "$stage_dir" "$pdf_dir"
cp main.tex abstract.txt references.bib main.bbl sn-jnl.cls sn-mathphys-ay.bst \
    Fig1.png Fig2.png Fig3.png Fig4.png main.pdf "$stage_dir/"
cp main.pdf "$pdf_dir/bulletin-of-mathematical-biology-submission.pdf"

rm -f "$archive"
(
    cd "$stage_dir"
    zip -q "$archive" main.tex abstract.txt references.bib main.bbl sn-jnl.cls \
        sn-mathphys-ay.bst Fig1.png Fig2.png Fig3.png Fig4.png main.pdf
)

echo "Created $archive"
echo "Created $pdf_dir/bulletin-of-mathematical-biology-submission.pdf"
