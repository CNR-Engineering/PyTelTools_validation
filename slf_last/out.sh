#!/bin/sh

# Basic 2D example
slf_last.py ../data/Yen/fis_yen-exp.slf out/fis_yen-exp_last.slf

# 3D example with output time sets to 0s
slf_last.py ../data/pildepon/f3d_piledepon.slf out/f3d_piledepon_last.slf --time 0 --lang en
