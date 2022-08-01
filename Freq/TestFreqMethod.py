# -*- coding: UTF-8 -*-
#头文件
import string
import os
from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
import timeit
import multiprocessing as mp

def RunJob():
  Num_CPU=int(mp.cpu_count())
  mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, 
      atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
      memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
      explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
      modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
      scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=Num_CPU, 
      numDomains=Num_CPU, numGPUs=0)
  mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
  mdb.jobs['Job-1'].waitForCompletion()
#EndDef

def GetFreq():
  #当前文件夹
  cur_dir=os.getcwd()
  #名称
  File_0           ="Job-1"
  File_ODB         =File_0+".odb"
  #读取odb文件
  FileInput=cur_dir+ "/" +File_ODB
  odb = session.openOdb(name = FileInput)
  frame = odb.steps[StepName2].frames
  #输出频率的文本文件
  f = open('AbaqusOutput.txt', 'a') # 打开文件， 用'w'写文件
  f.write('#各阶固有频率(Hz):\n')
  for i in range(1,len(frame)):
    aa=frame[i].frequency#频率值
    f.write('%10.2f  ' %(aa)) # 将最大应力写文本文件
  f.write('\n')
  f.close() 
  session.odbs[FileInput].close()
#EndDef

##新建文件
#f=open('AbaqusOutput.txt', 'w') # 打开文件， 用'w'写文件
#f.close() 

#要计算的固有频率数目
FreqNum=30
#最小固有频率
FreqMin=100.0
#最大固有频率
FreqMax=20000.0
#
StepName1='Initial'
StepName2='Step-1'

'''
#Subspace方法求固有频率
del mdb.models['Model-1'].steps[StepName2]
str0='Subspace方法求固有频率'
mdb.models['Model-1'].FrequencyStep(name=StepName2, previous=StepName1, 
    simLinearDynamics=OFF, normalization=MASS, numEigen=FreqNum, vectors=FreqNum+8, 
    maxIterations=30,minEigen=FreqMin,maxEigen=FreqMax, eigensolver=SUBSPACE, acousticCoupling=AC_OFF)
#运行Job
t0 = timeit.default_timer()
RunJob()
tn = timeit.default_timer()
tt=tn-t0
print 'Time=', str(tt), 's'
f=open('AbaqusOutput.txt', 'a') # 打开文件， 用'w'写文件
f.write('\n#############################\n')
f.write('#%s\n' %str0) # 将最大应力写文本文件
f.write('#计算耗时Time= %10.8e s \n' %tt) # 将最大应力写文本文件
f.close() 
GetFreq()
'''

#Lanczos方法求固有频率
del mdb.models['Model-1'].steps[StepName2]
str0='Lanczos方法求固有频率'    
mdb.models['Model-1'].FrequencyStep(name=StepName2, previous=StepName1, 
    normalization=MASS, minEigen=FreqMin,maxEigen=FreqMax, numEigen=FreqNum, eigensolver=LANCZOS, 
    simLinearDynamics=OFF)

#运行Job
t0 = timeit.default_timer()
RunJob()
tn = timeit.default_timer()
tt=tn-t0
print 'Time=', str(tt), 's'
f=open('AbaqusOutput.txt', 'a') # 打开文件， 用'w'写文件
f.write('#%s\n' %str0) # 将最大应力写文本文件
f.write('#计算耗时Time= %10.8e s \n' %tt) # 将最大应力写文本文件
f.close() 
GetFreq()

#AMS方法求固有频率
del mdb.models['Model-1'].steps[StepName2]
str0='AMS方法求固有频率'
mdb.models['Model-1'].FrequencyStep(name=StepName2, previous=StepName1, simLinearDynamics=ON,
    normalization=MASS,numEigen=FreqNum, minEigen=FreqMin, maxEigen=FreqMax,
    eigensolver=AMS, acousticCoupling=AC_OFF)

#运行Job
t0 = timeit.default_timer()
RunJob()
tn = timeit.default_timer()
tt=tn-t0
print 'Time=', str(tt), 's'
f=open('AbaqusOutput.txt', 'a') # 打开文件， 用'w'写文件
f.write('#%s\n' %str0) # 将最大应力写文本文件
f.write('#计算耗时Time= %10.8e s \n' %tt) # 将最大应力写文本文件
f.close() 
GetFreq()


