# Projet settings.
include project.mk

# Working directories.
BIN_D=./bin
TEX_D=./tex
DOCS_D=./docs
WEB_D=./_site

# Filesets.
BIB_SRC=${TEX_D}/bib.bib
TEX_SRC=$(wildcard ${TEX_D}/*.tex) ${BIB_SRC}
TEX_DST=$(patsubst %,${TEX_D}/${STEM}.%,aux bbl pdf toc)
DOCS_IGNORES=$(patsubst %,${TEX_D}/%,${STEM}.tex frontmatter.tex macros.tex settings.tex) ${BIB_SRC}
DOCS_SRC=$(filter-out ${DOCS_IGNORES},${TEX_SRC})
DOCS_DST=$(patsubst ${TEX_D}/%.tex,${DOCS_D}/%.html,${DOCS_SRC}) ${DOCS_D}/bib.html ${DOCS_D}/${STEM}.bib
DOCS_ALL=${DOCS_D}/${STEM}.html ${DOCS_D}/${STEM}.epub ${DOCS_D}/${STEM}.mobi ${DOCS_D}/${STEM}.pdf

# Tools.
LATEX=pdflatex
BIBTEX=bibtex
PANDOC=pandoc
PANDOC_FLAGS=--template=html.pandoc --from=latex --to=html

# Phony targets.
.PHONY: all commands pdf web serve

# default target
all : commands

## commands   : show all commands.
commands :
	@grep -E '^##' Makefile | sed -e 's/## //g'

## pdf        : build PDF versions of book.
pdf : ${TEX_D}/${STEM}.pdf

${TEX_DST} : ${TEX_SRC}
	@cd ${TEX_D} \
	&& ${LATEX} ${STEM} \
	&& ${BIBTEX} ${STEM} \
	&& ${LATEX} ${STEM} \
	&& ${LATEX} ${STEM} \
	&& ${LATEX} ${STEM}

## web        : make web-ready versions of book (HTML, EPUB, and MOBI).
web : ${DOCS_ALL}
	@jekyll build -s ${DOCS_D}

## serve      : serve HTML on port 4000.
serve : ${DOCS_ALL}
	@jekyll serve -s ${DOCS_D} -I

${DOCS_D}/%.html : ${TEX_D}/%.tex ${TEX_D}/${STEM}.aux ${BIN_D}/ltx2html-pre.py ${BIN_D}/ltx2html-post.py
	cat ${TEX_D}/macros.tex $< \
	| ${BIN_D}/ltx2html-pre.py ${TEX_D}/${STEM}.aux \
	| ${PANDOC} ${PANDOC_FLAGS} -o - --metadata title="$$(fgrep -e '\chapter' $< | head -n 1 | sed -e 's/\\chapter{//g' -e 's/}\\label.*//g')" \
	| ${BIN_D}/ltx2html-post.py \
	> $@

${DOCS_D}/bib.html : ${TEX_D}/${STEM}.bbl ${BIN_D}/bbl2html-pre.py ${BIN_D}/bbl2html-post.py
	${BIN_D}/bbl2html-pre.py $< \
	| ${PANDOC} ${PANDOC_FLAGS} -o - --metadata title="Bibliography" \
	| ${BIN_D}/bbl2html-post.py ${BIB_SRC} \
	> $@

${DOCS_D}/${STEM}.bib : ${BIB_SRC}
	@cp $< $@

${DOCS_D}/${STEM}.html : ${DOCS_DST} ${BIN_D}/mergebook.py
	${BIN_D}/mergebook.py ${TITLE} ${TEX_D}/${STEM}.tex ${DOCS_D} \
	> $@

${DOCS_D}/${STEM}.epub : ${DOCS_D}/${STEM}.html
	cat $< \
	| ${BIN_D}/unheader.py \
	| ${PANDOC} -o $@ --resource-path=${DOCS_D} --metadata title=${TITLE} --title=${TITLE}

${DOCS_D}/${STEM}.mobi : ${DOCS_D}/${STEM}.html
	cat $< \
	| ${BIN_D}/unheader.py \
	| ${PANDOC} -o $@ --resource-path=${DOCS_D} --metadata title=${TITLE} --title=${TITLE}

${DOCS_D}/${STEM}.pdf : ${TEX_D}/${STEM}.pdf
	cp $< $@

## ----------------------------------------

## exercises  : count exercises per chapter.
exercises :
	@${BIN_D}/exercises.py ${TEX_D}/${STEM}.tex

## fixme      : find and count things that need to be fixed.
fixme :
	@fgrep -e '\fixme' --exclude ${TEX_D}/macros.tex ${TEX_SRC}
	@echo 'small:' $$(fgrep -e '\fixme{small}' ${TEX_SRC} | wc -l)
	@echo 'medium:' $$(fgrep -e '\fixme{medium}' ${TEX_SRC} | wc -l)
	@echo 'large:' $$(fgrep -e '\fixme{large}' ${TEX_SRC} | wc -l)

## issues     : create single-page view of all GitHub issues.
issues :
	@${BIN_D}/issues.py ${REPO} | ${PANDOC} -o issues.html -

## labels     : make sure all labels conform to standards.
labels :
	@${BIN_D}/checklabels.py ${TEX_SRC}

## pages      : count pages per chapter.
pages : ${TEX_D}/${STEM}.toc
	@${BIN_D}/pages.py < ${TEX_D}/${STEM}.toc

## spelling   : check spelling.
spelling :
	@grep bibnote ${BIB_SRC} \
	| cat - ${DOCS_SRC} \
	| aspell --mode=tex list \
	| sort \
	| uniq \
	| comm -2 -3 - words.txt

## vocabulary : list all words used in all chapters.
vocabulary :
	@cd tex && detex -w ${STEM}.tex | sed -e "s:'s$$::g" | grep -v '<Picture' | sort | uniq -c | sort -n -r

## words      : count words per chapter.
words :
	@wc -w ${DOCS_SRC} | sort -n -r

## ----------------------------------------

## authors    : list all authors.
authors :
	@${BIN_D}/authors.py ${BIB_SRC}

## bibfiles   : check missing or unused papers - requires DIR=/some/path as command-line argument.
bibfiles :
	@${BIN_D}/bibfiles.py ${DIR} ${BIB_SRC}

## classify   : classify bibliography entry types.
classify :
	@${BIN_D}/classify.py ${BIB_SRC}

## missing    : list all missing bibliography entries.
missing :
	@${BIN_D}/checkcites.py --missing ${BIB_SRC} ${TEX_SRC}

## publishers : list all publishers.
publishers :
	@${BIN_D}/fields.py ${BIB_SRC} publisher

## titlelen   : list entry titles by length.
titlelen :
	@${BIN_D}/titlelen.py ${BIB_SRC}

## undone     : find bibliography entries that don't yet have notes.
undone :
	@${BIN_D}/undone.py ${BIB_SRC}

## unused     : list all unused bibliography entries.
unused :
	@${BIN_D}/checkcites.py --unused ${BIB_SRC} ${TEX_SRC}

## venues     : list all publication venues.
venues :
	@${BIN_D}/fields.py ${BIB_SRC} booktitle
	@${BIN_D}/fields.py ${BIB_SRC} journal

## yearlabels : make sure bibliography labels and years line up.
yearlabels :
	@${BIN_D}/yearlabels.py ${BIB_SRC}

## years      : CSV histogram of publication years.
years :
	@${BIN_D}/years.py ${BIB_SRC}

## ----------------------------------------

## mismatch   : identify leftover HTML files.
mismatch :
	@${BIN_D}/mismatch.py ${STEM} ${DOCS_D} ${DOCS_DST}

## clean      : clean up junk files.
clean :
	@rm -rf _site
	@rm -f tex/${STEM}.pdf
	@find . -name '*.aux' -exec rm {} \;
	@find . -name '*.bbl' -exec rm {} \;
	@find . -name '*.blg' -exec rm {} \;
	@find . -name '*.log' -exec rm {} \;
	@find . -name '*.out' -exec rm {} \;
	@find . -name '*.toc' -exec rm {} \;
	@find . -name '*~' -exec rm {} \;
	@find . -name .DS_Store -exec rm {} \;

## nonascii   : look for non-ASCII characters.
nonascii :
	@${BIN_D}/nonascii.py ${TEX_SRC}

## settings   : show values of variables.
settings :
	@echo 'STEM "'${STEM}'"'
	@echo 'REPO "'${REPO}'"'
	@echo 'LATEX "'${LATEX}'"'
	@echo 'BIBTEX "'${BIBTEX}'"'
	@echo 'PANDOC "'${PANDOC}'"'
	@echo 'PANDOC_FLAGS "'${PANDOC_FLAGS}'"'
	@echo 'TEX_D "'${TEX_D}'"'
	@echo 'DOCS_D "'${DOCS_D}'"'
	@echo 'WEB_D "'${WEB_D}'"'
	@echo 'TEX_SRC "'${TEX_SRC}'"'
	@echo 'TEX_DST "'${TEX_DST}'"'
	@echo 'DOCS_IGNORES "'${DOCS_IGNORES}'"'
	@echo 'DOCS_SRC "'${DOCS_SRC}'"'
	@echo 'DOCS_DST "'${DOCS_DST}'"'
	@echo 'DOCS_ALL "'${DOCS_ALL}'"'
