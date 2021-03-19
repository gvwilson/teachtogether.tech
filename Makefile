.PHONY : all clean commands html settings

# Files
TEX=$(wildcard en/*.tex) $(wildcard es/*.tex)
SRC=${TEX} $(wildcard en/*.bib) $(wildcard es/*.bib) $(wildcard *.cls) $(wildcard *.csl) $(wildcard */template.html)
HTML=docs/index.html docs/en/index.html docs/es/index.html
STATIC_SRC=$(wildcard static/*)
STATIC_DST=$(patsubst %,docs/%,${STATIC_SRC})

# Controls
all : commands

## commands : show all commands.
commands :
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' | column -t -s ':'

## pdf : generate PDF for all versions.
pdf :
	@make -C en pdf
	@make -C es pdf

## html : generate HTML from LaTeX source.
html :
	@make -C en html
	@make -C es html

# Copy static.
docs/static/% : static/%
	@mkdir -p docs/static
	@cp $< $@

# Copy CNAME file.
docs/CNAME : ./CNAME
	@mkdir -p docs
	@cp $< $@

## clean : clean up junk files.
clean :
	@find . -name '*~' -delete
	@find . -name '_minted-*' -prune -exec rm -r "{}" \;
	@find . -name .DS_Store -prune -exec rm -r "{}" \;
	@make -C en clean
	@make -C es clean
	@make -C kr clean

## settings : show settings.
settings :
	@echo TEX ${TEX}
	@echo SRC ${SRC}
	@echo HTML ${HTML}
