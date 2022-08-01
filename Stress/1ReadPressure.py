# -*- coding: mbcs -*-
################
## 读取Fluent生成的pressure和temperature数据文件
## 创建analytical field
################

#单位制转换
#Fluent默认单位:kg m  Pa  K
#Abaqus默认单位:T  mm MPa ℃
n1=1000    #m  -> mm
n2=1e-6    #Pa -> MPa
n3=-273.15 #K  -> 

#导入外部文件
#注意文本文件有5列，第1列为编号，不需要。后面的3列是x,y,z坐标，最后1列是标量值。
#因此忽略tmp[0]，从tmp[1]开始读取
datalist = []
with open(FilePres, "rb") as fp:
  for row in fp.readlines():
    tmp = row.split(",")
    try:
      datalist.append((n1*float(tmp[1]), n1*float(tmp[2]), n1*float(tmp[3]), n2*float(tmp[4])))
    except:pass

#创建静压解析场
mdb.models['Model-1'].MappedField(name='AnalyticalField-Pres', description='', 
    regionType=POINT, partLevelData=False, localCsys=None, pointDataFormat=XYZ, 
    fieldDataType=SCALAR, xyzPointData=datalist)
    