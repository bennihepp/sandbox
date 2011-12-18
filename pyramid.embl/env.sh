#!/bin/bash

PackDir="/g/software/linux/pack/python-2.7"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$PackDir/lib:/g/software/linux/pack/libboostpython-1.46.1/lib:/g/software/linux/pack/vigra-1.7.1/lib:/g/software/linux/pack/tiff-3.8.1/lib:/g/software/linux/pack/libjpeg-8/lib:/g/software/linux/pack/libpng-1.4.5/lib:/g/software/linux/pack/fftw-3.2.2/lib:/g/software/linux/pack/hdf5-1.8.4/lib:/g/software/linux/pack/szlib-2.1/lib"
export PYTHONPATH="$PYTHONPATH:/g/software/linux/pack/cellcognition-1.2.4/SRC/cecog_git/pysrc"

