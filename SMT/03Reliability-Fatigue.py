# -*- codig: UTF-8 -*-
from __future__ import print_function
import warnings
import AllDef as AD #自定义函数

if __name__=='__main__':
  #忽略warnings,不然在cmd窗口会输出一堆warning
  warnings.filterwarnings("ignore")
  #程序标记
  Exec1="Fatigue"
  Exec2="疲劳可靠性"
  
  #输入量
  FileAbaqus1="AbaqusOutTurbineStatic.txt" #Abaqus输出文件1，用于构建SMT模型
  FileAbaqus2="AbaqusOutTurbineStatic2.txt"#Abaqus输出文件2，用于校核SMT模型
  Num1=int(1e5)#可靠性计算大样本抽样数量
  FileGauss="GH4169-Gauss.txt"#保存随机变量信息的文本，用于可靠性计算大样本抽样
  FileMater="GH4169-Fatigue.txt" #存储GH4169材料的4个疲劳系数
  DocxName=AD.Object2+Exec2
  
  #清除不必要的文件
  AD.ClearFileDir()
  
  #自定义画图设置
  AD.FigConfig()
  
  print('\n 预测大样本的最大Mises应力应变 \n')  
  XR,YR,OptOut_str1,FigList1,FigCaption1,TxtList1,TxtCaption1,TxtHead1=\
    AD.StressStrain(Exec2,Num1,FileGauss,FileAbaqus1,FileAbaqus2)

  print('\n 预测大样本的疲劳寿命 \n')  
  FigList2,FigCaption2,TxtList2,TxtCaption2,TxtHead2=AD.FatigueReliability(XR,YR,FileMater)
  
  print('图片和表格输出到文件: "%s.docx" \n' %(DocxName))
  OptOut_str=OptOut_str1
  FigList=FigList1+FigList2
  FigCaption=FigCaption1+FigCaption2
  TxtList=TxtList1+TxtList2
  TxtCaption=TxtCaption1+TxtCaption2
  TxtHead=TxtHead1+TxtHead2
  path=AD.AddFigTab(Exec1,OptOut_str,FigList,FigCaption,TxtList,TxtCaption,TxtHead,DocxName)