# -*- coding: UTF-8 -*-
from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
import numpy as np
import os

#ax=np.array([-350.35,-211.65,-207.65,-101.65,-97.65,-14.64,-12.64,42.95,43.10,54.65])
#rt=np.array([[22.5,18.5],[22.5,18.5],[22.5,14.5],[22.5,14.5],[22.5,10.5],[22.5,10.5],[22.5,8.50],[22.5,8.50],[22.35,8.35],[22.35,8.35]])

StrFile="SectionsBeam.txt"
data=np.loadtxt(StrFile,skiprows=2,encoding='utf-8-sig')
#Abaqus中的梁单元只能在xy平面内构建，轴线方向为x方向。
#后面在assembly中通过旋转，将轴线改为z向
#所以此处的节点坐标放在了ax中
ax=data[:,0]#节点坐标。
ar=data[:,1]#横截面外径R1
at=data[:,2]#横截面壁厚t=R1-R0

#设置材料
Rho=7.8e-9
EModulus=210000
Niu=0.3
GModulus=EModulus/(2*(1+Niu))

mdb.models['Model-1'].Material(name='GH4169')
mdb.models['Model-1'].materials['GH4169'].Density(table=((Rho, ), ))
mdb.models['Model-1'].materials['GH4169'].Elastic(table=((EModulus, Niu), 
    ))

#构建梁单元
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
for ii in range(len(ax)-1):
  x1=ax[ii]
  x2=ax[ii+1]
  print x1
  s.Line(point1=(x1, 0.0), point2=(x2, 0.0))
#EndFor

p = mdb.models['Model-1'].Part(name='Part-Beam', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-Beam']
p.BaseWire(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-Beam']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']

#创建横截面形状：环形
for ii in range(len(ax)):
  StrName='ProfileBeam-'+'%02d' %(ii+1)
  r=ar[ii]
  t=at[ii]
  #mdb.models['Model-1'].PipeProfile(name=StrName, r=r, t=t,formulation=THIN_WALL)
  mdb.models['Model-1'].PipeProfile(name=StrName, r=r, t=t,formulation=THICK_WALL)
##EndFor

#创建截面特性
for ii in range(len(ax)-1):
  StrSection ='SectionBeam-'+'%02d' %(ii+1)
  StrProfile ='ProfileBeam-'+'%02d' %(ii+1)
  mdb.models['Model-1'].BeamSection(name=StrSection, 
    integration=DURING_ANALYSIS, poissonRatio=0.0, profile=StrProfile, 
    material='GH4169', temperatureVar=LINEAR, consistentMassMatrix=False)
#EndFor

#梁端赋截面特性，以及方向
p = mdb.models['Model-1'].parts['Part-Beam']
e = p.edges
for ii in range(len(ax)-1):
  xmid=(ax[ii]+ax[ii+1])/2#中点坐标
  StrSection ='SectionBeam-'+'%02d' %(ii+1)
  edges =e.findAt(((xmid,0.0,0.0),))#根据中点坐标查找edges，赋截面特性
  region = regionToolset.Region(edges=edges)
  #梁横截面特性
  p.SectionAssignment(region=region, sectionName=StrSection, offset=0.0, 
     offsetType=MIDDLE_SURFACE, offsetField='', 
     thicknessAssignment=FROM_SECTION)
  #梁方向
  p.assignBeamSectionOrientation(region=region, method=N1_COSINES, n1=(0.0, 0.0, 
    -1.0))
#EndFor

#创建Assembly
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['Part-Beam']
a.Instance(name='Part-Beam', part=p, dependent=ON)
#绕-y轴旋转90°，梁沿着z轴
a = mdb.models['Model-1'].rootAssembly
a.rotate(instanceList=('Part-Beam', ), axisPoint=(0.0, 0.0, 0.0), 
    axisDirection=(0.0, -1.0, 0.0), angle=90.0)
#End

#对梁单元划分网格
p = mdb.models['Model-1'].parts['Part-Beam']
p.seedPart(size=10, deviationFactor=0.1, minSizeFactor=0.1)
p.generateMesh()

##创建求频率的step
#mdb.models['Model-1'].FrequencyStep(name='Step-1', previous='Initial', 
#    minEigen=1.0, numEigen=6)

a = mdb.models['Model-1'].rootAssembly
#梁单元的端点
v1 = a.instances['Part-Beam'].vertices
verts1=v1.findAt(((0.0,0.0,ax[-1]),))
region1=regionToolset.Region(vertices=verts1)
#实体单元的端面
region2=a.sets['BEAM2SOLID']
#创建梁与实体的耦合连接
mdb.models['Model-1'].Coupling(name='BeamSolidCoupling', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=DISTRIBUTING, 
    weightingMethod=UNIFORM, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, 
    ur2=ON, ur3=ON)