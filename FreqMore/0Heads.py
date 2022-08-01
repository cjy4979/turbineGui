# -*- coding: UTF-8 -*-
#头文件
from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
from visualization import *
from odbAccess import *
import string
import os
import numpy as np
import math
import multiprocessing
import timeit
import sys
import glob
import shutil
import datetime

#CPU可用数目
NumCPU=multiprocessing.cpu_count()

#变量命名
FilePython1=cur_dir+ "/" +"1ChangeFreqStep.py"#读取Fluent生成的壁面温度数据
FilePython2=cur_dir+ "/" +"1MakeJob.py"#创建Job
FilePython3=cur_dir+ "/" +"1RunJob.py"#运行Job
FilePython4=cur_dir+ "/" +"1PostGetFreq.py"#提取static的Miese应力和应变
FilePython5=cur_dir+ "/" +"1ClearFile.py"#清除不必要的文件

FileThermal="TurbineThermal"#文件名，
FileStaFreq="TurbineStaticFreq"#文件名，
FileCaeThermal=cur_dir+ "/"+FileThermal+".cae"#Thermal的cae文件
FileOdbThermal=cur_dir+ "/"+FileThermal+".odb"#Thermal的odb文件
FileCaeStaFreq=cur_dir+ "/"+FileStaFreq+".cae"#Static的cae文件
FileOdbStaFreq=cur_dir+ "/"+FileStaFreq+".odb"#Static的odb文件
FileInputStatic =cur_dir+ "/AbaqusInputLatinHypercube.txt"#Static批处理计算输入的密度、弹模、转速
FileOutStatic   =cur_dir+ "/AbaqusOutTurbineStatic.txt"#Static输出misese应力应变的文件
FileOutFreq     =cur_dir+ "/AbaqusOutTurbineFreq.txt"#Static输出固有频率的文件

NumR1=90#第1列叶片数目
NumR2=94#第2列叶片数目

FreqNum=30       #要计算的固有频率数目
FreqMin=100.0    #最小固有频率
FreqMax=20000.0  #最大固有频率

#定义转中文字符的函数
def ToChinese(string):
  return string.decode('utf-8').encode('utf-8')