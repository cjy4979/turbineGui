# -*- coding: UTF-8 -*-

session.viewports['Viewport: 1'].restore()
session.viewports['Viewport: 1'].setValues(origin=(0.0, -8.25), 
    width=150, height=120)

#隐藏title、state、annotations、compass
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    title=OFF, state=OFF, annotations=OFF, compass=OFF)

#进入contour
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
#设置渲染方式
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    renderStyle=FILLED,visibleEdges=NONE)
#连续类型渲染
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    contourStyle=CONTINUOUS,)

#单一叶片
session.viewports['Viewport: 1'].odbDisplay.basicOptions.setValues(
    patternNumCircular=1)

#旋转
session.viewports['Viewport: 1'].view.setValues(nearPlane=180.273, 
    farPlane=291.921, width=84.4809, height=60.4747, cameraPosition=(185.741, 
    169.855, 189.801), cameraUpVector=(0.70438, -0.574765, -0.416526), 
    cameraTarget=(82.5034, -3.24312, 63.8999))

session.viewports['Viewport: 1'].view.fitView()

#移动
session.viewports['Viewport: 1'].view.setValues(nearPlane=155.537, 
    farPlane=294.958, width=101.649, height=76.7618, viewOffsetX=-11)

#保存图片格式
session.printOptions.setValues(vpDecorations=OFF)
session.pngOptions.setValues(imageSize=(1096, 826))

#应力云图legend
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    legendNumberFormat=FIXED,legendDecimalPlaces=1,legendBox=OFF)
#应力云图
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
#保存图片
session.printToFile(fileName=FigS1, 
    format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))
    
#位移云图legend
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    legendNumberFormat=FIXED,legendDecimalPlaces=3,legendBox=OFF)
#位移云图
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
#保存图片
session.printToFile(fileName=FigU1, 
    format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))
    
#应变云图legend
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    legendNumberFormat=FIXED,legendDecimalPlaces=6,legendBox=OFF)
#应变云图
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='LE', outputPosition=INTEGRATION_POINT, refinement=(
    INVARIANT, 'Mid. Principal'), )
#保存图片
session.printToFile(fileName=FigLE1, 
    format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))





#整圈叶片
session.viewports['Viewport: 1'].odbDisplay.basicOptions.setValues(
    patternNumCircular=90)
session.viewports['Viewport: 1'].view.setValues(nearPlane=509.004, 
    farPlane=936.353, cameraPosition=(-540.439, 65.5317, -407.184), 
    cameraUpVector=(0.0448358, 0.995265, 0.086244), cameraTarget=(-2.57492e-05, 
    -1.43051e-06, 68.1003))
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-500.969, 
    65.6592, -452.048), cameraTarget=(39.4704, 0.127512, 23.2366))
    

#应力云图legend
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    legendNumberFormat=FIXED,legendDecimalPlaces=1,legendBox=OFF)
#应力云图
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
#保存图片
session.printToFile(fileName=FigS2, 
    format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))
    
#位移云图legend
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    legendNumberFormat=FIXED,legendDecimalPlaces=3,legendBox=OFF)
#位移云图
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
#保存图片
session.printToFile(fileName=FigU2, 
    format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))
    
#应变云图legend
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    legendNumberFormat=FIXED,legendDecimalPlaces=6,legendBox=OFF)
#应变云图
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='LE', outputPosition=INTEGRATION_POINT, refinement=(
    INVARIANT, 'Mid. Principal'), )
#保存图片
session.printToFile(fileName=FigLE2, 
    format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))


    
