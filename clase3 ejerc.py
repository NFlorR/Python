#Leer una serie de numeros enteros que contenga como maximo veinte elementos. 
#En caso de ingresar un valor negativo o la cantidad de numeros ingresados supere los veinte, detener el proceso e informar mediante un mensaje cuantos son mayores a 100

n = int(input("Ingrese cantidad de numeros: "))

for i in range(n):
     masCien = n > 100
     num = int(input("Ingrese un numero: "))
     if n > 20 or num < 0:
        print("Numeros mayores a 100: ", masCien)


