LATEX=pdflatex --shell-escape
BIBTEX=biber

TEX=$(wildcard *.tex)
SRC=${TEX} $(wildcard *.bib) $(wildcard *.cls)
DST=book.pdf

# Controls
all : commands

## commands       : show all commands.
commands :
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g'

## pdf            : generate PDF from LaTeX source.
pdf : ${DST}

## once           : force a single run of LaTeX.
once :
	${LATEX} book

# ----------------------------------------

# Regenerate PDF once 'all.tex' has been created.
${DST} : ${SRC}
	${LATEX} book \
	&& ${BIBTEX} book \
	&& ${LATEX} book \
	&& ${LATEX} book \
	&& ${LATEX} book

## ----------------------------------------

## check          : check internal consistency.
check :
	@python bin/check.py ${TEX}

## remaining      : count work to be done.
remaining :
	@wc -w $$(fgrep FIXME book.tex | sed -e 's/\\input{//g' | sed -e 's/} % FIXME/.tex/g') | sort -n -r

## clean          : clean up junk files.
clean :
	@rm -f book.pdf
	@rm -r -f *.aux *.bak *.bbl *.bcf *.blg *.idx *.lof *.log *.lot *.out *.run.xml *.toc
	@find . -name '*~' -delete
	@find . -name '_minted-*' -prune -exec rm -r "{}" \;
	@find . -name .DS_Store -prune -exec rm -r "{}" \;
