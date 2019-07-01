import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt


temperatura = ctrl.Antecedent(np.arange(-10,40,1),'temperatura')
tazaSize = ctrl.Antecedent([0,30,60,90,120,150,200,250,300,350,400,450],'tasaSize')
intensidad = ctrl.Antecedent(np.arange(1,6,1),'intensidad')

temperatura['frio'] = fuzz.trapmf(temperatura.universe, [-10, -10, 5, 17])
temperatura['calido'] = fuzz.trimf(temperatura.universe, [10, 20, 28])
temperatura['caluroso'] = fuzz.trapmf(temperatura.universe, [22, 30, 40, 40])

tazaSize['pequeno'] = fuzz.trapmf(tazaSize.universe, [0, 0, 90, 180])
tazaSize['mediano'] = fuzz.trimf(tazaSize.universe, [125, 240, 350])
tazaSize['grande'] = fuzz.trapmf(tazaSize.universe, [300, 345, 450, 450])

intensidad['suave'] = fuzz.trapmf(intensidad.universe, [1, 1, 2, 3])
intensidad['medio'] = fuzz.trimf(intensidad.universe, [2, 3, 4])
intensidad['fuerte'] = fuzz.trapmf(intensidad.universe, [3, 4, 5, 5])

'''
temperatura.view()
tazaSize.view()
intensidad.view()
'''

fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

ax0.plot(temperatura.universe, temperatura['frio'].mf, 'b', linewidth=1.5, label='Frio')
ax0.plot(temperatura.universe, temperatura['calido'].mf, 'g', linewidth=1.5, label='Calido')
ax0.plot(temperatura.universe, temperatura['caluroso'].mf, 'r', linewidth=1.5, label='Caluroso')
ax0.set_title('Temperatura ambiental')
ax0.legend()
print("ax0")

ax1.plot(tazaSize.universe, tazaSize['pequeno'].mf, 'b', linewidth=1.5, label='Pequeño')
ax1.plot(tazaSize.universe, tazaSize['mediano'].mf, 'g', linewidth=1.5, label='Mediano')
ax1.plot(tazaSize.universe, tazaSize['grande'].mf, 'r', linewidth=1.5, label='Grande')
ax1.set_title('Tamano de la taza')
ax1.legend()

ax2.plot(intensidad.universe, intensidad['suave'].mf, 'b', linewidth=1.5, label='Suave')
ax2.plot(intensidad.universe, intensidad['medio'].mf, 'g', linewidth=1.5, label='Medio')
ax2.plot(intensidad.universe, intensidad['fuerte'].mf, 'r', linewidth=1.5, label='Fuerte')
ax2.set_title('Intensidad del cafe')
ax2.legend()

for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
plt.show()