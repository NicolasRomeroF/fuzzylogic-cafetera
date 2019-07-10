import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

def antecedentes():
    temperatura = ctrl.Antecedent(np.arange(-10, 41, 1), 'temperatura')
    tazaSize = ctrl.Antecedent([0, 30, 60, 90, 120, 150, 200, 250, 300, 350, 400, 450, 451], 'tazaSize')
    intensidad = ctrl.Antecedent(np.arange(1, 6, 1), 'intensidad')

    temperatura['frio'] = fuzz.zmf(temperatura.universe,-10, 41)
    temperatura['calido'] = fuzz.gaussmf(temperatura.universe, 18, 10)
    temperatura['caluroso'] = fuzz.smf(temperatura.universe, -11, 41)

    tazaSize['pequeno'] = fuzz.zmf(tazaSize.universe, 0, 451)
    tazaSize['mediano'] = fuzz.gaussmf(tazaSize.universe, 240, 100)
    tazaSize['grande'] = fuzz.smf(tazaSize.universe, 0, 451)

    intensidad['suave'] = fuzz.zmf(intensidad.universe, 0, 5)
    intensidad['medio'] = fuzz.gaussmf(intensidad.universe, 3, 1)
    intensidad['fuerte'] = fuzz.smf(intensidad.universe, 0, 5)

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

    agua['poca'] = fuzz.zmf(agua.universe, 90, 300)
    agua['media'] = fuzz.trimf(agua.universe, [125, 250, 350])
    agua['mucha'] = fuzz.smf(agua.universe, 200, 345)

    cafe['poca'] = fuzz.zmf(cafe.universe, 45, 76)
    cafe['media'] = fuzz.trimf(cafe.universe, [45, 75, 100])
    cafe['mucha'] = fuzz.smf(cafe.universe, 74, 100)

    leche['poca'] = fuzz.zmf(leche.universe, 14, 29)
    leche['media'] = fuzz.trimf(leche.universe, [14, 28, 42])
    leche['mucha'] = fuzz.smf(leche.universe, 27, 42)

    chocolate['poca'] = fuzz.zmf(chocolate.universe, 4, 8)
    chocolate['media'] = fuzz.trimf(chocolate.universe, [4, 7, 10])
    chocolate['mucha'] = fuzz.smf(chocolate.universe, 6, 10)

    tiempo['poca'] = fuzz.zmf(tiempo.universe, 1.5, 3.0)
    tiempo['media'] = fuzz.trimf(tiempo.universe, [1.5, 2.5, 3.5])
    tiempo['mucha'] = fuzz.smf(tiempo.universe, 2.0, 3.5)

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

def espresso(temperatura_input,tazaSize_input,intensidad_input,temperatura, tazaSize, intensidad, agua,cafe,tiempo):
    espresso_rule1 = ctrl.Rule(temperatura['frio'] & tazaSize['pequeno'] & intensidad['suave'],
                               (agua['poca'],cafe['poca'],tiempo['media']))
    espresso_rule2 = ctrl.Rule(temperatura['calido'] & tazaSize['pequeno'] & intensidad['fuerte'],
                               (agua['poca'],cafe['media'],tiempo['poca']))
    espresso_rule3 = ctrl.Rule(temperatura['calido'] & tazaSize['mediano'] & intensidad['medio'],
                               (agua['media'],cafe['poca'],tiempo['poca']))
    espresso_rule4 = ctrl.Rule(temperatura['caluroso'] & tazaSize['mediano'] & intensidad['fuerte'],
                               (agua['media'],cafe['media'],tiempo['poca']))
    espresso_rule5 = ctrl.Rule(temperatura['frio'] & tazaSize['grande'] & intensidad['suave'],
                               (agua['mucha'],cafe['media'],tiempo['media']))
    espresso_rule6 = ctrl.Rule(temperatura['caluroso'] & tazaSize['grande'] & intensidad['medio'],
                               (agua['mucha'],cafe['media'],tiempo['poca']))

    
    espresso_ctrl = ctrl.ControlSystem([espresso_rule1,espresso_rule2,espresso_rule3,espresso_rule4,espresso_rule5,espresso_rule6])
    
    espresso_sim = ctrl.ControlSystemSimulation(espresso_ctrl)

    espresso_sim.input['temperatura'] = temperatura_input
    espresso_sim.input['tazaSize'] = tazaSize_input
    espresso_sim.input['intensidad'] = intensidad_input

    espresso_sim.compute()


    print(espresso_sim.output['agua'])
    agua.view(sim=espresso_sim)

    print(espresso_sim.output['cafe'])
    cafe.view(sim=espresso_sim)

    print(espresso_sim.output['tiempo'])
    tiempo.view(sim=espresso_sim)

def capuccino(temperatura_input,tazaSize_input,intensidad_input,temperatura, tazaSize, intensidad, agua,cafe,leche,tiempo):
    capuccino_rule1 = ctrl.Rule(temperatura['frio'] & tazaSize['pequeno'] & intensidad['suave'], (agua['poca'],cafe['poca'],leche['media'],tiempo['media']))
    capuccino_rule2 = ctrl.Rule(temperatura['calido'] & tazaSize['pequeno'] & intensidad['fuerte'], (agua['poca'],cafe['media'],leche['poca'],tiempo['poca']))
    capuccino_rule3 = ctrl.Rule(temperatura['calido'] & tazaSize['mediano'] & intensidad['medio'], (agua['media'],cafe['media'],leche['media'],tiempo['media']))
    capuccino_rule4 = ctrl.Rule(temperatura['caluroso'] & tazaSize['mediano'] & intensidad['fuerte'], (agua['media'],cafe['media'],leche['poca'],tiempo['poca']))
    capuccino_rule5 = ctrl.Rule(temperatura['calido'] & tazaSize['grande'] & intensidad['suave'], (agua['mucha'],cafe['poca'],leche['media'],tiempo['media']))
    capuccino_rule6 = ctrl.Rule(temperatura['frio'] & tazaSize['grande'] & intensidad['fuerte'], (agua['mucha'],cafe['media'],leche['poca'],tiempo['mucha']))


    capuccino_ctrl = ctrl.ControlSystem([capuccino_rule1, capuccino_rule2, capuccino_rule3,capuccino_rule4,capuccino_rule5,capuccino_rule6])

    capuccino_sim = ctrl.ControlSystemSimulation(capuccino_ctrl)

    capuccino_sim.input['temperatura'] = temperatura_input
    capuccino_sim.input['tazaSize'] = tazaSize_input
    capuccino_sim.input['intensidad'] = intensidad_input

    capuccino_sim.compute()


    print(capuccino_sim.output['agua'])
    agua.view(sim=capuccino_sim)

    print(capuccino_sim.output['cafe'])
    cafe.view(sim=capuccino_sim)

    print(capuccino_sim.output['tiempo'])
    tiempo.view(sim=capuccino_sim)
    print(capuccino_sim.output['leche'])
    leche.view(sim=capuccino_sim)

def latte(temperatura_input,tazaSize_input,intensidad_input,temperatura, tazaSize, intensidad, agua,cafe,leche,tiempo):
    latte_rule1 = ctrl.Rule(temperatura['frio'] & tazaSize['pequeno'] & intensidad['suave'], (agua['poca'],cafe['poca'],leche['media'],tiempo['media']))
    latte_rule2 = ctrl.Rule(temperatura['caluroso'] & tazaSize['pequeno'] & intensidad['medio'], (agua['poca'],cafe['poca'],leche['poca'],tiempo['poca']))
    latte_rule3 = ctrl.Rule(temperatura['calido'] & tazaSize['mediano'] & intensidad['medio'], (agua['media'],cafe['media'],leche['media'],tiempo['poca']))
    latte_rule4 = ctrl.Rule(temperatura['caluroso'] & tazaSize['mediano'] & intensidad['fuerte'], (agua['media'],cafe['mucha'],leche['poca'],tiempo['poca']))
    latte_rule5 = ctrl.Rule(temperatura['frio'] & tazaSize['grande'] & intensidad['fuerte'], (agua['mucha'],cafe['mucha'],leche['poca'],tiempo['mucha']))
    latte_rule6 = ctrl.Rule(temperatura['calido'] & tazaSize['grande'] & intensidad['suave'], (agua['mucha'],cafe['poca'],leche['mucha'],tiempo['media']))


    latte_ctrl = ctrl.ControlSystem([latte_rule1, latte_rule2, latte_rule3,latte_rule4,latte_rule5,latte_rule6])

    latte_sim = ctrl.ControlSystemSimulation(latte_ctrl)

    latte_sim.input['temperatura'] = temperatura_input
    latte_sim.input['tazaSize'] = tazaSize_input
    latte_sim.input['intensidad'] = intensidad_input

    latte_sim.compute()


    print(latte_sim.output['agua'])
    agua.view(sim=latte_sim)

    print(latte_sim.output['cafe'])
    cafe.view(sim=latte_sim)

    print(latte_sim.output['tiempo'])
    tiempo.view(sim=latte_sim)
    print(latte_sim.output['leche'])
    leche.view(sim=latte_sim)

def mokaccino(temperatura_input,tazaSize_input,intensidad_input,temperatura, tazaSize, intensidad, agua,cafe,leche,chocolate,tiempo):
    latte_rule1 = ctrl.Rule(temperatura['calido'] & tazaSize['pequeno'] & intensidad['fuerte'], (agua['poca'],cafe['media'],leche['poca'],chocolate['poca'],tiempo['poca']))
    latte_rule2 = ctrl.Rule(temperatura['caluroso'] & tazaSize['pequeno'] & intensidad['suave'], (agua['poca'],cafe['poca'],leche['media'],chocolate['poca'],tiempo['poca']))
    latte_rule3 = ctrl.Rule(temperatura['frio'] & tazaSize['mediano'] & intensidad['medio'], (agua['media'],cafe['media'],leche['media'],chocolate['poca'],tiempo['media']))
    latte_rule4 = ctrl.Rule(temperatura['caluroso'] & tazaSize['mediano'] & intensidad['fuerte'], (agua['media'],cafe['media'],leche['poca'],chocolate['poca'],tiempo['poca']))
    latte_rule5 = ctrl.Rule(temperatura['frio'] & tazaSize['grande'] & intensidad['fuerte'], (agua['mucha'],cafe['media'],leche['media'],chocolate['poca'],tiempo['mucha']))
    latte_rule6 = ctrl.Rule(temperatura['calido'] & tazaSize['grande'] & intensidad['suave'], (agua['mucha'],cafe['poca'],leche['media'],chocolate['poca'],tiempo['media']))


    latte_ctrl = ctrl.ControlSystem([latte_rule1, latte_rule2, latte_rule3,latte_rule4,latte_rule5,latte_rule6])

    latte_sim = ctrl.ControlSystemSimulation(latte_ctrl)

    latte_sim.input['temperatura'] = temperatura_input
    latte_sim.input['tazaSize'] = tazaSize_input
    latte_sim.input['intensidad'] = intensidad_input

    latte_sim.compute()


    print(latte_sim.output['agua'])
    agua.view(sim=latte_sim)

    print(latte_sim.output['cafe'])
    cafe.view(sim=latte_sim)

    print(latte_sim.output['tiempo'])
    tiempo.view(sim=latte_sim)
    print(latte_sim.output['leche'])
    leche.view(sim=latte_sim)

temperatura,tazaSize,intensidad = antecedentes()
'''
temperatura.view()
tazaSize.view()
intensidad.view()
'''

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

if(preparacion_input=="espresso"):
    espresso(temperatura_input,tazaSize_input,intensidad_input,temperatura,tazaSize,intensidad,agua,cafe,tiempo)
elif(preparacion_input=="capuccino"):
    capuccino(temperatura_input,tazaSize_input,intensidad_input,temperatura,tazaSize,intensidad,agua,cafe,leche,tiempo)
elif(preparacion_input=="latte"):
    latte(temperatura_input,tazaSize_input,intensidad_input,temperatura,tazaSize,intensidad,agua,cafe,leche,tiempo)
elif(preparacion_input=="mokaccino"):
    mokaccino(temperatura_input,tazaSize_input,intensidad_input,temperatura,tazaSize,intensidad,agua,cafe,leche,chocolate,tiempo)