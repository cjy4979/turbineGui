# -*- coding: UTF-8 -*-
from __future__ import print_function
from scipy.stats import qmc
import numpy as np
import matplotlib.pyplot as plt
import warnings
import AllDef as AD #自定义函数

if __name__=='__main__':
  #忽略warnings，不然在cmd窗口会输出一堆warning
  warnings.filterwarnings("ignore")
  #程序标记
  Exec1="Sampling"
  Exec2="抽样"       
  
  ##输入量
  NumSample=40 ##初始设定的样本数量，后面要找到距离最近的素数
  FileGauss="GH4169-Gauss.txt"#保存随机变量信息的文本
  DocxName=AD.Object2+Exec2
  
  FigList=[]
  FigCaption=[]
  TxtList=[]
  TxtCaption=[]
  TxtHead=[]
  
  #清除不必要的文件
  AD.ClearFileDir()
  
  #自定义画图设置
  AD.FigConfig()
  
  print('读取原始数据 \n') 
  #读取文本文件，存入矩阵。分隔符为','，注释符为'#'
  data = np.loadtxt(FileGauss, comments='#',encoding='utf-8-sig')
  
  print('生成正态分布的平均值和标准差 \n') 
  #密度平均值(kg/m3)
  rho_avg=data[0,0]
  #密度变异系数
  rho_cv=data[0,1]
  #弹模平均值(GPa)
  E_avg=data[1,0]
  #弹模变异系数
  E_cv=data[1,1]
  #转速平均值(rpm)
  rpm_avg=data[2,0]
  #转速变异系数
  rpm_cv=data[2,1]
  
  #密度标准差
  rho_std=rho_avg*rho_cv
  #密度方差
  rho_var=rho_std*rho_std
  #弹模标准差
  E_std=E_avg*E_cv
  #弹模方差
  E_var=E_std*E_std
  #转速标准差
  rpm_std=rpm_avg*rpm_cv
  #转速方差
  rpm_var=rpm_std*rpm_std
  
  #根据正态分布的3σ准则确定样本抽样的上下限
  A=np.array([rho_avg,E_avg,rpm_avg])
  B=np.array([rho_std,E_std,rpm_std])
  l_bounds = A-4.0*B#样本缩放的下限
  u_bounds = A+4.0*B#样本缩放的上限
  #print(l_bounds,'\n')
  #print(u_bounds,'\n')
  #num0必须是素数：2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31
  num0=[2,3,5,7,11,13,17,19,23,29,31]
  Num0=np.c_[num0]**2
  
  #在素数平方中找到距离NumSample最近的素数平方
  temp=abs(Num0-NumSample)
  b=np.where(temp == min(temp))
  index=b[0][0]#最接近的位置坐标
  Num1=Num0[index,0]#抽样组的数目(采用强度2时，数目必须素数的平方)
  
  dim1=A.shape[0] #抽样维度的数目
  #print(dim1)
  StrNum='%03d'%(Num1)
    
  print('生成%d个优化拉丁超立方样本，强度为2 \n' %(Num1))
  #2维优化拉丁超立方，强度为2
  sampler = qmc.LatinHypercube(d=dim1,strength=2,optimization="random-cd")
  sample0 = sampler.random(n=Num1)
  error1  = qmc.discrepancy(sample0)
  sample  = qmc.scale(sample0, l_bounds, u_bounds)#样本缩放到上下限。
  #print(l_bounds)
  #print(u_bounds)
  #print(np.min(sample[:,0]),np.min(sample[:,1]),np.min(sample[:,2]))
  #print(np.max(sample[:,0]),np.max(sample[:,1]),np.max(sample[:,2]))
  
  print('绘制样本第1、2维数据图 \n') 
  str0='%.3e' %error1
  StrTitle=AD.Object2+'优化拉丁超立方抽样第1、2维数据(强度2,'+'差异度'+str0+')'
  fig = plt.figure()    # 定义一个图像窗口
  plt.plot(sample[:,0],sample[:,1],'.',markersize=4,color='blue')
  #plt.legend(loc="upper left")
  #plt.title(str1,fontsize=7)
  plt.title(StrTitle)
  plt.xlabel('密度 [kg/m^3]')
  plt.ylabel('弹性模量 [GPa]')
  FigName='Fig-LatinHypercube-Num'+StrNum+'-Dim1vDim2.png'
  plt.savefig(FigName, bbox_inches='tight')
  #plt.savefig('fig1.pdf', bbox_inches='tight') 
  plt.close()
  FigList.append(FigName)
  FigCaption.append(StrTitle)
  
  print('绘制样本第2、3维数据图 \n') 
  fig = plt.figure()    # 定义一个图像窗口
  StrTitle=AD.Object2+'拉丁超立方抽样第2、3维数据(强度2,'+'差异度'+str0+')'
  plt.plot(sample[:,1],sample[:,2],'.',markersize=4,color='blue')
  #plt.legend(loc="upper left")
  plt.title(StrTitle)
  plt.xlabel('弹性模量 [GPa]')
  plt.ylabel('转速 [r/min]')
  FigName='Fig-LatinHypercube-Num'+StrNum+'-Dim2vDim3.png'
  plt.savefig(FigName, bbox_inches='tight')
  plt.close()
  FigList.append(FigName)
  FigCaption.append(StrTitle)
  
  TxtName='AbaqusInputLatinHypercube-Num'+StrNum+'.txt'
  TabCaption=AD.Object2+'抽样数据(n='+'%d'%(Num1)+')'
  TabHead=['样本编号','密度[kg/m^3]','弹性模量[GPa]','转速[r/min]']
  print('保存样本到文件: "%s" \n' %(TxtName)) 
  XX=np.arange(1,len(sample[:,0])+1,1)
  data=np.c_[XX,sample]
  f = open(TxtName, 'w', encoding='utf-8-sig') # 打开文件， 用'w'写文件
  f.write('#%s\n' %(TabCaption))
  f.write('#      %s         ' %(TabHead[0]))
  f.write('       %s         ' %(TabHead[1]))
  f.write('       %s         ' %(TabHead[2]))
  f.write('       %s         \n' %(TabHead[3]))
  np.savetxt(f, X=data, delimiter=' ')
  f.close() 
  TxtList.append(TxtName)
  TxtCaption.append(TabCaption)
  TxtHead.append(TabHead)
  
  OptOut_str=[]
  print('图片和表格输出到文件: "%s.docx" \n' %(DocxName)) 
  AD.AddFigTab(Exec1,OptOut_str,FigList,FigCaption,TxtList,TxtCaption,TxtHead,DocxName)
  print('完成 \n') 
