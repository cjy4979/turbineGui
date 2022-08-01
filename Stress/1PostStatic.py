# -*- coding: UTF-8 -*-

#读取odb文件
odb = openOdb(path = FileOdbStatic)

#切换visualization
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
#report设置打印total和minmax关闭
session.fieldReportOptions.setValues(printTotal=OFF, printMinMax=OFF)
#report导出所有节点：节点号,L11,L22,L33,L12,L13,L23,SMises。保存文件为abaqus.rpt
session.writeFieldReport(fileName='abaqus.rpt', append=OFF, 
    sortItem='Node Label', odb=odb, step=0, frame=1, outputPosition=NODAL, 
    variable=(('LE', INTEGRATION_POINT, ((COMPONENT, 'LE11'), (COMPONENT, 
    'LE22'), (COMPONENT, 'LE33'), (COMPONENT, 'LE12'), (COMPONENT, 'LE13'), (
    COMPONENT, 'LE23'), )), ('S', INTEGRATION_POINT, ((INVARIANT, 'Mises'), )), 
    ), stepFrame=SPECIFY)
#重新读入abaqus.rpt。跳过前22行的注释，忽略第1列的节点编号
data = np.loadtxt("abaqus.rpt", dtype=float, skiprows=22, usecols=(1,2,3,4,5,6,7))
#LE应变分量
L11=data[:,0]
L22=data[:,1]
L33=data[:,2]
L12=data[:,3]
L13=data[:,4]
L23=data[:,5]
#Miese应力
S=data[:,6]

#Miese等效应力最大值
S_MisesMax=np.max(S)
#Miese等效应变
LEMises=((L11-L22)**2+(L22-L33)**2+(L33-L11)**2+(L12**2+L13**2+L23**2)*6)*2/9
#Miese等效应变最大值
LEMisesMax=np.max(np.sqrt(LEMises))

#print S_MisesMax,LEMisesMax

#保存文件为
f = open(FileOutStatic, 'w') # 打开文件， 用'w'写文件
f.write('#最大Miese应力(MPa)   最大Miese应变 \n')
f.write('%10.8e %10.8e \n' %(S_MisesMax,LEMisesMax))
f.close() 