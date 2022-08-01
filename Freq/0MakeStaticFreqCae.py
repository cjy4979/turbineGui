# -*- coding: UTF-8 -*-

#当前文件夹
cur_dir=os.getcwd()
FilePython0=cur_dir+ "/0Heads.py"#头文件
#头文件
execfile(FilePython0,)

#Thermal分析步信息
JobName=FileStaFreq #Job名
FileOdb=FileOdbStaFreq
FileCae=FileCaeStaFreq

StrPrint=ToChinese("\n 清理不必要的文件...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print StrPrint
execfile(FilePython9,)

StrPrint=ToChinese("\n 读取整圈结构inp文件(ANSA生成)...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print StrPrint
mdb.ModelFromInputFile(name='Model-1',inputFileName=FileAnsaInp)

StrPrint=ToChinese("\n 生成梁单元...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print StrPrint
execfile(FilePython2,)

StrPrint=ToChinese("\n 生成壳单元...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print StrPrint
execfile(FilePython3,)

StrPrint=ToChinese("\n 创建静力和频率分析步...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print StrPrint
execfile(FilePython5,)

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

StrPrint=ToChinese("\n 提交计算...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print StrPrint
execfile(FilePython7,)


StrPrint=ToChinese("\n 后处理，提取频率等...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print StrPrint
execfile(FilePython8,)

StrPrint=ToChinese("\n 清理不必要的文件...\n")
print >> sys.__stdout__, StrPrint
sys.__stdout__.flush()
print StrPrint
execfile(FilePython9,)

#压缩图片到压缩文件
ret=shutil.make_archive("Figs-bak",'zip', root_dir='Figs')
ret=shutil.rmtree('Figs')