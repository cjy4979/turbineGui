# -*- coding: UTF-8 -*-

#绘图区设置
def ViewSize():
  session.viewports['Viewport: 1'].restore()
  session.viewports['Viewport: 1'].setValues(origin=(0.0, -5.56111145019531), 
      width=150, height=120)
  session.viewports['Viewport: 1'].view.fitView()
  session.viewports['Viewport: 1'].view.setValues(nearPlane=900, 
      farPlane=1700, width=334.106, height=253.205, viewOffsetX=-19.8844, 
      viewOffsetY=-19.8844)
#EndDef

#仅显示坐标系
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(triad=ON, 
    legend=OFF, title=OFF, state=OFF, annotations=OFF, compass=OFF)
#修改渲染模式：填充，隐藏边
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    renderStyle=FILLED, visibleEdges=NONE)
#渲染梁单元
session.viewports['Viewport: 1'].odbDisplay.basicOptions.setValues(
    renderBeamProfiles=ON)
#云图设置为连续模式
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    contourStyle=CONTINUOUS,)

#读取odb文件
odb = session.openOdb(name = FileOdb)
session.viewports['Viewport: 1'].setValues(displayedObject=odb)

ViewSize()

#显示变形后云图
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))

frame = odb.steps['Step-2'].frames
#输出频率的文本文件
f = open('AbaqusOutput.txt', 'w') # 打开文件， 用'w'重新写文件
#f = open('AbaqusOutput.txt', 'a') # 打开文件， 用'a'追加写文件
f.write('#共有%d阶固有频率(Hz):\n' %(len(frame)-1))
for i in range(1,len(frame)):
  Freq=frame[i].frequency#频率值
  f.write('%10.2f  ' %(Freq)) # 将各阶固有频率写文本文件
  session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=i)
  StrPng='Fig-Sample-Mode'+ '%02d' %i +'-Freq'+ '%.2f' %Freq +'.png'
  session.printOptions.setValues(vpDecorations=OFF)
  session.printToFile(fileName=StrPng, format=PNG, 
    canvasObjects=(session.viewports['Viewport: 1'], ))

f.write('\n')
f.close() 

session.odbs[FileOdb].close()

#判断目录是否存在
DirFig='Figs'
if not os.path.exists(DirFig):
  os.makedirs(DirFig) 
#将图片移动到目录
StrCmd='@move /y Fig*.png '+DirFig
os.system(StrCmd)
