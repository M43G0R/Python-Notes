#LOOPS (CICLOS) 

foods = ["manzana", "peras", "uvas", "platanos"]
valores = ( (10, 20, 30), ["hola", "adios", " "], (True, False, True) )
lista = {1,2,3,4,5}
numero = 123456789
contador = 0

#--For Loop--
#---Ejemplo 1---
for food in foods:
    if food == "uvas":
        #break  #para parar el ciclo
        continue #continua el ciclo y ya no te muestra "uvas" si la validacon es true
    print(food)

#---Ejemplo 2---
for valor1, valor2, valor3 in valores:
    print(valor1, valor2, valor3)

#---Ejemplo 3---
for numero in range(1,10,2):   #del 1 hasta el 9 y la otra coma(2) seria para saltar 
    print(numero)

#---Ejemplo 4---
for indice, valor in enumerate(lista,10):  #el 10 es para que empiece el indice desde un numero que queramos
    print("indice: ", indice, "valor: ", valor)

#--While Loop--
#---Ejemplo 1---
cont = 4
while cont <= 10:
    print(cont)
    cont += 1

#---Ejemplo 2---
while numero >= 1:
    contador += 1
    numero = numero / 10
else:
    print("La cantidad de digitos del numeros es ", contador)