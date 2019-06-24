#!/usr/bin/env bash

pdflatex --shell-escape book
biber book
makeindex book
pdflatex --shell-escape book
pdflatex --shell-escape book
