# -*- coding: UTF-8 -*-
#清理不必要的文件
Mdb()
#os.system('del /q *.log *.msg *.sta *.sim *.ipm *.jnl *.com *.dat *.prt *.dmp *.lck *.rec *.SMABulk *.rpy.* *.times')

StrFile=JobName+".*"
File_List=glob.glob(StrFile)+glob.glob("*rpy.*")+glob.glob("*.rec")+glob.glob("*.rpt")
File_List=set(File_List)-set(glob.glob("*odb")) -set(glob.glob("*cae"))#排除cae和odb文件

for file in File_List:
  if os.path.isdir(file):
    shutil.rmtree(file)
  else:
    os.remove(file)
#EndFor