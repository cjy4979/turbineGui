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
#:  清理不必要的文件...
#: �µ�ģ�����ݿ��Ѵ���.
#: ģ�� "Model-1" �Ѵ���.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: 
#:  读取单级叶片inp文件(ANSA生成)...
#: ģ�� "Model-1" �Ѵ���.
#: ���� "PART-1" �Ѵ������ļ��е���.
#: ģ�� "Model-1" �Ѵ������ļ�����. 
#: �������϶��������Բ鿴����򾯸���Ϣ.
#: 
#:  计算单级叶片温度分布，构建整圈结构的温度分布边界...
#: ����: 
#: Following warning detected while evaluating the Mapped Field "AnalyticalField-Temp",
#: for a Boundary Condition.
#: The mapper has mapped the field values using distance weighting 
#: algorithm for some of the target nodes.
#: ģ��: C:/Users/CJY/Desktop/GUI0724/smt/dist/GUI_0725/Freq/Job-1.odb
#: װ�������:         1
#: װ���ʵ������: 0
#: ����ʵ���ĸ���:     1
#: ������:             1
#: ��Ԫ������:       2
#: ��㼯����:          6
#: �������ĸ���:              1
#: 
#:  读取整圈结构inp文件(ANSA生成)...
#: ģ�� "Model-1" �Ѵ���.
#: ���� "PART-1" �Ѵ������ļ��е���.
#: 
#: WARNING: Node-based surfaces are not yet supported in Abaqus/CAE. The following node sets have been created in place of the corresponding node-based surfaces so they can be used in Abaqus/CAE. 
#: Node Set Created            Node-Based Surface  
#: ------------------          -------------------- 
#:     SHELL2SOLIDTIE1-1            SHELL2SOLIDTIE1-1
#:     SHELL2SOLIDTIE2-1            SHELL2SOLIDTIE2-1
#: ģ�� "Model-1" �Ѵ������ļ�����. 
#: �������϶��������Բ鿴����򾯸���Ϣ.
#: 
#:  创建壳单�?..
#: 
#:  创建整圈结构热分析计算步...
#: 
#:  创建计算任务...
#: 
#:  保存cae文件...
#: ģ�����ݿ��ѱ��浽 "C:\Users\CJY\Desktop\GUI0724\smt\dist\GUI_0725\Freq\TurbineThermal.cae".
#: 
#:  提交计算任务...
#: ����: 
#: Following warning detected while evaluating the Mapped Field "AnalyticalField-Temp",
#: for a Boundary Condition.
#: The mapper has mapped the field values using distance weighting 
#: algorithm for some of the target nodes.
#: 
#:      Time=78.3993872s 
#: 
#:  清理不必要的文件...
#: �µ�ģ�����ݿ��Ѵ���.
#: ģ�� "Model-1" �Ѵ���.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
print 'RT script done'
#: RT script done
