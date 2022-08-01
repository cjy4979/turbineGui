# -*- coding: UTF-8 -*-

#读取odb文件
odb  =openOdb(path = FileOdbStatic)
FigS1 ='Fig-Sample'+str_ii+'-S1.png'
FigU1 ='Fig-Sample'+str_ii+'-U1.png'
FigLE1='Fig-Sample'+str_ii+'-LE1.png'
FigS2 ='Fig-Sample'+str_ii+'-S2.png'
FigU2 ='Fig-Sample'+str_ii+'-U2.png'
FigLE2='Fig-Sample'+str_ii+'-LE2.png'

#提取最大mises应力和mises应变
execfile('1PostMakeStressStrain.py',)
##输出云图
execfile('1PostMakeContour.py',)

#关闭odb
session.odbs[FileOdbStatic].close()

#判断目录是否存在
DirFig='Figs'
if not os.path.exists(DirFig):
  os.makedirs(DirFig) 
##将图片移动到目录
#StrCmd='@move /y Fig*.png '+DirFig
#os.system(StrCmd)

for file in glob.glob("Fig*.png"):
  shutil.copy(file,DirFig)
  os.remove(file)
#EndFor

##修改odb名称
#FileOld=FileOdbStatic
#FileNew=FileOdbStatic[:-4]+str_ii+'.odb'
#if os.path.exists(FileNew):
#  os.remove(FileNew)
#
#os.rename(FileOld,FileNew)