LATEX=pdflatex --shell-escape
BIBTEX=bibtex

SRC=$(wildcard *.tex)
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

## clean          : clean up junk files.
clean :
	@rm -f book.pdf
	@rm -r -f *.aux *.bbl *.blg *.idx *.lof *.log *.lot *.out *.toc
	@find . -name '*~' -delete
	@find . -name '_minted-*' -prune -exec rm -r "{}" \;
	@find . -name .DS_Store -prune -exec rm -r "{}" \;
