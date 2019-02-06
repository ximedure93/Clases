#crear una carpeta que se llame clases y adentro poner los archivos dino.py y persona.py
#crear una clase Persona() que tenga como atributos nombre, edad y profesion.
#Al instanciar la clase tiene que saludar igual que el dino diciendo sus atributos

class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre  #atributo = tipo variable interna de la clase
        self.edad = edad
        self.profesion = profesion
        print("me llamo", nombre, ". tengo", edad, "y soy", profesion)

per1 = Persona("Xime", "25", "Programadora") #objeto
per2 = Persona("Bjorn", "26", "Futbolista")
print(per1)

print(per1.nombre)
print(per1.edad)
print(per1.profesion)