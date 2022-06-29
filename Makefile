#!/usr/bin/make -f

.PHONY: all

help:  ## Usage information
	@LC_ALL=C $(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | \
		awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | \
		sort | \
		egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

push:	## Push to public repo
	python3 ./generate-meta-packages -p

all: push	## Default target


clean:	## cleanup work directory
	rm -f *.upload
	rm -f *.changes
	rm -f *.build
	rm -rf __pycache__
	rm -f *~
	rm -f *.pyc *.pyo
	rm -f *.deb
	rm -f *.dsc
	rm -f *~*.tar.xz
	rm -f *.buildinfo

