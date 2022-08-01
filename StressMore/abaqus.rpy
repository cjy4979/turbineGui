# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2021 replay file
# Internal Version: 2020_03_06-22.50.37 167380
# Run by CJY on Mon Jul 25 15:25:54 2022
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
execfile('C:/Users/CJY/Desktop/StressMore/0MoreStaticCae.py', 
    __main__.__dict__)
#: 
#:  鎵归噺璁＄畻闅忔満鍒嗗竷鐨勫崟鍙彾鐗囧簲鍔?寰幆鍛ㄦ湡瀵圭О)...
#: 
#:  娓呯悊涓嶅繀瑕佺殑鏂囦欢...
#: 新的模型数据库已创建.
#: 模型 "Model-1" 已创建.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: 
#:  璇诲彇cae鏂囦欢...
#: 模型数据库 "C:\Users\CJY\Desktop\StressMore\TurbineStatic.cae" 已打开.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: 
#:  璇诲彇闅忔満鍒嗗竷鐨勫弬鏁?..
#: ****ERROR: Transcoding Error: 
#:  共计算2组。
#: ****ERROR: Transcoding Error: 
#:  第001组:
#: 	 读取随机参数并赋值
#: 	 鍒涘缓璁＄畻浠诲姟...
#: 	 鎻愪氦璁＄畻浠诲姟...
#: 		 鎻愪氦鏃堕棿:2022-07-25 15:25:55.166000
#: 		 瀹屾垚鏃堕棿:2022-07-25 15:27:12.726000
#: 		 璁＄畻鑰楁椂:77.5610527s 
#: 	 鍚庡鐞?..
#: 模型: C:/Users/CJY/Desktop/StressMore/TurbineStatic.odb
#: 装配件个数:         1
#: 装配件实例个数: 0
#: 部件实例的个数:     1
#: 网格数:             1
#: 单元集合数:       4
#: 结点集合数:          9
#: 分析步的个数:              1
#: 	 鍚庡鐞嗗畬鎴?..
#: ****ERROR: Transcoding Error: 
#:  第002组:
#: 	 读取随机参数并赋值
#: 	 鍒涘缓璁＄畻浠诲姟...
#: 	 鎻愪氦璁＄畻浠诲姟...
#: 		 鎻愪氦鏃堕棿:2022-07-25 15:27:28.958000
#: 		 瀹屾垚鏃堕棿:2022-07-25 15:28:46.787000
#: 		 璁＄畻鑰楁椂:77.8290828s 
#: 	 鍚庡鐞?..
#: 模型: C:/Users/CJY/Desktop/StressMore/TurbineStatic.odb
#: 装配件个数:         1
#: 装配件实例个数: 0
#: 部件实例的个数:     1
#: 网格数:             1
#: 单元集合数:       4
#: 结点集合数:          9
#: 分析步的个数:              1
#: 	 鍚庡鐞嗗畬鎴?..
#: 
#: 鏁翠綋璁＄畻瀹屾垚
#: 
#:  娓呯悊涓嶅繀瑕佺殑鏂囦欢...
#: 新的模型数据库已创建.
#: 模型 "Model-1" 已创建.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
print 'RT script done'
#: RT script done
