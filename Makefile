# Settings
JEKYLL=jekyll
D_DST=_site
MD_SRC=$(wildcard _lessons/*.md) $(wildcard _extras/*.md)

# Controls
.PHONY : commands serve site bib crossref clean
all : commands

## commands : show all commands.
commands :
	@grep -h -E '^##' Makefile | sed -e 's/## //g'

## serve    : run a local server.
serve :
	${JEKYLL} serve -I

## site     : build files but do not run a server.
site :
	${JEKYLL} build

## bib      : rebuild Markdown bibliography from BibTeX source.
bib : ./_extras/bib.md
./_extras/bib.md : ./bin/bib2md.py ./files/t3.bib
	./bin/bib2md.py < ./files/t3.bib > ./_extras/bib.md

## crossref : rebuild cross-reference file.
crossref : ./files/crossref.js
./files/crossref.js : ./bin/crossref.py ./_config.yml ${MD_SRC}
	./bin/crossref.py < ./_config.yml > ./files/crossref.js

## clean    : clean up junk files.
clean :
	@rm -rf ${D_DST}
	@find . -name .DS_Store -exec rm {} \;
	@find . -name '*~' -exec rm {} \;
