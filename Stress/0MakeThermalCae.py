# -*- coding: UTF-8 -*-
#当前文件夹
import os
cur_dir=os.getcwd()
FilePython0=cur_dir+ "/" +"0Heads.py"#头文件
#头文件
exec(open(FilePython0).read())

#Thermal分析步信息
JobName=FileThermal #Job名
FileOdb=FileOdbThermal
FileCae=FileCaeThermal

StrPrint=ToChinese("\n 计算单只叶片温度分布(循环周期对称)...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print (StrPrint)

StrPrint=ToChinese("\n 读取ansa生成的inp文件...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print (StrPrint)
mdb.ModelFromInputFile(name='Model-1',inputFileName=FileAnsaInp)

StrPrint=ToChinese("\n 读取Fluent生成的壁面温度数据，形成analytical field...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print (StrPrint)
execfile(FilePython1,)

StrPrint=ToChinese("\n 创建传热分析步...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print (StrPrint)
execfile(FilePython3,)

StrPrint=ToChinese("\n 创建Job...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print (StrPrint)
execfile(FilePython5,)

StrPrint=ToChinese("\n 保存cae文件...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print (StrPrint)
mdb.saveAs(pathName=FileCae)

StrPrint=ToChinese("\n 提交Job...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print (StrPrint)
execfile(FilePython6,)

StrPrint=ToChinese("\n 清除不必要的文件...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print (StrPrint)
execfile(FilePython9,) 