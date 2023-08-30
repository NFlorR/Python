#Mostrar n numeros
#definimos la variable
i = 0
n = int(input("Ingrese la cantidad de numeros a mostrar1: "))

#mientras i sea menor a n, se ejecuta el ciclo. 
while i < n:
    print (i)
    i = i + 1   
#muestra i e incrementa 1. 

#mostrar nn numeros con FOR
nn = int(input("Ingrese la cantidad de numeros a mostrar2: "))

#i es la variable de control de ciclo que se INCREMENTA AUTOMATICAMENTE
for i in range (nn):
    #Mostrar el valor
    print("i: ", i)

#---------------------------------
#BUCLES CON WHILE
#Ingresamos numeros (la cantidad que indicamos) y nos devuelve cuantos son mayores a 0

#declaramos variables
conteo = 0 #contador de ciclo 
cont = 0 #contador de mayores a 0
#Ingresar cantidad de numeros e informar cuantos son mayores a 0 
n3 = int(input("Ingrese la cantidad de numeros a cargar:"))

#Se ejecuta el ciclo mientras la variable conteo sea menor a la variable cantidad
while conteo < n3:
    num = int(input("Ingrese un numero: "))
    if num > 0:
        cont = cont + 1 #cuenta mayores a 0
        conteo = conteo + 1 #incrementa la variable de control de ciclo
print("La cantidad de numeros mayores a 0 es: ", cont)

#------------------------

#Ingrese una serie de numeros que termina con cero e informe cuantos de ellos son mayores a 10.
cont = 0
num = int(input("Ingrese un numero (cero para terminar):"))
while num !=0:
        if num > 10:
                cont = cont + 1

        num = int (input ("Ingresar otro numero (o cero para terminar): "))
print("Cantidad de numeros mayores a 10 es:", cont)

#-----------------------

#BUCLES CON FOR
#Recorrer una secuencia de caracteres y mostrar sus caracteres.
secuencia = "Hola"
for car in secuencia:
     print(car)

#------------
#Cargar n numeros, calcular y mostrar la sumatoria de los números
#declaramos variable
sumatoria = 0
#ingresamos cantidad de numeros
n = int(input("Cuantos numeros procesamos?: "))
#recorremos
for i in range(n):
     num = int(input("Ingrese un numero: "))
     #sumamos
     sumatoria += num
print("La sumatoria de los numeros cargados es: ", sumatoria)


#---------------- 
#Cargar n numeros e informar si hay un numero que sea igual a un  valor clave ingresado por teclado
#declaramos variable para la busqueda
encontro = False
#ingresamos numeros
n = int(input("Ingrese cantidad de numeros: "))

#ingresamos valor clave
clave = int(input("Ingrese valor clave: "))

#recorremos
for i in range(n):
        num = int(input("Ingrese un número: "))
#verificamos si hay un numero igual
        if num == clave:
              encontro = True
              break
if encontro:
      print("Se encontro el valor clave")
else:
      print("NO se encontro el valor clave")


