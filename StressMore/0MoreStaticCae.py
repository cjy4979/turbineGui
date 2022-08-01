# -*- coding: UTF-8 -*-
#当前文件夹
cur_dir=os.getcwd()
FilePython0=cur_dir+ "\\" +"0Heads.py"#头文件
#头文件
execfile(FilePython0,)

#Static分析步
JobName=FileStatic #Job名
FileOdb=FileOdbStatic
FileCae=FileCaeStatic


StrPrint=ToChinese("\n 批量计算随机分布的单只叶片应力(循环周期对称)...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print StrPrint

#清除不必要的文件
StrPrint=ToChinese("\n 清理不必要的文件...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print StrPrint
execfile(FilePython5,)

#读取cae文件
StrPrint=ToChinese("\n 读取cae文件...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print StrPrint
openMdb(pathName=FileCae)
#读取文本文件，存入矩阵
StrPrint=ToChinese("\n 读取随机分布的参数...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print StrPrint
data = np.loadtxt(FileInputStatic, delimiter=' ',dtype=float, skiprows=1,comments='#',encoding='utf-8-sig')

StrPrint="\n 共计算" + '%d'%(len(data[:,0])) + "组。\n"
StrPrint=ToChinese(StrPrint)
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print StrPrint

for ii in range(len(data[:,0])):
  str_ii='%03d'%(ii+1) #数字转字符串
  rho=data[ii][0]  #密度kg/m^3
  E  =data[ii][1]  #弹模GPa
  rpm=data[ii][2]  #转速r/min
  
  #修改static分析步
  StrPrint="\n 第" + str_ii + "组:\n\t 读取随机参数并赋值\n"
  StrPrint=ToChinese(StrPrint)
  print >> sys.__stdout__, StrPrint
  sys.__stdout__.flush()
  print StrPrint
  execfile(FilePython1,)

  #创建Job
  StrPrint=ToChinese("\t 创建计算任务...\n")
  print >> sys.__stdout__, StrPrint
  sys.__stdout__.flush()
  print StrPrint
  execfile(FilePython2,)

  #print('\n')
  #mdb.saveAs(pathName=FileCae)

  #提交Job
  StrPrint=ToChinese("\t 提交计算任务...\n")
  print >> sys.__stdout__, StrPrint
  sys.__stdout__.flush()
  print StrPrint
  execfile(FilePython3,)
  
  #后处理
  StrPrint=ToChinese("\t 后处理...\n")
  print >> sys.__stdout__, StrPrint
  sys.__stdout__.flush()
  print StrPrint
  execfile(FilePython4,)
  StrPrint=ToChinese("\t 后处理完成...\n")
  print >> sys.__stdout__, StrPrint
  sys.__stdout__.flush()
  print StrPrint
  
#清除不必要的文件
StrPrint=ToChinese("\n整体计算完成\n\n 清理不必要的文件...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print StrPrint
execfile(FilePython5,)

#复制abaqus输出文件名
FileOld=FileOutStatic
FileNew=FileOutStatic[:-4]+'-Num'+str_ii+'.txt'
StrCmd='@ copy /y '+ FileOld +' '+ FileNew
os.system(StrCmd)

#压缩图片到压缩文件
FileFigzip="Figs-Num"+str_ii
ret=shutil.make_archive(FileFigzip,'zip', root_dir='Figs')
ret=shutil.rmtree('Figs')