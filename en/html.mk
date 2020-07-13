# Settings
HTML=../docs/index.html

# Commands.
PANDOC=pandoc \
  --standalone \
  --css=static/bootstrap.min.css \
  --css=static/tango.css \
  --css=static/book.css \
  --toc \
  --toc-depth=2 \
  --csl=../tex/chicago.csl

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
