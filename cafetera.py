import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

temperatura = ctrl.Antecedent(np.arange(-10,40,1),'temperatura')
tazaSize = ctrl.Antecedent([0,30,60,90,120,150,200,250,300,350,400,450],'tasaSize')
intensidad = ctrl.Antecedent(np.arange(1,6,1),'intensidad')

temperatura['frio'] = fuzz.trapmf(temperatura.universe, [-10, -10, 5, 17])
temperatura['calido'] = fuzz.trimf(temperatura.universe, [14, 20, 26])
temperatura['caluroso'] = fuzz.trapmf(temperatura.universe, [24, 30, 40, 40])

tazaSize['pequeno'] = fuzz.trapmf(tazaSize.universe, [0, 0, 90, 180])
tazaSize['mediano'] = fuzz.trimf(tazaSize.universe, [150, 240, 330])
tazaSize['grande'] = fuzz.trapmf(tazaSize.universe, [300, 345, 450, 450])

intensidad['suave'] = fuzz.trapmf(intensidad.universe, [1, 1, 2, 3])
intensidad['medio'] = fuzz.trimf(intensidad.universe, [2, 3, 4])
intensidad['fuerte'] = fuzz.trapmf(intensidad.universe, [3, 4, 5, 5])


temperatura.view()
tazaSize.view()
intensidad.view()