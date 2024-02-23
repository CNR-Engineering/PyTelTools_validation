set PYTHON=C:\softs\WinPython-64bits-3.11.5.0\python-3.11.5.amd64\python.exe
set PYTELTOOLS=C:\PROJETS\python\PyTelTools
set PYTHONPATH=%PYTELTOOLS%

REM Copy different Serafin files without changing precision or endianness
%PYTHON% %PYTELTOOLS%/cli/slf_base.py ref/r2d_bowl_vf_gb_DoublePrecision_BigEndian.slf out/r2d_bowl_vf_gb_DoublePrecision_BigEndian.slf
%PYTHON% %PYTELTOOLS%/cli/slf_base.py ref/r2d_bowl_vf_gb_DoublePrecision_LittleEndian.slf out/r2d_bowl_vf_gb_DoublePrecision_LittleEndian.slf
%PYTHON% %PYTELTOOLS%/cli/slf_base.py ref/r2d_bowl_vf_gb_SinglePrecision_BigEndian.slf out/r2d_bowl_vf_gb_SinglePrecision_BigEndian.slf
%PYTHON% %PYTELTOOLS%/cli/slf_base.py ref/r2d_bowl_vf_gb_SinglePrecision_LittleEndian.slf out/r2d_bowl_vf_gb_SinglePrecision_LittleEndian.slf

REM Change temporal window and select some 2D variables
%PYTHON% %PYTELTOOLS%/cli/slf_base.py ../data/Yen/fis_yen-exp.slf out/fis_yen-exp_new.slf --lang en --var2add C M Q F --var2del H 'C 1ST CLASS' 'PRIVE 1' 'PRIVE 2' --start 3600 --ech 2

REM Resample a 3D results file, compute velocity magnitude and apply a mesh translation
%PYTHON% %PYTELTOOLS%/cli/slf_base.py ../data/pildepon/f3d_piledepon.slf out/f3d_piledepon_new.slf --ech 4 --var2add M --shift 14 10 --lang en

REM Mesh transformation : local Lambert 93 => CC45
%PYTHON% %PYTELTOOLS%/cli/slf_base.py in/mesh_L93.slf out/mesh_CC45.slf --shift 960000 6550000 --epsg_mesh_transformation 2154 3945
