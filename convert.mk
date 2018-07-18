SRC=$(wildcard ./tex/*.tex)
DST=$(patsubst ./tex/%.tex,./en/%.md,${SRC})
PRE=./bin/tex2md.py

all : ${DST}

./en/%.md : ./tex/%.tex ${PRE}
	@${PRE} < $< > $@

settings:
	@echo 'SRC' ${SRC}
	@echo 'DST' ${DST}
