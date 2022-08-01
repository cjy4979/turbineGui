# -*- coding: UTF-8 -*-

#修改分析步的名称
mdb.models['Model-1'].steps.changeKey(fromName='Step1', toName='Step-1')
    
#根据Analytical Filed创建压力载荷
a = mdb.models['Model-1'].rootAssembly
region = a.surfaces['PRESSURE']
mdb.models['Model-1'].Pressure(name='Load-2', createStepName='Step-1', 
    region=region, distributionType=FIELD, field='AnalyticalField-Pres', 
    magnitude=1.0, amplitude=UNSET)

#创建圆柱坐标系
a = mdb.models['Model-1'].rootAssembly
Cylindrical1=a.DatumCsysByThreePoints(name='Cylindrical', coordSysType=CYLINDRICAL, 
    origin=(0.0, 0.0, 100.0), point1=(100.0, 0.0, 100.0), point2=(100.0,100.0,100.0))
#后续调用该圆柱坐标系RTZ
Cylindrical1 = a.datums[Cylindrical1.id]

#限制圆柱坐标系Z向平动自由度的边界条件
region = a.sets['BC2']
mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Initial', 
    region=region, u1=UNSET, u2=UNSET, u3=SET, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=Cylindrical1)

#创建圆柱坐标系T向对称边界条件
region = a.sets['BC1']
mdb.models['Model-1'].YsymmBC(name='BC-1', createStepName='Initial', 
    region=region, localCsys=Cylindrical1)


#根据传热分析结果，创建预温度场
a = mdb.models['Model-1'].rootAssembly
region = a.sets['ALL']
mdb.models['Model-1'].Temperature(name='Predefined Field-2', 
    createStepName='Step-1', region=region, 
    distributionType=FROM_FILE, 
    fileName=FileOdbThermal, 
    beginStep=None, beginIncrement=None, endStep=None, endIncrement=None, 
    interpolate=MIDSIDE_ONLY, absoluteExteriorTolerance=0.0, 
    exteriorTolerance=0.05)

#设置输出变量，其中S为应力、LE为真实应变、U为位移、NT为节点温度
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
    'S','LE','U','NT'), frequency=LAST_INCREMENT)