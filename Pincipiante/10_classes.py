###     Classes     ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson()) ## o tambien si no tenemos que rellenar ningun dato print(MyEmptyPerson)

class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.__name = name #Hemos privatizado esta propiedad
        self.surname = surname#Las siguientes siguen siendo publicas
        self.alias = alias
        self.fullname = f"{name} {surname} ({alias})"
    def walk (self):
        print(f"{self.fullname} está caminando.")

my_person = Person("Pol", "Navarro", "Ecko")
#print(f"Hola mi nombre es {my_person.__name} {my_person.surname}")
print(f"Hola mi nombre es {my_person.fullname}")#Nos da el mismo resultado ya que fullname == name + surname
my_person.walk()

my_girlfriend = Person("Fabiana", "Romero", "Haylek")
my_girlfriend.walk()

my_other_person = Person("Dani", "Pujol", "Deni")
my_other_person.fullname = "Deni (Sote)"
my_other_person.walk()

