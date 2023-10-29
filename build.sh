#!/bin/bash
mkdir -p output
rm -f output/*
#double build to make links work properly
pdflatex --enable-pipes --shell-escape ./Threads-of-Fate.tex
pdflatex --enable-pipes --shell-escape ./Threads-of-Fate.tex
