#Calcular perimetro de un triángulo
#Declaro variables
Lado1 = float(input("Ingrese lado 1:"))
Lado2 = float(input("Ingrese lado 2:"))
Lado3 = float(input("Ingrese lado 3:"))

#nos da un 0 decimal debido al float, recibe enteros y decimales.
#el tipo de dato que entrega lo define según los datos que recibe
#no se coloca coma en decimales, se coloca PUNTOS.

#Armo formula
Perimetro = Lado1+Lado2+Lado3

print('El valor del perimetro es', Perimetro)

#Promedio de temperaturas
Temp1 = float(input("Ingrese temp 1:"))
Temp2 = float(input("Ingrese temp 2:"))
Temp3 = float(input("Ingrese temp 3:"))

Promedio = (Temp1+Temp2+Temp3) // 3 
#Una barra te da decimales, dos barras enteros

print("El valor de la temperatura promedio es",int(Promedio))

# // nos da una división entera. SIN tener en cuenta los decimales
# le puedo agregar int en el print para no "ensuciar" la variable
# int nos da un valor entero

print("El valor de la temperatura promedio es",round(Promedio,2))
#Con round redondeamos a los decimales que se le indiquen




