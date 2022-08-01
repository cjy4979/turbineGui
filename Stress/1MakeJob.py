# -*- coding: mbcs -*-
#计算前先删除odb文件
#StrCmd='del /q '+FileOdb
#os.system(StrCmd)

################
##  创建任务
################
if NumCPU>10:
  NumCPU=10#测试了一下，发现10核的速度最佳
mdb.Job(name=JobName, model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=NumCPU, 
    numDomains=NumCPU, numGPUs=0)