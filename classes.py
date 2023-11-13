#CLASSES

print("\n")
#------------------------------------------------------------------------------
#----------------Estrucutra Basica-------------------
#------------------------------------------------------------------------------
class Usuario: #Esta  es una clase

    def __init__(self, username="", correo="", nombre=""):#Esto es como el constructor
        self.username = username
        self.correo = correo
        self.nombre = nombre

    """ Self es obligatorio"""
    def saluda(self): #Esto es un metodo, basicamente es una funcion para que haga algo
        return "soy un usuario " + self.nombre
        """los metodos pueden usar el return o print"""

    def mostrar_correo(self): #Este es otro metodo
        print(self.correo)


codi = Usuario("Codi","codi@gmail.com","Codigo")#Eso es un objeto y le pasamos valores
facilito = Usuario()#Este es otro obj pero vacio


resultado = codi.saluda()

print(resultado) 
codi.mostrar_correo()


print("\n")
#------------------------------------------------------------------------------
#----------------Variables-------------------
#------------------------------------------------------------------------------
class Circulo:
    pi = 3.141592 #es una variable de clase

    def __init__(self,radio):
        self.radio = radio #es una variable de instancia

circulo_a = Circulo(10)
circulo_b = Circulo(20)

circulo_b.radio = 100

print(Circulo.pi)
print(circulo_a.radio)
print(circulo_b.radio)



print("\n")
#------------------------------------------------------------------------------
#----------------Herencia-------------------
#------------------------------------------------------------------------------
class Animal(object):
    def __init__(self,nom):
        self.nom = nom
        #self.edad = edad
    def comer(self):
        print("Comiendo")

    def dormir(self):
        print("Durmiendo")

class Mascota:
    def fecha_adopcion(self,fecha):
        self.fecha = fecha

class Perro(Animal,Mascota):
    def __init__(self,nom,nombre,raza,edad):
        Animal.__init__(self,nom)
        self.raza = raza
        self.nombre = nombre
        self.edad = edad

    def nomb(self):
        return 'nombre: ',self.nom
    def ladrar(self):
        print("Ladrando")

class Gato(Animal):
    def __init__(self,nombre="",raza="",edad=""):
        self.raza = raza
        self.nombre = nombre
        self.edad = edad
    def ronronear(self):
        print("Ronroneo")
    def mostrar_nombre(self):
        print(self.nombre)

Animal(nom='max')
firulais = Perro('',"max","snahuzer",8.7)
firulais.comer()
firulais.dormir()
firulais.ladrar()
firulais.fecha_adopcion("hoy") 
print('nombre: ',firulais.nombre)
hola = firulais.nomb()
print(hola)

print("\n-------\n")

moy = Gato("Moy","no se",8)
moy.comer()
moy.dormir()
moy.ronronear()
moy.mostrar_nombre()