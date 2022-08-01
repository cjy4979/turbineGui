# -*- coding: UTF-8 -*-

#修改static分析步，增加大变形，方便传递应力到频率分析步
mdb.models['Model-1'].steps['Step-1'].setValues(nlgeom=ON)

#设置输出变量，其中S为应力、LE为真实应变、U为位移、NT为节点温度
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
    'S','NT',), frequency=LAST_INCREMENT)

##创建频率分析步：Lanczos方法求固有频率
#mdb.models['Model-1'].FrequencyStep(name='Step-2', previous='Step-1',
#    normalization=MASS, minEigen=FreqMin,maxEigen=FreqMax, numEigen=FreqNum, eigensolver=LANCZOS, 
#    simLinearDynamics=OFF)

#创建频率分析步：AMS方法求固有频率
mdb.models['Model-1'].FrequencyStep(name='Step-2', previous='Step-1', simLinearDynamics=ON,
    normalization=MASS,numEigen=FreqNum, minEigen=FreqMin, maxEigen=FreqMax,
    eigensolver=AMS, acousticCoupling=AC_OFF)

#抑制Shell2SolidTie（该Tie是热分析中替换Shell2Solid Coupling）
mdb.models['Model-1'].constraints['SHELL2SOLIDTIE2-1'].suppress()
mdb.models['Model-1'].constraints['SHELL2SOLIDTIE1-1'].suppress()

#将梁、壳、实体组合为一个ALL集合，用于定义温度场和离心载荷
a=mdb.models['Model-1'].rootAssembly
a.SetByBoolean(name='ALL', sets=(a.allInstances['PART-1-1'].sets['SHELLDISK'], 
    a.allInstances['PART-1-1'].sets['SOLID'], 
    a.allInstances['Part-Beam'].sets['Beam'], ))

#根据传热分析结果，创建温度场
region = a.sets['ALL']
#初始预温度为20摄氏度
mdb.models['Model-1'].Temperature(name='Predefined Field-1', 
    createStepName='Initial', region=region, distributionType=UNIFORM, 
    crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, magnitudes=(30.0, ))
#施加温度场
mdb.models['Model-1'].Temperature(name='Predefined Field-2', 
    createStepName='Step-1', region=region, 
    distributionType=FROM_FILE, 
    fileName=FileOdbThermal, 
    beginStep=None, beginIncrement=None, endStep=None, endIncrement=None, 
    interpolate=MIDSIDE_ONLY, absoluteExteriorTolerance=0.0, 
    exteriorTolerance=0.05)

#施加离心载荷
region = a.sets['ALL']
RPM=18600.0
Omega=2.0*math.pi*RPM/60.0
mdb.models['Model-1'].RotationalBodyForce(name='Load-1', 
    createStepName='Step-1', region=region, magnitude=Omega, centrifugal=ON, 
    rotaryAcceleration=OFF, point1=(0.0, 0.0, 0.0), point2=(0.0, 0.0, 10.0))
    
#将梁单元距离轮盘的远端点设置为固定边界条件
region = a.instances['Part-Beam'].sets['Beam']
mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='Initial', 
    region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0, 
    amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', 
    localCsys=None)