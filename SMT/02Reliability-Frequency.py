# -*- coding: UTF-8 -*-
from __future__ import print_function
import numpy as np
import warnings
import AllDef as AD #自定义函数

if __name__=='__main__':
  #忽略warnings,不然在cmd窗口会输出一堆warning
  warnings.filterwarnings("ignore")
  #程序标记
  Exec1="Freq"
  Exec2="振动可靠性"
  
  #输入量
  FileAbaqus1="AbaqusOutTurbineFreq.txt" #Abaqus输出文件1，用于构建SMT模型
  FileAbaqus2="AbaqusOutTurbineFreq2.txt"#Abaqus输出文件2，用于校核SMT模型
  Num1=int(1e5)#可靠性计算大样本抽样数量
  FileGauss="GH4169-Gauss.txt"#保存随机变量信息的文本，用于可靠性计算大样本抽样
  DocxName=AD.Object2+Exec2
  
  #清除不必要的文件
  AD.ClearFileDir()
  #自定义画图设置
  AD.FigConfig()
  
  
  ######################
  # 构建Kriging代理模型
  ######################
  #读取Abaqus计算的频率结果，构建kriging模型
  print('\n\n读取Abaqus计算的频率结果 \n')
  #读取第1个abaqus计算的频率结果，样本数少，用于构建kriging模型
  print('\t 读取数据构建kriging模型 \n')
  X1,Freq1=AD.GetDataFreq(FileAbaqus1)
  #读取第2个abaqus计算的频率结果，样本数多，用于校核kriging模型
  print('\t 读取数据校核kriging模型 \n')
  X2,Freq2=AD.GetDataFreq(FileAbaqus2)
  
  #谐波频率避开率Δ
  delta=0.05#避开率Δ
  
  #提取各阶节径振型固有频率，分别构建kriging模型，并校核
  II=[]
  R1=[]
  R2=[]
  OptOut_str=[]
  FigList=[]
  FigCaption=[]
  TxtList=[]
  TxtCaption=[]
  TxtHead=[]
  for index in range(len(Freq1[0])):
    Y1=np.c_[Freq1[:,index]]#提取某阶节径振型固有频率，并转为列向量
    Y2=np.c_[Freq2[:,index]]#校核用的
    II.append(index+1)
    R_tri,R_delta,OptSMT_str1,FigList1,FigCaption1,TxtList1,TxtCaption1,TxtHead1=\
      AD.FrequencyReliability(index+1,X1,Y1,X2,Y2,delta,Num1,FileGauss)
    R1.append(R_tri)
    R2.append(R_delta)
    OptOut_str.extend(OptSMT_str1)
    FigList.extend(FigList1)
    FigCaption.extend(FigCaption1)
    TxtList.extend(TxtList1)
    TxtCaption.extend(TxtCaption1)
    TxtHead.extend(TxtHead1)
    #FigCaption=FigCaption+FigCaption1
  #EndFor
  R=np.c_[R1]*np.c_[R2]
  
  #保存可靠性结果
  print('\n保存各节径振动可靠度到txt文本\n')
  data=np.c_[II,II,R,R1,R2]
  StrFile='KrigingOut-Frequency-Reliability.txt'
  TxtCaption1=AD.Object2+'前%d节径振动可靠度' %(index+1)
  TxtHead1=['编号','节径','总可靠度','三重点共振可靠度', '谐波频率避开率%3.2f%%可靠度' %(delta*100)]
  TxtList.append(StrFile)
  TxtCaption.append(TxtCaption1)
  TxtHead.append(TxtHead1)
  
  f = open(StrFile, 'w', encoding='utf-8-sig') # 打开文件， 用'w'写文件
  f.write('#%s\n'   %(TxtCaption1))
  f.write('#    %s     %s    %s    %s    %s\n' %(TxtHead1[0],TxtHead1[1],TxtHead1[2],TxtHead1[3],TxtHead1[4]))
  #np.savetxt(f, X=data, fmt='%d     %d       %f            %f            %f', delimiter=' ', encoding='utf-8-sig')
  np.savetxt(f, X=data, delimiter=' ', encoding='utf-8-sig')
  f.close() 
  
  print('图片和表格输出到文件: "%s.docx" \n' %(DocxName)) 
  path=AD.AddFigTab(Exec1,OptOut_str,FigList,FigCaption,TxtList,TxtCaption,TxtHead,DocxName)