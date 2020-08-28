set PYTHON=\\cnr\dfs\Telemac\_OUTILS\WinPython64-3.7.2\python-3.7.2.amd64\python.exe
set PYTHONPATH=\\cnr\dfs\Telemac\_OUTILS\scripts\ADCPtool;\\cnr\dfs\Telemac\_OUTILS\TELEMAC\scripts\PyTelTools;

%PYTHON% T:\_OUTILS\TELEMAC\scripts\PyTelTools\cli\plot_comp_ADCP_t2d.py out\Res_ADCP.csv out\Res_T2D.csv out\Comp_Donzere.png

pause
