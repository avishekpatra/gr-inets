#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/inets/source/gr-inets/lib
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/inets/source/gr-inets/build/lib:$PATH
export LD_LIBRARY_PATH=/home/inets/source/gr-inets/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-inets 
