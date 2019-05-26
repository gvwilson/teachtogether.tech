# Commands
LATEX=pdflatex --shell-escape
BIBTEX=biber
PANDOC=pandoc -s --css=bootstrap.min.css --css=book.css --toc --toc-depth=1

# File(s)
TEX=$(wildcard *.tex)
SRC=${TEX} $(wildcard *.bib) $(wildcard *.cls)
HTML=book.html
PDF=book.pdf

# Controls
all : commands

## commands       : show all commands.
commands :
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g'

## html           : generate HTML from LaTeX source.
html : ${HTML}

## pdf            : generate PDF from LaTeX source.
pdf : ${PDF}

## once           : force a single run of LaTeX.
once :
	${LATEX} book

# ----------------------------------------

# Regenerate PDF once 'all.tex' has been created.
${PDF} : ${SRC}
	${LATEX} book \
	&& ${BIBTEX} book \
	&& ${LATEX} book \
	&& ${LATEX} book \
	&& ${LATEX} book

# Generate HTML
${HTML} : ${SRC} template.html
	sed -e 's/input{settings}/input{html}/g' book.tex > temp.tex
	${PANDOC} --template=template.html --bibliography=book.bib -o book.html temp.tex
	rm temp.tex

## ----------------------------------------

## check          : check internal consistency.
check :
	@python bin/check.py ${TEX}

## remaining      : count work to be done.
remaining :
	@wc -w $$(fgrep chaplbl ${TEX} | fgrep FIXME | cut -d ':' -f 1) | sort -n -r

## clean          : clean up junk files.
clean :
	@rm -f book.pdf
	@rm -f *.4ct *.4tc *.aux *.bak *.bbl *.bcf *.blg *.dvi *.idx *.lof *.log *.lot *.out *.run.xml *.tmp *.toc *.xref
	@find . -name '*~' -delete
	@find . -name '_minted-*' -prune -exec rm -r "{}" \;
	@find . -name .DS_Store -prune -exec rm -r "{}" \;
