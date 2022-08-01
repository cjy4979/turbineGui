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
#:  批量计算随机分布的单只叶片应�?循环周期对称)...
#: 
#:  清理不必要的文件...
#: �µ�ģ�����ݿ��Ѵ���.
#: ģ�� "Model-1" �Ѵ���.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: 
#:  读取cae文件...
#: ģ�����ݿ� "C:\Users\CJY\Desktop\StressMore\TurbineStatic.cae" �Ѵ�.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: 
#:  读取随机分布的参�?..
#: ****ERROR: Transcoding Error: 
#:  ������2�顣
#: ****ERROR: Transcoding Error: 
#:  ��001��:
#: 	 ��ȡ�����������ֵ
#: 	 创建计算任务...
#: 	 提交计算任务...
#: 		 提交时间:2022-07-25 15:25:55.166000
#: 		 完成时间:2022-07-25 15:27:12.726000
#: 		 计算耗时:77.5610527s 
#: 	 后处�?..
#: ģ��: C:/Users/CJY/Desktop/StressMore/TurbineStatic.odb
#: װ�������:         1
#: װ���ʵ������: 0
#: ����ʵ���ĸ���:     1
#: ������:             1
#: ��Ԫ������:       4
#: ��㼯����:          9
#: �������ĸ���:              1
#: 	 后处理完�?..
#: ****ERROR: Transcoding Error: 
#:  ��002��:
#: 	 ��ȡ�����������ֵ
#: 	 创建计算任务...
#: 	 提交计算任务...
#: 		 提交时间:2022-07-25 15:27:28.958000
#: 		 完成时间:2022-07-25 15:28:46.787000
#: 		 计算耗时:77.8290828s 
#: 	 后处�?..
#: ģ��: C:/Users/CJY/Desktop/StressMore/TurbineStatic.odb
#: װ�������:         1
#: װ���ʵ������: 0
#: ����ʵ���ĸ���:     1
#: ������:             1
#: ��Ԫ������:       4
#: ��㼯����:          9
#: �������ĸ���:              1
#: 	 后处理完�?..
#: 
#: 整体计算完成
#: 
#:  清理不必要的文件...
#: �µ�ģ�����ݿ��Ѵ���.
#: ģ�� "Model-1" �Ѵ���.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
print 'RT script done'
#: RT script done
