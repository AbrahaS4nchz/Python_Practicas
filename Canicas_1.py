import random
import os

def probabilidad(color, canicas):
    total_canicas = 10
    return canicas[color] / total_canicas

def get_color(colores):
    return random.choice(colores)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def preguntar_salir_juego():
    while True:
        salir = input("¿Desea salir del juego? (s/n): ").lower()
        if salir == "s":
            print("Gracias por jugar!")
            exit()
        elif salir == "n":
            break
        else:
            print("[!] Opción no válida.")


def jugar_canicas(colores, canicas, total_canicas):
    while total_canicas < 10:
        for color in colores:
            num = -1
            if total_canicas != 10:
                while num > 10 - total_canicas or num < 0 :
                    try:
                        num = int(input("Cuántas canicas de color " + color + " quieres? (máximo " + str(10 - total_canicas) + "): "))
                        if num > 10 - total_canicas or num < 0:
                            print("[!] El número debe estar entre 0 y " + str(10 - total_canicas) + ".")
                        else:
                            canicas[color] = num
                    except ValueError:
                        print("[!] Por favor, introduce un número entero.5")
                        num = -1
                    if total_canicas == 10:
                        break
                total_canicas += num
            elif total_canicas == 10:
                break
    #print("canicas total : ",total_canicas)
    #clear_screen()

seguir_juego= True
while seguir_juego:
    colores = ['rojo', 'azul', 'verde', 'amarillo', 'negro', 'blanco']
    canicas = {color: 0 for color in colores}
    total_canicas=0

    jugar_canicas(colores, canicas, total_canicas)
    #print("total de canicas : {}\n".format(total_canicas))

    colores_disponibles = [color for color in colores if canicas[color] > 0]
    for color in colores_disponibles:
        prob = probabilidad(color, canicas) * 100
    #print("- Canicas de color " + color + ": " + str(canicas[color]))
        print("Probabilidad de sacar una canica de color {}: {:.2f}% (cantidad: {})".format(color, prob, canicas[color]))
    while True:
        continuar = input("¿Desea continuar jugando? (s/n): ").lower()
        clear_screen()
        if continuar == "n":
            preguntar_salir_juego()
        elif continuar == "s":
            seguir = True
            while seguir:
                color = get_color(colores_disponibles)
                prob = probabilidad(color, canicas) * 100

                print("\nHas sacado una canica de color {} (probabilidad {:.2f}%)".format(color, prob))

                seguir = input("¿Quieres seguir sacando canicas? (s/n): ") == "s"
                clear_screen()
            preguntar_salir_juego()
            break
        else:
            print("[!] Opcion no valida.")
