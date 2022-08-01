# -*- coding: UTF-8 -*-

################
##  提交任务
################
#运行Job
t0 = timeit.default_timer()

#mdb.jobs[JobName].writeInput(consistencyChecking=OFF)
mdb.jobs[JobName].submit(consistencyChecking=OFF)
mdb.jobs[JobName].waitForCompletion()

tn = timeit.default_timer()
tt=tn-t0

StrPrint='\n     Time='+ str(tt) +'s \n'
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print StrPrint