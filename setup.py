#!/usr/bin/env python3
### setup2.py (for gedcom)
###
### Copyright 2017 Mac Radigan
### All Rights Reserved

from distutils.extension import Extension
from Cython.Distutils import build_ext
from distutils.core import setup
from Cython.Build import cythonize

setup(
 #ext_modules = [
 #  Extension('gedcom', ['library/gedcom/GedcomParser.py']),
 #],
 #executable_filename = 'bin/gedcom',
 #scripts = cythonize("gedcom.py"),
  name = "gedcom",
  cmd_class = {'build_ext': build_ext},
  scripts = "gedcom.py",
  ext_modules = cythonize(["library/gedcom/*.py"])
)

### *EOF*
