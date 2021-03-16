.PHONY : all check clean commands html pages pdf spell words

# Language
LANGUAGE=es

# Settings
OUTPUT=../docs/${LANGUAGE}
TEX=$(wildcard *.tex)
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
html: temp.html
	@mkdir -p ${OUTPUT}
	cat temp.html | ../bin/post-pandoc.py > ${OUTPUT}/index.html

temp.html: ${FIGURES_DST} ../bin/pre-pandoc.py ../bin/post-pandoc.py template.html
	../bin/pre-pandoc.py < book.tex > temp.tex
	${PANDOC} --template=template.html --bibliography=book.bib --output=temp.html temp.tex

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
	@find . -name '*~' -delete
	@find . -name '_minted-*' -prune -exec rm -r "{}" \;
