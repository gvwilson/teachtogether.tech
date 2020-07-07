TEX=$(wildcard *.tex)
BIB=$(wildcard *.bib)

# Controls
all : commands

## commands : show all commands.
commands :
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' | column -t -s ':'

## pdf : Re-make PDF.
pdf : ${TEX} ${BIB}
	xelatex --shell-escape book
	biber book
	makeindex book
	xelatex --shell-escape book
	xelatex --shell-escape book
	xelatex --shell-escape book

## pages : pages per chapter.
pages : ${PDF}
	@../bin/pages.py book.log book.toc

## words : count words.
words :
	@../bin/texcount.pl -brief ${TEX} | sed -e 's/\+.*://g' -e 's/+.* Total//g' | sort -n -r

## clean : Clean things up.
clean :
	@rm -f book.pdf
	@rm -f *.aux *.bak *.bbl *.bcf *.blg *.dvi *.idx *.ilg *.ind *.lof *.log *.lot *.out *.pyg *.run.xml *.tmp *.toc *.xref
	@find . -name '*~' -delete
	@find . -name '_minted-*' -prune -exec rm -r "{}" \;
