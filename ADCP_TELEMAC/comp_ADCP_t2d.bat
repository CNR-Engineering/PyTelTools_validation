set PYTHON=\\cnr\dfs\Telemac\_OUTILS\WinPython64-3.7.2\python-3.7.2.amd64\python.exe
set PYTHONPATH=\\cnr\dfs\Telemac\_OUTILS\scripts\ADCPtool;\\cnr\dfs\Telemac\_OUTILS\TELEMAC\scripts\PyTelTools;

%PYTHON% T:\_OUTILS\TELEMAC\scripts\PyTelTools\cli\comp_ADCP_t2d.py in\PROFILS_ANT_BGE_DM260112SF6W2_0_000_gps_ASC.TXT in\PROFILS_ANT_BGE_DM260112SF6W2_0_000_ASC.TXT out\Trace_ADCP.shp out\Res_ADCP.csv out\Res_T2D.csv --inTELEMAC in\C3_2D_calageVitesse2012_P1\r2d_last.slf in\C3_2D_calageVitesse2012_P1_mixte_SL_d90\r2d_last.slf in\C4_3D_calageVitesse2012_P1_mixte_SL_d90\r2d_last.slf --shift +830000 +6360000

pause
