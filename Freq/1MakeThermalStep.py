# -*- coding: UTF-8 -*-

#删除不必要的分析步
del mdb.models['Model-1'].steps['Step-1']#删除ANSA导出的Static
##创建传热分析步
mdb.models['Model-1'].HeatTransferStep(name='Step-1', previous='Initial', 
    response=STEADY_STATE, amplitude=RAMP)

###创建传热-应力耦合分析步
#mdb.models['Model-1'].CoupledTempDisplacementStep(name='Step-1', 
#    previous='Initial', response=STEADY_STATE, deltmx=None, cetol=None, 
#    creepIntegration=None, amplitude=RAMP, nlgeom=ON)
#
##创建频率分析步
#mdb.models['Model-1'].FrequencyStep(name='Step-2', previous='Step-1', 
#    minEigen=100.0, numEigen=20)

##设置输出变量，其中NT为节点温度
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
    'NT', ), frequency=LAST_INCREMENT)

#创建整圈叶片的温度分布Analytical Filed
mdb.models['Model-1'].MappedField(name='AnalyticalField-Temp', description='', 
    regionType=POINT, partLevelData=False, localCsys=None, pointDataFormat=XYZ, 
    fieldDataType=SCALAR, xyzPointData=ListTemp)

#根据Analytical Filed创建热边界条件
a = mdb.models['Model-1'].rootAssembly
region = a.sets['TEMPERATURE']
mdb.models['Model-1'].TemperatureBC(name='Temperature', createStepName='Step-1', 
    region=region, fixed=OFF, distributionType=FIELD, 
    fieldName='AnalyticalField-Temp', magnitude=1.0, amplitude=UNSET)

#修改单元类型
p = mdb.models['Model-1'].parts['PART-1']
#ANSA默认输出的实体单元类型是C3D8R和C3D6，修改为传热单元 DC3D8和DC3D6
elemType1 = mesh.ElemType(elemCode=DC3D8, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=DC3D6, elemLibrary=STANDARD)
z1 = p.sets['SOLID'].elements
pickedRegions =(z1, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))

#ANSA默认输出的壳单元类型是S3和S4，修改为传热单元 DS3和DS4
elemType1 = mesh.ElemType(elemCode=DS4, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=DS3, elemLibrary=STANDARD)
z1 = p.sets['SHELLDISK'].elements
pickedRegions =(z1, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))

##ANSA默认输出的梁单元类型是B31，修改为传热单元DC1D2
#elemType1 = mesh.ElemType(elemCode=DC1D2, elemLibrary=STANDARD)
#p = mdb.models['Model-1'].parts['Part-Beam']
#e = p.edges
#edges = e
#pickedRegions =(edges, )
#p.setElementType(regions=pickedRegions, elemTypes=(elemType1, ))

#Shell to Solid 定义的edge based surface 集合，不适用于传热分析，需要删除
mdb.models['Model-1'].rootAssembly.deleteSurfaces(surfaceNames=(
    'SHELL2SOLID1-1', 'SHELL2SOLID2-1', ))
#同时删除对应的shell to solid coupling，后面静强度计算，重新读取文件，并使用shell to solid
mdb.models['Model-1'].constraints.delete(('SHELL2SOLID1-1', 
    'SHELL2SOLID2-1', ))
