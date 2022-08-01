# -*- coding: UTF-8 -*-
rho1=rho*1e-12        # kg/m^3 => T/mm^3
E1=E*1e3              # GPa => MPa
rpm1=rpm*2*np.pi/60   # r/min => rad/s
#最小化视图
session.viewports['Viewport: 1'].minimize()

mdb.models['Model-1'].materials['GH4169'].density.setValues(table=((rho1, ), ))
mdb.models['Model-1'].materials['GH4169'].elastic.setValues(table=((E1,0.32), ))
mdb.models['Model-1'].loads['CENTRIF-1'].setValues(magnitude=rpm1)
mdb.models['Model-1'].predefinedFields['Predefined Field-2'].setValues(fileName=FileOdbThermal)