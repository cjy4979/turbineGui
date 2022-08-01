# -*- coding: UTF-8 -*-
################
## 读取Fluent生成的pressure和temperature数据文件
## 创建analytical field
################

# (valuex,valuey)绕(pointx,pointy,0)逆时针旋转角度angle。实际是绕z轴旋转
def Nrotate(angle,valuex,valuey,pointx,pointy):
  valuex = np.array(valuex)
  valuey = np.array(valuey)
  nRotatex = (valuex-pointx)*math.cos(angle) - (valuey-pointy)*math.sin(angle) + pointx
  nRotatey = (valuex-pointx)*math.sin(angle) + (valuey-pointy)*math.cos(angle) + pointy
  return nRotatex, nRotatey


#单位制转换
#Fluent默认单位:kg m  Pa  K
#Abaqus默认单位:T  mm MPa ℃
n1=1000    #m  -> mm
n2=1e-6    #Pa -> MPa
n3=-273.15 #K  -> 

##导入壁面静压文本文件
##注意文本文件有5列，第1列为编号，不需要。后面的3列是x,y,z坐标，最后1列是标量值。
#DataPres=np.loadtxt(FilePres,skiprows=1,usecols=(1,2,3,4), delimiter=',' ,encoding='utf-8-sig')
#DataPres[:,0:3]=DataPres[:,0:3]*n1
#DataPres[:,3]=DataPres[:,3]*n2
#
##创建单叶片上的壁面静压analytical field
#mdb.models['Model-1'].MappedField(name='AnalyticalField-Pres', description='', 
#    regionType=POINT, partLevelData=False, localCsys=None, pointDataFormat=XYZ, 
#    fieldDataType=SCALAR, xyzPointData=DataPres)
    
#导入壁温文本文件
#注意文本文件有5列，第1列为编号，不需要。后面的3列是x,y,z坐标，最后1列是标量值。
DataTemp=np.loadtxt(FileTemp,skiprows=1,usecols=(1,2,3,4), delimiter=',' ,encoding='utf-8-sig')
DataTemp[:,0:3]=DataTemp[:,0:3]*n1
DataTemp[:,3]=DataTemp[:,3]+n3
#两列叶片的中间位置z坐标
ZCenter=(max(DataTemp[:,2])+min(DataTemp[:,2]))/2

#创建单叶片上的壁温analytical field
mdb.models['Model-1'].MappedField(name='AnalyticalField-Temp', description='', 
    regionType=POINT, partLevelData=False, localCsys=None, pointDataFormat=XYZ, 
    fieldDataType=SCALAR, xyzPointData=DataTemp)
#创建传热分析步
mdb.models['Model-1'].HeatTransferStep(name='Step-1', previous='Initial', 
    response=STEADY_STATE, amplitude=RAMP)
#mdb.models['Model-1'].CoupledTempDisplacementStep(name='Step-1', 
#    previous='Initial', response=STEADY_STATE, deltmx=None, cetol=None, 
#    creepIntegration=None, amplitude=RAMP)

a = mdb.models['Model-1'].rootAssembly
#创建热边界
region = a.sets['TEMPERATURE']
mdb.models['Model-1'].TemperatureBC(name='BC-1', createStepName='Step-1', 
    region=region, fixed=OFF, distributionType=FIELD, 
    fieldName='AnalyticalField-Temp', magnitude=1.0, amplitude=UNSET)

##创建位移边界
#region = a.sets['TIE1-S']
#mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Step-1', 
#    region=region, u1=0.0, u2=0.0, u3=0.0, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
#    amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', 
#    localCsys=None)
#region = a.sets['TIE3-S']
#mdb.models['Model-1'].DisplacementBC(name='BC-3', createStepName='Step-1', 
#    region=region, u1=0.0, u2=0.0, u3=0.0, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
#    amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', 
#    localCsys=None)
##创建静压载荷
#region = a.surfaces['PRESSURE']
#mdb.models['Model-1'].Pressure(name='Load-1', createStepName='Step-1', 
#    region=region, distributionType=FIELD, field='AnalyticalField-Pres', 
#    magnitude=1.0, amplitude=UNSET)

#创建输出变量
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
    'NT', ), frequency=LAST_INCREMENT, position=NODES)

#修改单元为传热单元
elemType1 = mesh.ElemType(elemCode=DC3D8, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=DC3D6, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['PART-1']
z1 = p.elements
pickedRegions =(z1, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))

#创建Job
mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=NumCPU, 
    numDomains=NumCPU, numGPUs=0)

#运行Job
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
mdb.jobs['Job-1'].waitForCompletion()


#删除Job
del mdb.jobs['Job-1']

#读取odb文件
File_ODB ="Job-1.odb"             
FileInput=cur_dir+ "/" +File_ODB
odb = openOdb(path = FileInput)

#温度场，Step-1的最终解
Temper= odb.steps['Step-1'].frames[-1].fieldOutputs['NT11']
#Instance
Instan =odb.rootAssembly.instances['PART-1-1']
#点集合
RefSet =odb.rootAssembly.nodeSets['TEMPERATURE']
#点集合节点
Nodes = Instan.nodes
#点集合的应力场
TemperRefSet=Temper.getSubset(region=RefSet)
#温度场数组，初始为空，第1-3列为x,y,z；第4列温度值
ListTemp0=[]
ListTemp1=[]
ListTemp =[]

#提取节点的坐标和温度
#并作循环复制
for v in TemperRefSet.values:
  CordX=float(Instan.getNodeFromLabel(v.nodeLabel).coordinates[0])
  CordY=float(Instan.getNodeFromLabel(v.nodeLabel).coordinates[1])
  CordZ=float(Instan.getNodeFromLabel(v.nodeLabel).coordinates[2])
  Tempe=float(v.data)
  ListTemp0.append((CordX,CordY,CordZ,Tempe))
  if CordZ<ZCenter:
    for i in range(1, NumR1):
    #for i in range(1, 2):
      angle=i*360.0/NumR1
      CordX1,CordY1 = Nrotate(math.radians(angle),CordX,CordY,0,0)
      ListTemp1.append((CordX1,CordY1,CordZ,Tempe))
    #EndFor
  else:
    for i in range(1, NumR2):
    #for i in range(1, 2):
      angle=i*360.0/NumR2
      CordX1,CordY1 = Nrotate(math.radians(angle),CordX,CordY,0,0)
      ListTemp1.append((CordX1,CordY1,CordZ,Tempe))
    #EndFor
  #EndIf
#EndFor

#组合温度分布
ListTemp=ListTemp0+ListTemp1

#关闭odb，否则其他job没法运行覆盖odb文件
session.odbs[FileInput].close()

#删除临时文件
File_List=glob.glob("Job-1.*")
for file in File_List:
  os.remove(file)