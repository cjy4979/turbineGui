# -*- coding: UTF-8 -*-
#删除不必要的分析步
del mdb.models['Model-1'].steps['Step1']#删除ANSA导出的Static
#创建传热分析步
mdb.models['Model-1'].HeatTransferStep(name='Step-1', previous='Initial', 
    response=STEADY_STATE, amplitude=RAMP)
    
#根据Analytical Filed创建热边界条件
a = mdb.models['Model-1'].rootAssembly
region = a.sets['TEMPERATURE']
mdb.models['Model-1'].TemperatureBC(name='Temperature', createStepName='Step-1', 
    region=region, fixed=OFF, distributionType=FIELD, 
    fieldName='AnalyticalField-Temp', magnitude=1.0, amplitude=UNSET)

#ANSA默认输出的单元类型是C3D8R和C3D6，修改为传热单元 DC3D6和DC3D6
elemType1 = mesh.ElemType(elemCode=DC3D8, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=DC3D6, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['PART-1']
z1 = p.elements
region =(z1, )
p.setElementType(regions=region, elemTypes=(elemType1, elemType2))

#设置输出变量，其中NT为节点温度
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
    'NT', ), frequency=LAST_INCREMENT)