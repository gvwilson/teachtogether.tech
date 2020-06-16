# Files.
TEX=$(wildcard *.tex)
BIB=$(wildcard *.bib)
HTML=../docs/index.html

# Commands.
PANDOC=pandoc \
  --standalone \
  --css=assets/bootstrap.min.css \
  --css=assets/tango.css \
  --css=assets/book.css \
  --toc \
  --toc-depth=2 \
  --csl=../chicago.csl

# Controls
all : commands

## commands : show all commands.
commands :
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' | column -t -s ':'

## pdf : re-make PDF.
pdf : ${TEX} ${BIB}
	pdflatex --shell-escape book
	biber book
	makeindex book
	pdflatex --shell-escape book
	pdflatex --shell-escape book
	pdflatex --shell-escape book

## html : re-make HTML.
html : ../bin/pre-pandoc.py ../bin/post-pandoc.py ../template.html
	@mkdir -p ../docs
	../bin/pre-pandoc.py < book.tex > temp.tex
	${PANDOC} --template=../template.html --bibliography=book.bib --output=- temp.tex \
	| ../bin/post-pandoc.py \
	> ${HTML}
	rm temp.tex

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
	@rm -f *.aux *.bak *.bbl *.bcf *.blg *.dvi *.idx *.ilg *.ind *.lof *.log *.lot *.out *.pyg *.run.xml *.tmp *.toc *.xref
	@find . -name '*~' -delete
	@find . -name '_minted-*' -prune -exec rm -r "{}" \;
