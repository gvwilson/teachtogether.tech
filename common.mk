ifndef LANGUAGE
$(error LANGUAGE is not defined)
endif

.PHONY : all check clean commands html pages pdf spell words

# Settings
OUTPUT=../docs/${LANGUAGE}
TEX=$(filter-out temp.tex,$(wildcard *.tex))
BIB=$(wildcard *.bib)
FIGURES_SRC=$(wildcard figures/*)
FIGURES_DST=$(patsubst %,${OUTPUT}/%,${FIGURES_SRC})

# Commands.
LATEX=pdflatex --shell-escape --recorder
PANDOC=pandoc \
  --standalone \
  --css=../static/bootstrap.min.css \
  --css=../static/tango.css \
  --css=../static/book.css \
  --toc \
  --toc-depth=2 \
  --csl=../tex/chicago.csl

# Controls
all : commands

## commands : show all commands.
commands :
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' | column -t -s ':'

## html : re-make HTML.
html: tex.html bib.html ../bin/post-pandoc.py
	@mkdir -p ${OUTPUT}
	../bin/post-pandoc.py tex.html bib.html > ${OUTPUT}/index.html

tex.html: temp.tex template.html
	${PANDOC} --template=template.html --bibliography=book.bib --output=tex.html temp.tex

bib.html: book.bib ../bin/bib2html.py
	../bin/bib2html.py < book.bib > bib.html

temp.tex: ${TEX} ${FIGURES_DST} ../bin/pre-pandoc.py
	../bin/pre-pandoc.py < book.tex > temp.tex

## pdf : Re-make PDF.
pdf : ${TEX} ${BIB}
	${LATEX} book
	biber book
	makeindex book
	${LATEX} book
	${LATEX} book
	${LATEX} book

# Copy figures.
${OUTPUT}/figures/% : figures/%
	@mkdir -p ${OUTPUT}/figures
	@cp $< $@

## check : check internal consistency.
check :
	@../bin/check.py -b book.bib -f figures ${TEX}

## spell : check spelling.
spell :
	@-cat ${TEX} | aspell -t list | sort | uniq | diff -y --suppress-common-lines - wordlist.txt

## pages : pages per chapter.
pages : ${PDF}
	@../bin/pages.py book.log book.toc

## words : count words.
words :
	@../bin/texcount.pl -brief ${TEX} | sed -e 's/\+.*://g' -e 's/+.* Total//g' | sort -n -r

## clean : Clean things up.
clean :
	@rm -f book.pdf
	@rm -f *.aux *.bak *.bbl *.bcf *.blg *.dvi *.fls *.idx *.ilg *.ind *.lof *.log *.lot *.out *.pyg *.run.xml *.tmp *.toc *.xref
	@rm -f tex.html bib.html temp.tex
	@find . -name '*~' -delete
	@find . -name '_minted-*' -prune -exec rm -r "{}" \;
