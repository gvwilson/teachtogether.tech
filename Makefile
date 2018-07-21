# Tools.
JEKYLL=jekyll
LATEX=pdflatex
BIBTEX=bibtex
PANDOC=pandoc
PANDOC_FLAGS=--from=gfm --to=latex

# Settings.
LESSONS_MD=$(wildcard _lessons_en/*.md)
EXTRAS_MD=$(filter-out _extras_en/bib.md,$(wildcard _extras_en/*.md))
ALL_MD=${LESSONS_MD} ${EXTRAS_MD}
LESSONS_TEX=$(patsubst _lessons_en/%.md,tex_en/lessons/%.tex,${LESSONS_MD})
EXTRAS_TEX=$(patsubst _extras_en/%.md,tex_en/extras/%.tex,${EXTRAS_MD})

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

## pdf      : build PDF version of book.
pdf : tex_en/t3.pdf

## tex      : generate LaTeX for book, but don't compile to PDF.
tex : ${LESSONS_TEX} ${EXTRAS_TEX}

tex_en/t3.pdf : ${LESSONS_TEX} ${EXTRAS_TEX} tex_en/t3.bib
	@cd tex_en \
	&& ${LATEX} t3 \
	&& ${BIBTEX} t3 \
	&& ${LATEX} t3 \
	&& ${LATEX} t3 \
	&& ${LATEX} t3

tex_en/lessons/%.tex : _lessons_en/%.md bin/texpre.py bin/texpost.py _includes/links.md
	mkdir -p tex_en/lessons && \
	cat $< \
	| bin/texpre.py \
	| ${PANDOC} ${PANDOC_FLAGS} -o - \
	| bin/texpost.py _includes/links.md \
	> $@

tex_en/extras/%.tex : _extras_en/%.md bin/texpre.py bin/texpost.py _includes/links.md
	mkdir -p tex_en/extras && \
	cat $< \
	| bin/texpre.py \
	| ${PANDOC} ${PANDOC_FLAGS} -o - \
	| bin/texpost.py _includes/links.md \
	> $@

tex_en/t3.bib : files/t3.bib
	cp $< $@

## bib      : rebuild Markdown bibliography from BibTeX source.
bib : _extras_en/bib.md
_extras_en/bib.md : bin/bib2md.py files/t3.bib
	bin/bib2md.py < files/t3.bib > _extras_en/bib.md

## crossref : rebuild cross-reference file.
crossref : files/crossref.js
files/crossref.js : bin/crossref.py _config.yml ${ALL_MD}
	bin/crossref.py < _config.yml > files/crossref.js

## clean    : clean up junk files.
clean :
	@rm -rf _site tex_en/lessons/* tex_en/extras/*
	@find . -name .DS_Store -exec rm {} \;
	@find . -name '*~' -exec rm {} \;
	@find . -name '*.aux' -exec rm {} \;
	@find . -name '*.bbl' -exec rm {} \;
	@find . -name '*.blg' -exec rm {} \;
	@find . -name '*.log' -exec rm {} \;
	@find . -name '*.out' -exec rm {} \;
	@find . -name '*.toc' -exec rm {} \;
