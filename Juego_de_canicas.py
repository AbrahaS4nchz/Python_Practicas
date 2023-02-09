import random
import os

# Lista con los colores disponibles
colores = ["Rojo", "Azul", "Verde", "Amarillo", "Naranja", "Morado"]

# Diccionario para guardar la cantidad de canicas de cada color
canicas = {color: 0 for color in colores}

# Variable para guardar el total de canicas agregadas
total_canicas = 0

# Función que devuelve un color aleatorio
def get_color():
  return random.choice(colores)

# Función que calcula la probabilidad de sacar una canica de un color
def probabilidad(color):
  if total_canicas == 0:
    return 0
  return canicas[color] / total_canicas

def preguntar_usuario(mensaje):
    """Función para manejar la entrada del usuario"""
    respuesta = input(mensaje).lower()
    return respuesta == "s"

def salir_juego():
    """Función para manejar la salida del juego"""
    print("Gracias por jugar!")
    exit()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Repetimos este proceso hasta que el usuario decida detenerlo

while True:

    # Preguntamos al usuario cuantas canicas de cada color quiere
    for color in colores:
        num = -1
        while num > 10 or num < 0:
            try:
                num = int(input("Cuantas canicas de color " + color + " quieres? (máximo 10): "))
                clear_screen()
                if num > 10 or num < 0:
                    print("[!] El número debe estar entre 0 y 10.")
                else:
                    total_canicas += num
            except ValueError:
                print("[!] Por favor, introduce un número entero.")
                num = -1
        canicas[color] = num
        
    # Limpiar pantalla despues de preguntar 
    clear_screen()

    # Imprimir el numero total de canicas
    print("El numero total de canicas son: {}\n".format(total_canicas))

  # Mostramos la probabilidad de sacar cada color
    for color in colores:
        prob = probabilidad(color) * 100
        print("Probabilidad de sacar una canica de color {}: {:.2f}% (cantidad: {})".format(color, prob, canicas[color]))
    
    seguir_juego = True
    while seguir_juego:
        continuar = input("¿Desea continuar jugando? (s/n): ").lower()
        if continuar == "n":
            while True:
                salir = input("¿Desea salir del juego? (s/n): ").lower()
                if salir == "s":
                    salir_juego()
                elif salir == "n":
                    break
                else:
                    print("[!] Opcion no valida.")
        elif continuar == "s":
            seguir_juego = False
        else:
            print("[!] Opcion no valida.")
        

print("hola")