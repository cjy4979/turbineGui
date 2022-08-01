# -*- coding: UTF-8 -*-

StrFile="SectionsShell.txt"
DataShell=np.loadtxt(StrFile,skiprows=1,encoding='utf-8-sig')

#局部圆柱坐标系的原点z坐标
Z0=DataShell[0]
#创建局部圆柱坐标系
a = mdb.models['Model-1'].rootAssembly
Csys=a.DatumCsysByThreePoints(name='Csys-Cylindrical', coordSysType=CYLINDRICAL, 
    origin=(0.0, 0.0, Z0), point1=(Z0, 0.0, Z0), point2=(Z0, Z0, Z0))
CsysID=Csys.id#提取局部圆柱坐标系编号

#壳厚度计算参数（局部圆柱坐标系）
#转换为字符串
R1='%f' %DataShell[1]#内径     
Z1='%f' %DataShell[2]#内径壳厚度
R2='%f' %DataShell[3]#外径     
Z2='%f' %DataShell[4]#外径壳厚度
#R1=28.48   Z1=20.47      R2=74.91   Z2=13.09

#壳厚度分布名称
StrShellThick='AnalyticalField-ShellThick'
#壳厚度分布表达式
Str0='(R-'+R1 +')/('+ R2+'-'+ R1+')*('+Z2 +'-'+Z1+')+'+Z1
#Z=(R-R1)/(R2-R1)*(Z2-Z1)+Z1
#(R-28.48)/(74.91-28.48)*(13.09-20.47)+20.47  

#根据之前提取的局部坐标系编号，选择局部坐标系
datum = mdb.models['Model-1'].rootAssembly.datums[CsysID]
#构建壳厚度分布的解析表达式
mdb.models['Model-1'].ExpressionField(name=StrShellThick, 
    localCsys=datum, description='', expression=Str0)

#修改壳单元的section设置
mdb.models['Model-1'].sections['Section-2-SHELLDISK'].setValues(
    preIntegrate=OFF, material='GH4169', thickness=0.0, 
    thicknessType=NODAL_ANALYTICAL_FIELD, 
    nodalThicknessField=StrShellThick, 
    idealization=NO_IDEALIZATION, integrationRule=SIMPSON, numIntPts=5)
