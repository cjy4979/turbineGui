# -*- coding: UTF-8 -*-

################
##  提交任务
################
#运行Job
t0 = timeit.default_timer()
now_time = datetime.datetime.now()
StrPrint='\t\t 提交时间:'+ str(now_time) +'\n'
StrPrint=ToChinese(StrPrint)
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print StrPrint

#mdb.jobs[JobName].writeInput(consistencyChecking=OFF)
mdb.jobs[JobName].submit(consistencyChecking=OFF)
mdb.jobs[JobName].waitForCompletion()

tn = timeit.default_timer()
tt=tn-t0

now_time = datetime.datetime.now()
StrPrint='\t\t 完成时间:'+ str(now_time) +'\n'
StrPrint=StrPrint+'\t\t 计算耗时:'+ str(tt) +'s \n'
StrPrint=ToChinese(StrPrint)
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print StrPrint