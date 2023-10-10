# Yo
'''
notas = [6,8,8,8,9]
suma_notas = 0 #Acumulador
cantidad_notas = 0 #Contador
for nota in notas:
    suma_notas += nota
    cantidad_notas += 1
    
promedio = suma_notas / cantidad_notas    
print('promedio: ',promedio)
'''

# Compañero    
'''
notas = [6,8,8,8,9]
suma = 0
for n in notas:
    suma += n

print("Promedio: ", suma/len(notas))
'''

# Profe
'''
notas = [6,8,8,8,9]
print('Promedio:', sum(notas)/len(notas)) #sum: suma cada elemento/len: cuenta cuantos elemento hay
'''

# Crear una coleccion de facturas y sacar el promedio
# Usar una lista para este ejercicio
# Ingresar monto por cada factura hasta que el monto sea menor o igual a 0

'''
facturas = []
suma_facturas = 0
cantidad de facturas = 0

monto = int(input('Ingrese monto de la factura: '))
while monto > 0:
    facturas.append(monto) #.append: para agregar elemento a la lista
    monto = int(input('Ingrese monto de la factura: '))

print(facturas)
'''

# Crear una coleccion de facturas y sacar el promedio
# Pedir al usuario primero el numero de facturas
# Usar una lista para este ejercicio

'''
facturas = []

cantidad_de_facturas = int(input('Ingrese cantidad de facturas: '))

for num in range(1, cantidad_de_facturas+1):
    monto = int(input(f'Ingrese el monto de la factura {num}: '))
    facturas.append(monto)
    
suma = 0 
for monto in facturas: #Tambien se puede usar la funcion sum()
    suma += monto

promedio = suma / cantidad_de_facturas
print('El promedio de las facturas es: ', promedio)
'''


