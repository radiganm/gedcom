#!/usr/bin/make -sf
### makefile (for gedcom)
###
### Copyright 2017 Mac Radigan
### All Rights Reserved

.PHONY: init clean clobber run test
.DEFAULT_GOAL := all

BLDDIR=./build

target = gedcom

all: init build

CCC = g++
CYC = cython3
PYC = python3

APPDIR=./library/$(target)
BINDIR=bin

CYSRC = \
  library/$(target)/GedcomParser.py

CYAPPS = \
  $(target).py
CYBINS = $(patsubst %,$(BINDIR)/%, $(CYAPPS:.py=))

build: $(CYBINS)

$(BINDIR)/$(target): $(target).py lib$(target).a
	$(CYC) -a library/gedcom/GedcomParser.py
	$(CYC) --embed -a $(target).py
	#$(CCC) -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -I/usr/include/python3.5 -o $(BINDIR)/$(target) $(target).c
	$(CCC) -o $@ $(target).c ./library/gedcom/GedcomParser.c -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -I/usr/include/python3.5 -L/usr/lib/x86_64-linux-gnu -lpython3.5m -L. -l$(target)

libedcom.a: $(CYSRC)
	$(PYC) setup2.py

#$(BINDIR)/$(target): $(target).py
	#$(PYC) setup.py build_ext --inplace

init:
	-mkdir -p $(BINDIR)

clobber: clean
	-rm -f $(CYBINS)
	-rm -f *.so

clean:

run:
	env LD_LIBRARY_PATH=. $(BINDIR)/$(target) -f ./data/KennedyFamily.ged

test:
	$(MAKE) -C ./tests

## *EOF*
