# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2021 replay file
# Internal Version: 2020_03_06-22.50.37 167380
# Run by CJY on Mon Jul 25 21:11:40 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(1.20703, 1.20139), width=177.675, 
    height=119.178)
session.viewports['Viewport: 1'].makeCurrent()
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
execfile(
    'C:/Users/CJY/Desktop/GUI0724/smt/dist/GUI_0725/Freq/0MakeThermalCae.py', 
    __main__.__dict__)
#: 
#:  娓呯悊涓嶅繀瑕佺殑鏂囦欢...
#: 新的模型数据库已创建.
#: 模型 "Model-1" 已创建.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: 
#:  璇诲彇鍗曠骇鍙剁墖inp鏂囦欢(ANSA鐢熸垚)...
#: 模型 "Model-1" 已创建.
#: 部件 "PART-1" 已从输入文件中导入.
#: 模型 "Model-1" 已从输入文件导入. 
#: 请向上拖动滚动条以查看错误或警告信息.
#: 
#:  璁＄畻鍗曠骇鍙剁墖娓╁害鍒嗗竷锛屾瀯寤烘暣鍦堢粨鏋勭殑娓╁害鍒嗗竷杈圭晫...
#: 警告: 
#: Following warning detected while evaluating the Mapped Field "AnalyticalField-Temp",
#: for a Boundary Condition.
#: The mapper has mapped the field values using distance weighting 
#: algorithm for some of the target nodes.
#: 模型: C:/Users/CJY/Desktop/GUI0724/smt/dist/GUI_0725/Freq/Job-1.odb
#: 装配件个数:         1
#: 装配件实例个数: 0
#: 部件实例的个数:     1
#: 网格数:             1
#: 单元集合数:       2
#: 结点集合数:          6
#: 分析步的个数:              1
#: 
#:  璇诲彇鏁村湀缁撴瀯inp鏂囦欢(ANSA鐢熸垚)...
#: 模型 "Model-1" 已创建.
#: 部件 "PART-1" 已从输入文件中导入.
#: 
#: WARNING: Node-based surfaces are not yet supported in Abaqus/CAE. The following node sets have been created in place of the corresponding node-based surfaces so they can be used in Abaqus/CAE. 
#: Node Set Created            Node-Based Surface  
#: ------------------          -------------------- 
#:     SHELL2SOLIDTIE1-1            SHELL2SOLIDTIE1-1
#:     SHELL2SOLIDTIE2-1            SHELL2SOLIDTIE2-1
#: 模型 "Model-1" 已从输入文件导入. 
#: 请向上拖动滚动条以查看错误或警告信息.
#: 
#:  鍒涘缓澹冲崟鍏?..
#: 
#:  鍒涘缓鏁村湀缁撴瀯鐑垎鏋愯绠楁...
#: 
#:  鍒涘缓璁＄畻浠诲姟...
#: 
#:  淇濆瓨cae鏂囦欢...
#: 模型数据库已保存到 "C:\Users\CJY\Desktop\GUI0724\smt\dist\GUI_0725\Freq\TurbineThermal.cae".
#: 
#:  鎻愪氦璁＄畻浠诲姟...
#: 警告: 
#: Following warning detected while evaluating the Mapped Field "AnalyticalField-Temp",
#: for a Boundary Condition.
#: The mapper has mapped the field values using distance weighting 
#: algorithm for some of the target nodes.
#: 
#:      Time=78.3993872s 
#: 
#:  娓呯悊涓嶅繀瑕佺殑鏂囦欢...
#: 新的模型数据库已创建.
#: 模型 "Model-1" 已创建.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
print 'RT script done'
#: RT script done
