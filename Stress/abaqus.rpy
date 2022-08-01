# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2021 replay file
# Internal Version: 2020_03_06-22.50.37 167380
# Run by CJY on Mon Jul 25 21:06:11 2022
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
    'C:/Users/CJY/Desktop/GUI0724/smt/dist/GUI_0725/Stress/0MakeStaticCae.py', 
    __main__.__dict__)
#: 
#:  璁＄畻鍗曞彧鍙剁墖搴斿姏(寰幆鍛ㄦ湡瀵圭О)...
#: 
#:  璇诲彇ansa鐢熸垚鐨刬np鏂囦欢...
#: 模型 "Model-1" 已创建.
#: 部件 "PART-1" 已从输入文件中导入.
#: 相互作用 "Int-CycSymm" 已创建.
#: 模型 "Model-1" 已从输入文件导入. 
#: 请向上拖动滚动条以查看错误或警告信息.
#: 
#:  璇诲彇Fluent鐢熸垚鐨勫闈㈡俯搴︽暟鎹紝褰㈡垚analytical field...
#: 
#:  淇敼static鍒嗘瀽姝?..
#: 
#:  鍒涘缓Job...
#: 
#:  淇濆瓨cae鏂囦欢...
#: 模型数据库已保存到 "C:\Users\CJY\Desktop\GUI0724\smt\dist\GUI_0725\Stress\TurbineStatic.cae".
#: 
#:  鎻愪氦Job...
#: 		 鎻愪氦鏃堕棿:2022-07-25 21:06:19.801000
#: 		 瀹屾垚鏃堕棿:2022-07-25 21:07:49.200000
#: 		 璁＄畻鑰楁椂:89.3987139s 
#: 
#:  鍚庡鐞?..
#: 模型: C:/Users/CJY/Desktop/GUI0724/smt/dist/GUI_0725/Stress/TurbineStatic.odb
#: 装配件个数:         1
#: 装配件实例个数: 0
#: 部件实例的个数:     1
#: 网格数:             1
#: 单元集合数:       4
#: 结点集合数:          9
#: 分析步的个数:              1
#: 
#:  娓呴櫎涓嶅繀瑕佺殑鏂囦欢...
#: 新的模型数据库已创建.
#: 模型 "Model-1" 已创建.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
print 'RT script done'
#: RT script done
