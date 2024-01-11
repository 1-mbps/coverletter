#!/bin/bash

pdflatex -jobname="${1}_cover_letter" -output-directory="cover_letters/$1" cover_letters/$1/main.tex
