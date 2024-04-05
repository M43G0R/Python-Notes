#DICTIONARIES 

#es un conjunto de datos, se parece a un archivo json  

#Ejemplo 1
producto = {
    "Name": "book",
    "Cantidad": 3,
    "precio": 200
}

#Ejemplo 2
persona = {
    "nombre": "juan",
    "apellido": "hernandez"
}

#Diccionario vacio
diccionario = {}

#Para imprimir los metodos que tiene el diccionario, podemos hacer esto
print(dir(producto))

#Para imprimir el lo que tiene el diccionario es asi
print(producto)

#Para imprimir un dato especifico
print(persona["nombre"])

#Para eliminar una llave en especifico con su valor
del producto["Name"]
print(producto)

#Para ver si un dato esta en el diccionario, podemos usar "in"
print("z" in persona)
#Ó tambien esta la opcion de usar .get
print(persona.get("Hola", "Not found"))


#Tambien se puede llenar un diccionario por pasos y juntarlo en una misma funcion
opcion1 = input("Dame el nombre de la key")
opcion2 = int(input("Que valor le quieres dar: "))
#Aqui ya juntamos las preguntas (key + value) y lo asignamos a un dictionary
resultado = diccionario.setdefault(opcion1,opcion2)