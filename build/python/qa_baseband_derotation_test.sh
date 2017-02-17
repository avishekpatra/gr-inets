#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/inets/source/gr-inets/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/inets/source/gr-inets/build/python:$PATH
export LD_LIBRARY_PATH=/home/inets/source/gr-inets/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/inets/source/gr-inets/build/swig:$PYTHONPATH
/usr/bin/python2 /home/inets/source/gr-inets/python/qa_baseband_derotation.py 
