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
#:  计算单只叶片应力(循环周期对称)...
#: 
#:  读取ansa生成的inp文件...
#: ģ�� "Model-1" �Ѵ���.
#: ���� "PART-1" �Ѵ������ļ��е���.
#: �໥���� "Int-CycSymm" �Ѵ���.
#: ģ�� "Model-1" �Ѵ������ļ�����. 
#: �������϶��������Բ鿴����򾯸���Ϣ.
#: 
#:  读取Fluent生成的壁面温度数据，形成analytical field...
#: 
#:  修改static分析�?..
#: 
#:  创建Job...
#: 
#:  保存cae文件...
#: ģ�����ݿ��ѱ��浽 "C:\Users\CJY\Desktop\GUI0724\smt\dist\GUI_0725\Stress\TurbineStatic.cae".
#: 
#:  提交Job...
#: 		 提交时间:2022-07-25 21:06:19.801000
#: 		 完成时间:2022-07-25 21:07:49.200000
#: 		 计算耗时:89.3987139s 
#: 
#:  后处�?..
#: ģ��: C:/Users/CJY/Desktop/GUI0724/smt/dist/GUI_0725/Stress/TurbineStatic.odb
#: װ�������:         1
#: װ���ʵ������: 0
#: ����ʵ���ĸ���:     1
#: ������:             1
#: ��Ԫ������:       4
#: ��㼯����:          9
#: �������ĸ���:              1
#: 
#:  清除不必要的文件...
#: �µ�ģ�����ݿ��Ѵ���.
#: ģ�� "Model-1" �Ѵ���.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
print 'RT script done'
#: RT script done
