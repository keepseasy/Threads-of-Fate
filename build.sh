#!/bin/bash
mkdir -p output
rm -f output/*
#double build to make links work properly
texfot pdflatex --shell-escape -halt-on-error -output-directory=output ./Threads-of-Fate.tex
texfot pdflatex --shell-escape -halt-on-error -output-directory=output ./Threads-of-Fate.tex
