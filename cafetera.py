import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

def antecedentes():
    temperatura = ctrl.Antecedent(np.arange(-10, 41, 1), 'temperatura')
    tazaSize = ctrl.Antecedent([0, 30, 60, 90, 120, 150, 200, 250, 300, 350, 400, 450], 'tazaSize')
    intensidad = ctrl.Antecedent(np.arange(1, 6, 1), 'intensidad')

    temperatura['frio'] = fuzz.trapmf(temperatura.universe, [-10, -10, 5, 17])
    temperatura['calido'] = fuzz.trimf(temperatura.universe, [10, 20, 28])
    temperatura['caluroso'] = fuzz.trapmf(temperatura.universe, [22, 30, 40, 40])

    tazaSize['pequeno'] = fuzz.trapmf(tazaSize.universe, [0, 0, 90, 180])
    tazaSize['mediano'] = fuzz.trimf(tazaSize.universe, [125, 240, 350])
    tazaSize['grande'] = fuzz.trapmf(tazaSize.universe, [300, 345, 450, 450])

    intensidad['suave'] = fuzz.trapmf(intensidad.universe, [1, 1, 2, 3])
    intensidad['medio'] = fuzz.trimf(intensidad.universe, [2, 3, 4])
    intensidad['fuerte'] = fuzz.trapmf(intensidad.universe, [3, 4, 5, 5])

    return temperatura,tazaSize,intensidad


def graficar_antecedentes(temperatura,tazaSize,intensidad):
    fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

    ax0.plot(temperatura.universe, temperatura['frio'].mf, 'b', linewidth=1.5, label='Frio')
    ax0.plot(temperatura.universe, temperatura['calido'].mf, 'g', linewidth=1.5, label='Calido')
    ax0.plot(temperatura.universe, temperatura['caluroso'].mf, 'r', linewidth=1.5, label='Caluroso')
    ax0.set_title('Temperatura ambiental')
    ax0.legend()

    ax1.plot(tazaSize.universe, tazaSize['pequeno'].mf, 'b', linewidth=1.5, label='Pequeño')
    ax1.plot(tazaSize.universe, tazaSize['mediano'].mf, 'g', linewidth=1.5, label='Mediano')
    ax1.plot(tazaSize.universe, tazaSize['grande'].mf, 'r', linewidth=1.5, label='Grande')
    ax1.set_title('Tamano de la taza (ml)')
    ax1.legend()
    print("ax0")

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

def consecuentes():
    agua = ctrl.Consequent([0, 30, 60, 90, 120, 150, 200, 250, 300, 350, 400, 450], 'agua')
    cafe = ctrl.Consequent(np.arange(0, 151, 1), 'cafe')
    leche = ctrl.Consequent(np.arange(0, 58, 1), 'leche')
    chocolate = ctrl.Consequent(np.arange(0, 15, 1), 'chocolate')
    tiempo = ctrl.Consequent(np.arange(1, 4.5, 0.5), 'tiempo')

    agua['poca'] = fuzz.trapmf(agua.universe, [0, 0, 90, 250])
    agua['media'] = fuzz.trimf(agua.universe, [125, 250, 350])
    agua['mucha'] = fuzz.trapmf(agua.universe, [250, 345, 450, 450])

    cafe['poca'] = fuzz.trapmf(cafe.universe, [0, 0, 45, 75])
    cafe['media'] = fuzz.trimf(cafe.universe, [45, 75, 100])
    cafe['mucha'] = fuzz.trapmf(cafe.universe, [75, 100, 150, 150])

    leche['poca'] = fuzz.trapmf(leche.universe, [0, 0, 14, 28])
    leche['media'] = fuzz.trimf(leche.universe, [14, 28, 42])
    leche['mucha'] = fuzz.trapmf(leche.universe, [28, 42, 57, 57])

    chocolate['poca'] = fuzz.trapmf(chocolate.universe, [0, 0, 4, 7])
    chocolate['media'] = fuzz.trimf(chocolate.universe, [4, 7, 10])
    chocolate['mucha'] = fuzz.trapmf(chocolate.universe, [7, 10, 14, 14])

    tiempo['poca'] = fuzz.trapmf(tiempo.universe, [1, 1, 1.5, 2.5])
    tiempo['media'] = fuzz.trimf(tiempo.universe, [1.5, 2.5, 3.5])
    tiempo['mucha'] = fuzz.trapmf(tiempo.universe, [2.5, 3.5, 4, 4])

    return agua,cafe,leche,chocolate,tiempo

def graficar_consecuentes(agua,cafe,leche,chocolate,tiempo):
    fig, (ax0, ax1, ax2, ax3, ax4) = plt.subplots(nrows=5, figsize=(8, 15))

    ax0.plot(agua.universe, agua['poca'].mf, 'b', linewidth=1.5, label='Poca')
    ax0.plot(agua.universe, agua['media'].mf, 'g', linewidth=1.5, label='Media')
    ax0.plot(agua.universe, agua['mucha'].mf, 'r', linewidth=1.5, label='Mucha')
    ax0.set_title('Cantidad de agua (ml)')
    ax0.legend()

    ax1.plot(cafe.universe, cafe['poca'].mf, 'b', linewidth=1.5, label='Poca')
    ax1.plot(cafe.universe, cafe['media'].mf, 'g', linewidth=1.5, label='Media')
    ax1.plot(cafe.universe, cafe['mucha'].mf, 'r', linewidth=1.5, label='Mucha')
    ax1.set_title('Cantidad de cafe (gr)')
    ax1.legend()

    ax2.plot(leche.universe, leche['poca'].mf, 'b', linewidth=1.5, label='Poca')
    ax2.plot(leche.universe, leche['media'].mf, 'g', linewidth=1.5, label='Media')
    ax2.plot(leche.universe, leche['mucha'].mf, 'r', linewidth=1.5, label='Mucha')
    ax2.set_title('Cantidad de leche (gr)')
    ax2.legend()

    ax3.plot(chocolate.universe, chocolate['poca'].mf, 'b', linewidth=1.5, label='Poca')
    ax3.plot(chocolate.universe, chocolate['media'].mf, 'g', linewidth=1.5, label='Media')
    ax3.plot(chocolate.universe, chocolate['mucha'].mf, 'r', linewidth=1.5, label='Mucha')
    ax3.set_title('Cantidad de chocolate (gr)')
    ax3.legend()

    ax4.plot(tiempo.universe, tiempo['poca'].mf, 'b', linewidth=1.5, label='Poca')
    ax4.plot(tiempo.universe, tiempo['media'].mf, 'g', linewidth=1.5, label='Media')
    ax4.plot(tiempo.universe, tiempo['mucha'].mf, 'r', linewidth=1.5, label='Mucha')
    ax4.set_title('Tiempo de preparacion (min)')
    ax4.legend()

    for ax in (ax0, ax1, ax2, ax3, ax4):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()

    plt.tight_layout()
    plt.show()

def pedirTazaSize():
    flag = True
    tazaSize = 0

    while flag:
        try:
            tazaSize = int(input("Ingrese la tamaño de la taza a preparar (entre 0 y 450 ml): "))
            if tazaSize <= 450 and tazaSize >= 0:
                flag = False
            else:
                print("Valor no valido")
        except:
            print("Valor no valido")
            flag = True

    return tazaSize

def pedirTemperatura():
    flagTemp = True
    temperatura_input = 0

    while flagTemp:
        try:
            temperatura_input = int(input("Ingrese la temperatura ambiente (valores entre -10 y 40 grados celcius): "))
            if temperatura_input <= 40 and temperatura_input >= -10:
                flagTemp = False
            else:
                print("Valor no valido")
        except:
            print("Valor no valido")
            flagTemp = True

    return temperatura_input

def pedirIntensidad():
    flag = True
    intensidad = 0

    while flag:
        try:
            intensidad = int(input("Ingrese intensidad del cafe (de 1 a 5): "))
            if intensidad <= 5 and intensidad >= 1:
                flag = False
            else:
                print("Valor no valido")
        except:
            print("Valor no valido")
            flag = True

    return intensidad

def pedirPreparacion():
    flag = True
    preparacion = 0
    tipos = ['espresso', 'capuccino', 'latte', 'mokaccino']

    while flag:
        try:
            print('''
            1. Espresso
            2. Capuccino
            3. Latte
            4. Mokaccino''')
            preparacion = int(input("Indique el numero de la preparacion que desea: "))
            if preparacion <= 4 and preparacion >= 1:
                flag = False
            else:
                print("Valor no valido")
        except:
            print("Valor no valido")
            flag = True

    return tipos[preparacion - 1]

'''
temperatura.view()
tazaSize.view()
intensidad.view()
'''

temperatura,tazaSize,intensidad = antecedentes()

graficar_antecedentes(temperatura,tazaSize,intensidad)

agua,cafe,leche,chocolate,tiempo = consecuentes()

graficar_consecuentes(agua,cafe,leche,chocolate,tiempo)

'''
agua.view()
cafe.view()
leche.view()
chocolate.view()
tiempo.view()
'''

temperatura_input = pedirTemperatura()
tazaSize_input = pedirTazaSize()
intensidad_input = pedirIntensidad()
preparacion_input = pedirPreparacion()

print(preparacion_input)




espresso_rule1 = ctrl.Rule(temperatura['frio'] & tazaSize['pequeno'] & intensidad['suave'], (agua['poca'],cafe['poca'],tiempo['media']))
espresso_rule2 = ctrl.Rule(temperatura['calido'] & tazaSize['pequeno'] & intensidad['fuerte'], (agua['poca'],cafe['media'],tiempo['poca']))
espresso_rule3 = ctrl.Rule(temperatura['calido'] & tazaSize['mediano'] & intensidad['medio'], (agua['media'],cafe['poca'],tiempo['poca']))
espresso_rule4 = ctrl.Rule(temperatura['caluroso'] & tazaSize['mediano'] & intensidad['fuerte'], (agua['media'],cafe['media'],tiempo['poca']))
espresso_rule5 = ctrl.Rule(temperatura['frio'] & tazaSize['grande'] & intensidad['suave'], (agua['mucha'],cafe['media'],tiempo['media']))
espresso_rule6 = ctrl.Rule(temperatura['caluroso'] & tazaSize['grande'] & intensidad['medio'], (agua['mucha'],cafe['media'],tiempo['poca']))


espresso_ctrl = ctrl.ControlSystem([espresso_rule1, espresso_rule2, espresso_rule3,espresso_rule4,espresso_rule5,espresso_rule6])

espresso_sim = ctrl.ControlSystemSimulation(espresso_ctrl)

espresso_sim.input['temperatura'] = 18
espresso_sim.input['tazaSize'] = 250
espresso_sim.input['intensidad'] = 3

espresso_sim.compute()


print(espresso_sim.output['agua'])
agua.view(sim=espresso_sim)

print(espresso_sim.output['cafe'])
cafe.view(sim=espresso_sim)

print(espresso_sim.output['tiempo'])
tiempo.view(sim=espresso_sim)






