'''JUEGO DEL AHORCADO'''

'''Consigna: Crear un juego interactivo de “El Ahorcado”.
El juego consiste en adivinar una palabra letra por letra antes de que se
complete un dibujo de un ahorcado.'''

'''Requisitos:
1 - El juego debe tener una lista de palabras predefinidas de las cuales se
elige una palabra aleatoriamente para que el jugador adivine.
2 - El jugador tiene un número limitado de intentos para adivinar la palabra
(por ejemplo, 6 intentos).
3 - Debe mostrar las letras adivinadas y las letras incorrectas.
4 - El juego debe verificar si la letra ingresada por el jugador está en la
palabra secreta y actualizar el estado del juego en consecuencia.
5 - El juego debe terminar cuando el jugador adivine la palabra o se quede
sin intentos.
6 - Debe mostrar un mensaje de victoria o derrota al final del juego.
7 - Opcional: debe mostrar una representación gráfica del estado actual del
ahorcado. Puedes usar arte ASCII para esto.
'''

'''
- Puedes usar una lista para llevar un registro de las letras adivinadas, una
cadena para la palabra secreta y una variable para contar los intentos
restantes.
- Puedes usar un ciclo while para controlar el flujo del juego hasta que el
jugador gane o pierda.
- Puedes permitir que el jugador ingrese letras una por una y verificar si la
letra ingresada es válida (por ejemplo, si es una sola letra y no se ha
adivinado antes).
- Puedes utilizar arte ASCII para representar el estado del ahorcado en
función de los intentos restantes.
'''

from random import choice
from grafico import mostrar_grafico

def mostrar_lista(lista):
    
    # Esta funcion toma como parametro una lista y muestra cada elemento en una misma linea

    for elemento in lista:
        print(elemento, end=' ')
    print()

print()
print('¡Bienvenido al Juego del Ahorcado!')
print('Tu objetivo es adivinar la palabra secreta que tengo preparada para ti')
print('Tienes un total de 6 intentos para adivinarla')
print('¡Buena suerte y que te diviertas!')

salir = False
while not salir:
    palabras = ['Messi', 'Maradona', 'River', 'Argentina', 'Francia', 'Mundial', 'Milei', 'Ferrari', 'Computadora', 'Python', 'Libertadores', 'Lionel', 'Camioneta', 'Futbol', 'Pelota', 'perro', 'gato', 'telefono', 'viaje', 'playa', 'amigos']
    palabra_aleatoria = choice(palabras).lower()

    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    correctas = []
    incorrectas = []

    palabra_secreta = ['_'] * len(palabra_aleatoria)

    intentos = 6
    mostrar_grafico(intentos)
    mostrar_lista(palabra_secreta)
    print()

    palabra_acertada = False
    while intentos > 0:
        letra_usuario = input('Ingrese una letra:\n-> ')
        print()
        
        if len(letra_usuario) == 1:
            if letra_usuario.isalpha():
                if letra_usuario in abecedario:
                    indice = 0
                    letra_existe = False
                    for letra in palabra_aleatoria:
                        if letra == letra_usuario:
                            letra_existe = True
                            palabra_secreta[indice] = letra_usuario
                        indice += 1

                    if letra_existe:
                        correctas.append(letra_usuario)
                    else:
                        incorrectas.append(letra_usuario)
                        intentos -=1

                    print(f'Letras correctas:')
                    mostrar_lista(correctas)
                    print(f'Letras incorrectas:')
                    mostrar_lista(incorrectas)
                    print()
                    print(f'Tienes {intentos} intentos más para descifrar la palabra')

                    mostrar_grafico(intentos)

                    mostrar_lista(palabra_secreta)
                    print()

                    abecedario.remove(letra_usuario)

                else:
                    print('¡Ups! La letra ya la habias ingresado anteriormente')
                    print('Intenta con otra letra')
                    print()
            else:
                print('Ups, creo que no ingresaste una letra valida')
                print('Ingresa por favor una letra del abecedario')
                print()
        else:
            print('Creo que ingresaste más de una letra')
            print('Por favor ingresa una única letra del abecedario')
            print()

        palabra_completa = ''.join(palabra_secreta)
        if palabra_completa == palabra_aleatoria:
            palabra_acertada = True
            break

    if palabra_acertada:
        print('¡Felicidades! Ganaste')
        print(f'La palabra secreta era: {palabra_aleatoria.capitalize()}')
        print('Lo lograste antes de que se te agotaran los intentos')
        print('¡Genial!')
        print()
    else:
        print('¡Oh no! Se te acabaron los intentos.')
        print('¡No lograste adivinar la palabra! Has perdido')
        print(f'La palabra secreta era: {palabra_aleatoria.capitalize()}')
        print()
    
    print('¿Quieres intentarlo de nuevo?')

    while not salir:
        repetir = input('ingresa SI o NO:\n-> ').lower()
        print()
        if repetir == 'si':
            print('¡Excelente elección!')
            print('¡Mucha suerte en tu nuevo intento!')
            print()
            break
        elif repetir == 'no':
            print('¡Gracias por jugar! Vuelve pronto')
            salir = True
            break
        else:
            print('Por favor, ingresa una opcion valida')

    if salir:
        break

        


