#Estructuras Condicionales

#Verificar que un divisor sea diferente de cero.
#Ingresar datos
num = int(input("Ingrese numerador:"))
den = int(input("Ingrese denominador:"))

if den == 0:

    print("No se puede dividir por cero!")

else:
    division = num/den
    print('resultado', division)

#Carga dos numeros por teclado y muestra el mayor. 
A = int(input("Ingrese el valor de A: "))
B = int(input("Ingrese el valor de B: 1"))

if A > B:
    mayor = A
    print("El mayor es:", mayor)

else:
    mayor = B
    print("El mayor es:", mayor)

#Carga tres numeros por teclado y mostrar el mayor
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))
if a > b and a > c:
    may = a 

elif b > c:
    may = b

else:
    may = c

print ("El mayor es ", may)

