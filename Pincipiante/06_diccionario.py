##Dictionaries##

my_dict= dict()
my_other_dict={}

my_other_dict = {
    "Nombre: ":"Pol",
    "Apellido: ":"Navarro",
    "Edad: ": 29,
    "Lenguajes: ": {"Python","HTML","CSS"},
    1:1.77,
    "Calle: ": "Carrer Maresme"
}
print(my_other_dict)
print(len(my_other_dict))

print(my_other_dict["Nombre: "])
print(my_other_dict[1])
my_other_dict["Nombre: "]="Arkaitz"
print(my_other_dict["Nombre: "])
del my_other_dict["Calle: "]
print(my_other_dict)
print("Arkaitz" in my_other_dict.values())#Esto nos sirve para ver si un valor en concreto esta en el diccionario en alguno de los valores. Si no pusieramos el .values() nos daria False ya que solo buscaria entre las claves(nombre, apellido....)
print(my_other_dict.items())
print(my_other_dict.keys())
print(my_other_dict.values())

##crear un diccionario sin valores a partir de una lista
my_list = ["Nombre", "Piso", 1]
my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
# Es lo mismo que hacer esto
my_new2_dict = dict.fromkeys(("Nombre", 1, "Calle"))
print(my_new2_dict)
##También sirve para vaciar los valores de un diccionario

