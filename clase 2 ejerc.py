#Calcular el area de un triangulo, cargando el valor de la base y sabiendo que su altura es igual al cuadrado de la base.
base = float(input("Ingrese el valor de la base: "))
altura = base ** 2
area = base * altura / 2 
#le agrego el int para que me de entero
print("El area del triangulo es: ", int(area))

#Un vehículo parte de la ciudad de Córdoba y se dirige a Buenos Aires por autopista. La distancia aproximada
#entre ambas ciudades es de 800 kilómetros. El vehículo se desplaza con velocidad promedio de 122 km/h.
#Desarrolle un programa que calcule el tiempo total en horas que demorará ese vehículo en llegar a Buenos
#Aires. 

distancia = 800
velocidad = 122
tiempo = distancia / velocidad

print ("El tiempo que demorará es de: ", round(tiempo,2), "horas")

#Leer dos números y calcular: La suma de sus cuadrados. El promedio de sus cubos.
numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))

cuadrado = (numero1 * 2) + (numero2 * 2)
print ("La suma de los cuadrados es: ", cuadrado)

promedioDeCubos = (numero1 * 3) + (numero2 * 3) / 2
print ("El promedio de sus cubos es:", promedioDeCubos)

#Conociendo el precio de lista de un articulo, determinar: Precio de venta al contado (5% de descuento)
#Precio de venta con tarjeta (10% de recargo)

precioDeLista = float(input("Ingresar precio de lista: "))

precioDeVentaCont = print("Precio al contado: ", int(precioDeLista * 0.95))
precioDeVentaTarj = print("Precio con Tarjeta: ", int(precioDeLista * 1.10))

#Calcular el descuento y el monto a pagar por un medicamento en una farmacia
#Todos los medicamentos tienen un descuento del 5%. 
#Mostrar precio actual, monto de descuento y monto final a pagar

precioDeMedicamento = float(input("Ingresar precio del medicamento: "))
print("Precio del medicamento: ", precioDeMedicamento)

descuento = 0.05
print("Monto de descuento: ", precioDeMedicamento * descuento)

montoFinal = precioDeMedicamento - descuento 
print("Monto final a pagar: ", montoFinal)



