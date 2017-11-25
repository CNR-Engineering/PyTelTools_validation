#!/bin/sh

# Copy different Serafin files without changing precision or endianness
slf_base.py ref/r2d_bowl_vf_gb_DoublePrecision_BigEndian.slf out/r2d_bowl_vf_gb_DoublePrecision_BigEndian.slf
slf_base.py ref/r2d_bowl_vf_gb_DoublePrecision_LittleEndian.slf out/r2d_bowl_vf_gb_DoublePrecision_LittleEndian.slf
slf_base.py ref/r2d_bowl_vf_gb_SinglePrecision_BigEndian.slf out/r2d_bowl_vf_gb_SinglePrecision_BigEndian.slf
slf_base.py ref/r2d_bowl_vf_gb_SinglePrecision_LittleEndian.slf out/r2d_bowl_vf_gb_SinglePrecision_LittleEndian.slf

# Change temporal window and select some 2D variables
slf_base.py ../data/Yen/fis_yen-exp.slf out/fis_yen-exp_new.slf --lang en --var2add C M Q F --var2del H 'C 1ST CLASS' 'PRIVE 1' 'PRIVE 2' --start 3600 --ech 2

# Resample a 3D results file, compute velocity magnitude and apply a mesh translation
slf_base.py ../data/pildepon/f3d_piledepon.slf out/f3d_piledepon_new.slf --ech 4 --var2add M --shift 14 10 --lang en
