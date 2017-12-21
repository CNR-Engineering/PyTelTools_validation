#!/bin/sh

slf_3d_to_2d.py ../data/pildepon/f3d_piledepon.slf out/f3d_piledepon_vertical_mean_withBH.slf --aggregation mean --vars B H --lang en

slf_3d_to_2d.py ../data/pildepon/f3d_piledepon.slf out/f3d_piledepon_vertical_mean.slf --aggregation mean --lang en

slf_3d_to_2d.py ../data/pildepon/f3d_piledepon.slf out/f3d_piledepon_vertical_max.slf --aggregation max --lang en

slf_3d_to_2d.py ../data/pildepon/f3d_piledepon.slf out/f3d_piledepon_top.slf --layer 6 --lang en

slf_3d_to_2d.py ../data/pildepon/f3d_piledepon.slf out/f3d_piledepon_bottom.slf --layer 1 --lang en
