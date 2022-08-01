# -*- coding: UTF-8 -*-
#当前文件夹
cur_dir=os.getcwd()
FilePython0=cur_dir+ "/" +"0Heads.py"#头文件
#头文件
execfile(FilePython0,)

#Static分析步
JobName=FileStatic #Job名
FileOdb=FileOdbStatic
FileCae=FileCaeStatic

#读取cae文件
openMdb(pathName=FileCae)

#读取文本文件，存入矩阵
data = np.loadtxt(FileInputStatic, delimiter=' ', dtype=float, skiprows=1)

for i in range(len(data[:,1])):
  rho=data[i][0]#密度kg/m^3
  E  =data[i][1]#弹模GPa
  rpm=data[i][2]#转速r/min
  



#修改static分析步
execfile(FilePython4,)

#创建Job
execfile(FilePython5,)

##保存cae文件
mdb.saveAs(pathName=FileCae)

##提交Job
execfile(FilePython6,)

##后处理
execfile(FilePython7,)

##清除不必要的文件
execfile(FilePython9,)