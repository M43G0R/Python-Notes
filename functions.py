#FUNCTIONS 

#Estructura basica de una funcion basica
def hola(): #el def sirve para que definir la funcion
    print("Hola, amigo")

hola() #Mandamos llamar a la funcion


#Otro ejemplo con variables
def suma (n1,n2):
    return n1 + n2

print(suma(10,30)) #Aqui le pasamos los valores de las variables

print("\n")
#------------------------------------------------------------------------------
#----------------Args-------------------
#------------------------------------------------------------------------------
#esto se puede utilizar cuando no sabes cuantos argumentos se va a utilizar
#este * se debe de poner en el ultimo parametro por ejemplo, def suma(val1, *args):
#este te agrupa los datos en una tupla
def suma(*args):
    total = 0
    for valor in args:
        total += valor
    return total

resultado = suma(10, 20, 30, 40, 50, 60, 70)
print(resultado) #Basicamente en esta funcion le decimos que sume los valores que le metemos y que nos de el resultado


#Otra forma es poner **kwargs
#este te agrupa en un diccionario
def usuarios_autenticados(**kwargs):
    print(kwargs)

usuarios_autenticados(codi=True, facilito=False) #Aqui nos dice que usuario esta auntentificados y cuales no


#Tambien puedes hacer una combinacion de estos
def combinacion(requerido, *args, **kwargs):
    print(requerido)
    print(args)
    print(kwargs)

combinacion("valor requerido", 10, 20, valor1=True, valor2=False)

print("\n")
#------------------------------------------------------------------------------
#----------------Decoradores-------------------
#------------------------------------------------------------------------------
#Los decoradores es como agregarle funciones extras a tu funcion principal

#Ejemplo 1
#Esta funcion es el decorador (es cun ejemplo)
def decorador(funcion):#El nombre del decorador debe ser normalmente muy descriptivo
    def nueva_funcion(*args,**kwargs):
        print("Podemos agregar codigo antes")
        resultado = funcion(*args,**kwargs) #Esta funcion es la que se va a decorar
        print("Podemos agregar codigo despues")
        return resultado
    return nueva_funcion

#Funcion 1
@decorador #Llamamos al decorador encima de la funcion principal
def funcion_a_decorar():
    print("Este es una funcion a decorar")

#Funcion 2
@decorador
def suma(val1,val2):
    return val1 + val2

funcion_a_decorar()

resultado = suma(10,20)
print(resultado)


#Ejemplo 2 haciendo que podamos agregarle valores extra al decorador

#Simplemente debemos agregar una funcion mas y bajar de nivel las otras
def decorador(name, number): #Podemos pedirle el numero de parametros que querramos
    def nueva_funcion(funcion): #Bajamos el paramentro funcion y podemos agregarle a la funcion 1 los parametros que querramos
        def nueva_funcion2(*args,**kwargs): #Bajamos tambien los args y los kwargs a la funcion de abajo
            print("Podemos agregar codigo antes")
            resultado = funcion(*args,**kwargs) #Esta funcion es la que se va a decorar
            print("Podemos agregar codigo despues")
            return resultado
        return nueva_funcion2
    return nueva_funcion

#Funcion 1
@decorador('Juan', 23) #Les agregamos los valores directamente aqui
def funcion_a_decorar():
    print("Este es una funcion a decorar")

#Funcion 2
@decorador('Jose', 21412)
def suma(val1,val2):
    return val1 + val2

funcion_a_decorar()

resultado = suma(10,20)
print(resultado)


print("\n")
#------------------------------------------------------------------------------
#----------------Closures-------------------
#------------------------------------------------------------------------------
#Basicamente son funciones dentro de otras funciones usando las variables de la funcion inicial
def mostrar_mensaje(mensaje):
    mensaje = mensaje.title() #.title() te pone la oracion con la primera letra en mayus

    def mostrar():
        print(mensaje)
    return mostrar

nueva_funcion = mostrar_mensaje("codigo facilito")
nueva_funcion()

print("\n")
#------------------------------------------------------------------------------
#----------------Funciones Anidadas-------------------
#------------------------------------------------------------------------------
def comenzar_playlist(lista):
    def reproducir():
        #nonlocal lista       #para poder cambiar la lista dentro de la funcion, debemos usar el nonlocal
        lista = [1,2,3,4]  
        for val in lista:
            print(val)
    reproducir() #la funcion anidada debe ser nombrada dentro de la funcion principal
    print(lista)

lista = ["track 1", "track 2", "track 3", "track 4"]
comenzar_playlist(lista)