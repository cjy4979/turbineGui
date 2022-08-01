# -*- coding: UTF-8 -*-

#当前文件夹
cur_dir=os.getcwd()
FilePython0=cur_dir+ "/" +"0Heads.py"#头文件
#头文件
execfile(FilePython0,)

#Thermal分析步信息
JobName=FileThermal #Job名
FileOdb=FileOdbThermal
FileCae=FileCaeThermal

StrPrint=ToChinese("\n 清理不必要的文件...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print StrPrint
execfile(FilePython9,)

StrPrint=ToChinese("\n 读取单级叶片inp文件(ANSA生成)...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print StrPrint
mdb.ModelFromInputFile(name='Model-1',inputFileName=FileAnsaInp0)

StrPrint=ToChinese("\n 计算单级叶片温度分布，构建整圈结构的温度分布边界...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print StrPrint
execfile(FilePython1,)

StrPrint=ToChinese("\n 读取整圈结构inp文件(ANSA生成)...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print StrPrint
mdb.ModelFromInputFile(name='Model-1',inputFileName=FileAnsaInp)

#StrPrint='\n 构建梁单元 \n'
#print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
#print StrPrint
#execfile(FilePython2,)

StrPrint=ToChinese("\n 创建壳单元...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print StrPrint
execfile(FilePython3,)

StrPrint=ToChinese("\n 创建整圈结构热分析计算步...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print StrPrint
execfile(FilePython4,)

StrPrint=ToChinese("\n 创建计算任务...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print StrPrint
execfile(FilePython6,)

StrPrint=ToChinese("\n 保存cae文件...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print StrPrint
mdb.saveAs(pathName=FileCae)

StrPrint=ToChinese("\n 提交计算任务...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print StrPrint
execfile(FilePython7,)

StrPrint=ToChinese("\n 清理不必要的文件...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print StrPrint
execfile(FilePython9,)
