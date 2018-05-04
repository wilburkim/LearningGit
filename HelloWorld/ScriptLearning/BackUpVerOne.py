#coding=utf-8
import os
import time
import zipfile

#source=['..\\..\\SourceDir\\Dir1','..\\..\\SourceDir\\Dir2']
#targer_dir='..\\..\\TargerDir'
#source=['K:\\Win7专用分区\\PythonProjects\\HelloWorld\\SourceDir\\Dir1','K:\\Win7专用分区\\PythonProjects\\HelloWorld\\SourceDir\\Dir2']
source='K:\\Win7专用分区\\PythonProjects\\HelloWorld\\SourceDir\\Dir1\\'
targer_dir='K:\\Win7专用分区\\PythonProjects\\HelloWorld\\TargerDir\\'
target=targer_dir+time.strftime("%Y%m%d%H%M%S")+".rar"

print(target)

#zipcommand = "rar a %s %s"%(target,source)

zipcommand=r"'E:\安装软件\WinRAR\WinRAR.exe' rar a %s %s"%(target, source)
print(zipcommand)
if os.system(zipcommand) == 0:
    print("Sucessfully");
else:
    print("backup failed")