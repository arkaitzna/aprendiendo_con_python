###Lists###


my_list = list() #Si no pusieramos list() y solo pusieramos () seria una TUPLA
my_other_list=[]
print(len(my_list))

my_list=[35, 24, 62, 53, 30, 30, 17]
print(my_list)
print(len(my_list))

my_other_list=[29, 1.83, "Pol", "Navarro"]
print(type(my_other_list))
print(type(my_list))

"""print(my_other_list[0])
age=my_other_list[0]
height=my_other_list[1]
name=my_other_list[2]
surname=my_other_list[3]
print(age, height, name, surname)
print("Mi edad es de", age,"años y mi nombre es", name, surname, "y mi altura es de", height, "metros")"""
print(my_list.count(30))#Me devuelve los elementos que hay repetidos con este valor
#Lo que he puesto arriba se puede resumir en esto
age, height, name, surname= my_other_list
print(name)

print(my_list+my_other_list )

#Array: para trabajar con arrais en python tenemos que descargarnos la libreria numpy (import numpy as np) y ejecutarla. El array nos puede servir para hacer calculos aritmeticos con ellos. Es decir podriamos multiplicar una lista x2 y nos multiplicaria cada elementox2. 


###TUPLAS###
my_tuple = tuple()
my_other_tuple = (35, "Arkaitz")

my_tuple = ( 29, 1.82, "Pol", "Navarro", "Navarro")

print(my_tuple)
print(type(my_tuple))
print(my_tuple[0:2])
print(my_tuple[-1])
#ERROR print(my_tuple[6] o incluso [-5]) Da error ya que no existe
print(type(my_tuple[0:2]))
print(my_tuple.count(29))
print(my_tuple.count("Navarro"))
print(my_tuple.index(29))
"""my_tuple[0] = 1.82
print(my_tuple)""" ###Las Tuplas son inmutables por eso no puedes asignarles otro valor
print(my_tuple + my_other_tuple)


my_son_tuple = my_tuple + my_other_tuple

print(my_son_tuple)
print(my_son_tuple[3:6])

###Transformememos una tupla en una lista

my_tuple_to_list = list(my_tuple)
print(type(my_tuple_to_list))
