IGNORES=frontmatter macros settings t3
SRC=$(filter-out $(patsubst %,./tex/%.tex,${IGNORES}),$(wildcard ./tex/*.tex))
DST=$(patsubst ./tex/%.tex,./en/%.md,${SRC})
PRE=./bin/tex2md.py
POST=./bin/mdtidy.py
PANDOC=pandoc
PANDOC_FLAGS=--template=html.pandoc --from=latex --to=gfm

all : ${DST}

./en/%.md : ./tex/%.tex ${PRE} convert.mk
	cat $< \
	| ${PRE} \
	| ${PANDOC} ${PANDOC_FLAGS} -o - --metadata title="$$(fgrep -e '\chapter' $< | head -n 1 | sed -e 's/\\chapter{//g' -e 's/}\\label.*//g')" \
	| ${POST} \
	> $@

settings:
	@echo 'IGNORES' ${IGNORES}
	@echo 'SRC' ${SRC}
	@echo 'DST' ${DST}
