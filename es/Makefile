TEX=$(wildcard *.tex) $(wildcard *.bib)

## book.pdf : Re-make PDF.
book.pdf : ${TEX}
	pdflatex --shell-escape book
	biber book
	makeindex book
	pdflatex --shell-escape book
	pdflatex --shell-escape book
	pdflatex --shell-escape book

## clean : Clean things up.
clean :
	@rm -f book.pdf
	@rm -f *.aux *.bak *.bbl *.blg *.dvi *.idx *.ilg *.ind *.lof *.log *.lot *.out *.pyg *.run.xml *.tmp *.toc *.xref
	@find . -name '*~' -delete
	@find . -name '_minted-*' -prune -exec rm -r "{}" \;
