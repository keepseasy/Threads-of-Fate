#!/bin/bash
mkdir -p output
rm -f output/*
#double build to make links work properly
pdflatex --enable-pipes --shell-escape -output-directory=output ./Threads-of-Fate.tex
cd output
for name in `ls *.idx`; do
 makeindex $name
done
cd ..
pdflatex --enable-pipes --shell-escape -output-directory=output ./Threads-of-Fate.tex
pdflatex --enable-pipes --shell-escape -output-directory=output ./Threads-of-Fate.tex
