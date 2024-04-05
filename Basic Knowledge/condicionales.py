#CONDICIONALES

x = int(input("Digita un numero:"))
color = "negro"
calificacion = 10

#--Ejemplo_1--
if x < 30:
    print("x es menor de 30")
elif x == 30:
    print("x es igual a 30")

else:
    print("x es mayor de 30")

#--Ejemplo_2--
if color == "rojo":
    print("puedes continuar")
elif color == "negro":
    print("puedes continuar")
else:
    print("no puede continuar")

#--Ejemplo_3--
color = "verde" if calificacion >= 6 else "rojo"
print(calificacion, color) 