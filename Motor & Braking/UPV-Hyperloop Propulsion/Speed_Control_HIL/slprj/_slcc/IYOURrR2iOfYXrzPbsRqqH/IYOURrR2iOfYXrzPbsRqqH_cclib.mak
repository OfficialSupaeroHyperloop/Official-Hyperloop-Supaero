#------------------------ Tool Specifications & Options ----------------------

COMPILER  =  lcc

CC        =  "C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\bin\lcc64.exe"
LD        =  "C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\bin\lcclnk64.exe"
LIBCMD    =  "C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\bin\lcclib64.exe"
CFLAGS    =  -dll -noregistrylookup  -c -Zp8 -DLCC_WIN64 -DMATLAB_MEX_FILE -nodeclspec
LDFLAGS   =  -s -dll -entry LibMain IYOURrR2iOfYXrzPbsRqqH_cclib.def -L"C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\lib64"

OBJECTS = \
	   slcc_instrum1_IYOURrR2iOfYXrzPbsRqqH_cclib.obj \
	   slcc_instrum2_IYOURrR2iOfYXrzPbsRqqH_cclib.obj \
	   slcc_interface_IYOURrR2iOfYXrzPbsRqqH.obj \
	   slcc_instrumtr_IYOURrR2iOfYXrzPbsRqqH_cclib.obj \
	   lccstub.obj \

STATICLIBS = \
	   "C:\Program Files\MATLAB\R2022b\extern\lib\win64\microsoft\libmwsl_sfcn_cov_bridge.lib" \

#------------------------------ Include/Lib Path ------------------------------

INCLUDE_PATH = \
     -I"c:\program files\matlab\r2022b\extern\include" \
     -I"c:\program files\matlab\r2022b\simulink\include" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_hil\slprj\_slcc\iyourrr2iofyxrzpbsrqqh" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_hil\c code\prueba_controlador_sandbox\include" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_hil" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_hil\c code" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_hil\c code\prueba_controlador_sandbox\src" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_hil\c code\prueba_controlador_sandbox\manualstub" \
     -I"c:\program files\matlab\r2022b\sys\lcc64\lcc64\include64" \
     -I"c:\program files\matlab\r2022b\sys\lcc64\lcc64\mex" \

#--------------------------------- Rules --------------------------------------

IYOURrR2iOfYXrzPbsRqqH_cclib.dll : $(MAKEFILE) $(OBJECTS)
	$(LD) $(LDFLAGS) /OUT:IYOURrR2iOfYXrzPbsRqqH_cclib.dll $(OBJECTS)  $(STATICLIBS) "C:\Program Files\MATLAB\R2022b\extern\lib\win64\microsoft\libmex.lib" "C:\Program Files\MATLAB\R2022b\extern\lib\win64\microsoft\libmx.lib"
slcc_instrum1_IYOURrR2iOfYXrzPbsRqqH_cclib.obj :	C:\Users\mique\ICLOUD~1\HYPERL~1\SPEED_~4\slprj\_slcc\IYOURR~1\SLCC_I~1.C
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Users\mique\iCloudDrive\Hyperloop Upv\Speed_Control_HIL\slprj\_slcc\IYOURrR2iOfYXrzPbsRqqH\slcc_instrum1_IYOURrR2iOfYXrzPbsRqqH_cclib.c"
slcc_instrum2_IYOURrR2iOfYXrzPbsRqqH_cclib.obj :	C:\Users\mique\ICLOUD~1\HYPERL~1\SPEED_~4\slprj\_slcc\IYOURR~1\SLCC_I~2.C
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Users\mique\iCloudDrive\Hyperloop Upv\Speed_Control_HIL\slprj\_slcc\IYOURrR2iOfYXrzPbsRqqH\slcc_instrum2_IYOURrR2iOfYXrzPbsRqqH_cclib.c"
slcc_interface_IYOURrR2iOfYXrzPbsRqqH.obj :	C:\Users\mique\ICLOUD~1\HYPERL~1\SPEED_~4\slprj\_slcc\IYOURR~1\SLCC_I~4.C
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Users\mique\iCloudDrive\Hyperloop Upv\Speed_Control_HIL\slprj\_slcc\IYOURrR2iOfYXrzPbsRqqH\slcc_interface_IYOURrR2iOfYXrzPbsRqqH.c"
slcc_instrumtr_IYOURrR2iOfYXrzPbsRqqH_cclib.obj :	C:\Users\mique\ICLOUD~1\HYPERL~1\SPEED_~4\slprj\_slcc\IYOURR~1\SLCC_I~3.C
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Users\mique\iCloudDrive\Hyperloop Upv\Speed_Control_HIL\slprj\_slcc\IYOURrR2iOfYXrzPbsRqqH\slcc_instrumtr_IYOURrR2iOfYXrzPbsRqqH_cclib.c"
lccstub.obj :	C:\PROGRA~1\MATLAB\R2022b\sys\lcc64\lcc64\mex\lccstub.c
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\mex\lccstub.c"