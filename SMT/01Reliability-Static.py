# -*- coding: UTF-8 -*-
from __future__ import print_function
import warnings
import AllDef as AD #自定义函数

if __name__=='__main__':
  #忽略warnings,不然在cmd窗口会输出一堆warning
  warnings.filterwarnings("ignore")
  #程序标记
  Exec1="Static"
  Exec2="静强度可靠性"
  
  #输入量
  FileAbaqus1="AbaqusOutTurbineStatic.txt" #Abaqus输出文件1，用于构建SMT模型
  FileAbaqus2="AbaqusOutTurbineStatic2.txt"#Abaqus输出文件2，用于校核SMT模型
  Num1=int(1e5)#可靠性计算大样本抽样数量
  FileGauss="GH4169-Gauss.txt"#保存随机变量信息的文本，用于可靠性计算大样本抽样
  DocxName=AD.Object2+Exec2

  #清除不必要的文件
  AD.ClearFileDir()
  #自定义画图设置
  AD.FigConfig()
  
  print('\n 预测大样本的最大Mises应力应变 \n')  
  XR,YR,OptOut_str1,FigList1,FigCaption1,TxtList,TxtCaption,TxtHead= \
    AD.StressStrain(Exec2,Num1,FileGauss,FileAbaqus1,FileAbaqus2)
  S=YR[:,0]#提取应力
  
  print('\n 计算大样本的静强度可靠度 \n')  
  R,FigList2,FigCaption2=AD.StressReliability(S,FileGauss)
  
  print('图片和表格输出到文件: "%s.docx" \n' %(DocxName)) 
  OptOut_str=OptOut_str1
  FigList=FigList1+FigList2
  FigCaption=FigCaption1+FigCaption2
  path=AD.AddFigTab(Exec1,OptOut_str,FigList,FigCaption,TxtList,TxtCaption,TxtHead,DocxName)