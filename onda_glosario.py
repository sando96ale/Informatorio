'''VARIABLES'''
variable = 1
print(type(variable)) #Para saber que tipo de dato es

VARIABLE_MESSI = 10 # En mayuscula una variable constante

'''ENTEROS'''
variable = 1 #Definir una variable
variable = int(variable) #Lo transforma a entero

'''FLOTANTES O DECIMALES'''
variable3 = 3,978
variable3 = float(variable3) #Lo transforma a decimal
variable3 = round(variable3, 2) #round redondea la parte decimal a la cantidad que queramos

'''STRING O CADENA DE CARACTERES'''
variable4 = 'Hola Alexis'
variable4 = variable4.upper() # upper Transforma la cadena en MAYUSCULA
variable4 = variable4.lower() # lower Transforma la cadena en MINUSCULA
variable4.capitalize() # capitalize pone la primera letra en mayuscula
variable4.strip() # strip elimina los espacios al principio y al final
variable4.replace('a', 'o') # remplaza una letra por otra por ejemplo, la a por la o
variable4 = str(variable4) # str Lo transforma a string
print(len(variable4)) # len para saber la longitud de una cadena
variable4.count('Hola') # count sirve para saber cuantas veces aparece un elemento
longitud = len(variable4) # Para saber la longitud de una cadena
variable4.isalpha() # Verifica si toda la cadena son letras del alfabeto
variable4 in 'aeiou'# IN sirve para verificar si esa variable se encuentra en una cadena

'''BOOLEANOS''' '''True o False'''

'''OPERADORES''' 
# suma: +, resta: -, Division retorna flotante: /, Division retorna entero: //, multiplicacion: *
# Retorna el resto de la division: %, Potencia: **
# <, <=, >, >=, ==, !=, and, or, not

'''Funciones que viene con Python'''
print(1,end="") # Sirve para especificar lo que debe aparecer al final de la cadena impresa
def mi_funcion1(a,b): # _doc_ sirve para imprimir el docstring que esta en la funcion
    c = a + b
    '''Funcion'''
    
print(mi_funcion1.__doc__)

'''CONDICIONALES''' '''IF ELIF ELSE'''
if variable > variable3: # Esto es SI condicion :
    print('Alexis')
    
elif variable < variable3:
    print()
    
else: # Esto es
    print('Sandoval')
    
'''LISTAS'''
mi_lista = [1,2,3,'Alexis','Sandoval'] #Como crear una lista
mi_lista1 = [4,5,6,'Emanuel']
mi_lista_range = list(range(1, 11)) # Asi tambien se puede crear una lista de numeros 

for i, elemento in enumerate(mi_lista, start = 1): # enumerate sirve para dar un indice a cada elemento de la lista, tupla, cadena, 
    pass                                           # y start para definir en que indice comienza

print(mi_lista[1]) # Como acceder a los elementos de una lista, comienza del [0], y acceder al ultimo elemento: [-1]
print(mi_lista[1:4]) # Acceder a un rango especifico de la lista
print(mi_lista[::-1]) # Imprime la lista en orden inverso
mi_lista[2] = 1 # Como modificar un elemento
del mi_lista[2] # Como eliminar un elemento
mi_lista.count('Alexis') # count sirve para saber cuantas veces aparece un elemento
mi_lista.index('Alexis',1,3) # index en que ubicacion esta el elemento, se le puede poner el inicio y el fin de la busqueda
variable6 = mi_lista.pop([2]) # Quita el elemento de a lista y lo retorna el valor
mi_lista.append(3.11) # Agrega elementos a la lista
mi_lista2 = mi_lista.extend(mi_lista1) # Agrega los elemento de una lista a la otra
mi_lista.insert(2,'Billarreal') # Agrega un elemento en un posicion especifica
mi_lista.remove(2) # Elimina la primera posicion de la lista
mi_lista.clear() # Elimina todos los elementos de la lista
mi_lista.reverse() # Invierte el orden de los elementos
cadena = ' '.join(mi_lista) # Convierte los elementos de una secuencia iterable en una cadena.
mi_lista3 = list(reversed(mi_lista)) # Para que no se modifique la lista original
copia_mi_lista = mi_lista.copy() # Una copia de la lista original
mi_lista4 = sorted(mi_lista, key=str.lower, reverse=False) # Ordena los elementos, False: Menor a mayor, True: de Mayor a menor
# Key: str.lower: Para convertir todo en minuscula y ordenarlo alfabeticamente
# Key: len: Ordena por longitud
longitud = len(mi_lista) # Para saber la longitud de la lista
nueva_lista = list('mi_diccionario.keys()') # Convertir en una lista, por ejemplo las claves de un diccionario
lista_numeros_enteros = [int(numero) for numero in mi_lista] # Para transformar los elementos de la lista en enteros

'''TUPLAS''' # Inmutables
mi_tupla = (1,2,3,5,'Azul','Rojo') #Como crear una tupla

print(mi_tupla[1]) # Para acceder a un elemento de la tupla
mi_tupla.count('Azul') # count sirve para saber cuantas veces aparece un elemento
mi_tupla.index('Azul') # index sirve para saber en que ubicacion esta ese elemento
longitud = len(mi_tupla) # Para saber la longitud de una tupla
a,b,c,d,e,f = mi_tupla # Desempaquetar los elemento en una variable

'''DICCIONARIOS'''
mi_diccionario = {'num1':1, 'num2':2, 'num3':3} #Como crear una lista

mi_diccionario['num1'] # Acceder a los elementos de un diccionario
mi_diccionario['num1'] = 4 # Modificar un elemento, Para agregar uno nuevo es de la misma forma
mi_diccionario.setdefault('num4', 4)
mi_diccionario.clear() # Elimina todos los elementos del diccionario
mi_diccionario.copy() # Hace una copia del diccionario
mi_diccionario.get() # Para acceder a un valor del diccionario, y si no esta no da error
mi_diccionario.keys() # Para ver todas las claves que hay en el diccionario
mi_diccionario.values() # Para ver todos los valores que hay en un diccionario
mi_diccionario.pop() # Elimina y devuelve el valor asociado a la clave dada
mi_diccionario.popitem() # Elimina y devuelta clave:valor aleatorio
mi_diccionario.setdefault() # Devuelve el valor de una clave dada, o creo la crea con un valor predeterminado si no esta
mi_diccionario.update({'clave': 'valor'}) # update sirve para agregar un elemento a la lista
longitud = len(mi_diccionario) # Para saber la longitud de un diccionario
cadena = ' '.join(mi_tupla) # Convierte los elementos de una secuencia iterable en una cadena.

for clave in mi_diccionario: # Para recorrer los elementos de un diccionario 
    print(f'La clave es: {clave}')
    print(f'Su valor es: {mi_diccionario[clave]}')

for clave, valor in mi_diccionario.items(): # items sirve para mostrar cada clave: valor que hay en un diccionario de forma de tupla
    print(clave, ':', valor)

mi_diccionario['clave'] = 'valor' #Agregar elementos a un diccionario

'num1' in mi_diccionario #Para verificar si la clave se encuentra en el diccionario
del mi_diccionario['num1'] # Para eliminar una clave:valor de un diccionario
variable5 = mi_diccionario.pop('num1') # Quita el elemento del diccionario y lo retorna el valor

'''SETS'''
mi_set = {1,2,3,4,5,'Alexis','Emanuel'} #Como crear un set
mi_set1 = {6,7,8,'Sandoval'}

mi_set.add('Sandoval') # Agregar elemento al set
mi_set.remove('Sandoval') # Eliminar un elemento del set
mi_set.discard('Billarreal') # Para eliminar, pero si no esta el elemento no tira error
mi_set.pop() # Eliminar un elemento aleatoriamente
mi_set.clear() # Elimina todos los elementos del set
mi_set2 = mi_set.union(mi_set1) # Une 2 conjuntos en uno nuevo
mi_set3 = mi_set.intersection(mi_set1, mi_set2) # Sirve para encontrar la interseccion entre 2 o mas conjuntos
mi_set4 = mi_set.difference(mi_set1) # La diferencia entre el mi_set - mi_set1, queda los que no estan en mi_set1
mi_set5 = mi_set.symmetric_difference(mi_set1) # Los elementos que no estan en ambos conjuntos, ellos que no se repiten
longitud = len(mi_set) # Para saber la longitud de un set
numero_mas_grande = max(mi_set) # Max sirve para mostrar el elemento mas grande la lista
mi_set_numeros = set(range(1,10,2)) # Para crear un conjunto dando los parametros que queramos

'''BUCLES'''
contador = 0 # es una variable que incrementa o decrementa por cada repeticion del bucle
acumulador = 0 # Una variable que almacena resultados de las operaciones del bucle
bandera = True # Almacena True o False, para comunicar informacion de una parte a otra

'''While''' """(Mientras)"""
# No se sabe la cantidad de veces que va a repetir, depende de la condicion que se le ponga

numero = 5
cantidad = 0
num = 0
while cantidad >= numero:
    num = num + cantidad
    cantidad += 1
    print('Todavia se puede')

a, b = b, a + b # Actualizar variable en simultaneo en una sola linea
    
# Este es un ejemplo que me costo, creo 2 variables para que una vaya creciendo y la otra decreciendo,
# Para ir comparando si las letras son iguales, si encuentra una que es distinta hace un break.
palabra = input('Por favor, ingrese una palabra y te dire si es un palindromo:\n-> ').lower()

palabra = palabra.replace(' ', '')    
izquierda = 0
derecha = len(palabra) - 1
es_palindromo = True

while izquierda < derecha:
    if palabra[izquierda] != palabra[derecha]:
        es_palindromo = False
        break
    izquierda += 1
    derecha -= 1
    
'''FOR''' """(Para)"""
#
    
for elemento in mi_diccionario: # Se ejecuta tantas veces como elementos de una lista, cadena, tupla, range, diccionario, set
    pass

for elemento in range(1,10,2): # Range controla las veces que se ejecuta el for, desde donde comienza, donde finaliza y en cuantos saltos va
    print('Hola')
    break # Se ejecuta en while y for, simplemente termina el bucle
    continue # Se regresa al comienzo del bucle, ignorando todo lo que hay abajo

for elemento in reversed(mi_lista): # Sirve para invertir una secuencia iterable
    pass

'''FUNCIONES'''

def mi_funcion(a,b): # Forma de crear una funcion, se le pasa los parametros para desde ser usada
    pass

mi_funcion(1,2) # Para llamar la funcion con argumentos, esto seria por posicion
mi_funcion(b=2,a=1) # Para llamar la funcion por nombre

def mi_funcion(*args): # Cuando queremos darle parametros indeterminados
    for arg in args:
        print(arg)

mi_funcion(1, 2, 3, 4, 5)

def mi_funcion(**kwargs): # Cuando queremos darle parametros indeterminadas que sean clave:valor
    '''Funcion'''
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')

mi_funcion(nombre='Juan', edad=30, ciudad='Madrid')

def imprimir_argumentos(*args, **kwargs): # Se puede utilizar los 2 en una misma funcion
    print("Argumentos posicionales:")
    for arg in args:
        print(arg)
    print("Argumentos de palabras clave:")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

imprimir_argumentos(1, 2, 3, nombre="Juan", edad=30)

def modificar_cadena(cadena): # Cuando se pasa los argumentos por valor, se hace una copia pero no afecta a la variable original
    cadena = cadena + " mundo"
    print(cadena)

saludo = "Hola"
modificar_cadena(saludo)
print(saludo)

def agregar_elemento(diccionario, clave, valor): # Cuando se pasa los argumentos por referencia, si hace cambios en el original
    diccionario[clave] = valor

mi_diccionario = {"nombre": "Juan", "edad": 30}
agregar_elemento(mi_diccionario, "ciudad", "Madrid")
print(mi_diccionario)  # Esto imprimirá {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}, ya que el diccionario se modifica dentro de la función

def default(var1=10, var2=5): # Definir una funcion con valores predeterminados
    return var1, var2

'''IMPORTAR MODULOS'''
import random
variable2 = random.randint(1,100) #Me da un numero aleatoreo depende de los parametros que le paso
var_max = random.randint(0, 100) # Genera un valor maximo entre 0 y 100
var_min = random.randint(-100, 0) # Genera un valor minimo entre -100 y 0
mi_lista_mezclada = random.shuffle(mi_lista) # Mezcla aleatoriamente los elementos

import datetime

fecha_actual = datetime.date.today() # Para obtener la fecha actual
tiempo_actual = datetime.datetime.now() # Para obtener la fecha y hora actual

import time

time.sleep(10) # Esto espera los minutos que recibe de parametros para que el bloque de codigo siga

import math

print(math.sqrt(25)) # Para calcular la raiz cuadrada
print(math.sin(math.pi/2)) # Sena de pi/2 (90 grados)
print(math.log10(100)) # Logaritmo base 10 de 100

import os

print(os.getcwd()) # Obtener el directorio del trabajo actual
os.mkdir('nuevo_directorio') # Crea un nuevo directorio

import csv

with open('datos.csv', 'r') as archivo:
    lector_csv = csv.reader(archivo)
    for fila in lector_csv:
        print(fila)

'''IMPORTAR ARCHIVOS EXTERNOS'''
from menu_completo import menu, hamburguesa #Importa archivos aparte, por ejemplo importe los menu que tengo en otro archivo para usarlos