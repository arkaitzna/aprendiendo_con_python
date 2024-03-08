### Loops ###

#While


my_condition = 0

while  my_condition < 10:
    print(my_condition)
    my_condition += 2
else: 
    print("El contador ha llegado a 10")
    
while  my_condition < 20:
    my_condition += 1
    print(my_condition)
    if my_condition == 15:
        print("Mi condicion es  15")
        print("Se detiene el bucle")
        break
print("La ejecucion continua con los FOR")

#For

my_list=[30, 23, 49, 87, 78, 15]

for element in my_list:
    
    print(element)
    
print("Todos los elementos FOR de my_list se han impreso en consola")

my_tuple= (35, 1.77, "Pol", "Navarro")
for element2 in my_tuple:
    
    print(element2)
    
print("Todos los elementos FOR de my_tupla se han impreso en consola")

my_set={"Pol", "Navarro", 29}
for element3 in my_set:
    
    print(element3)
    
print("Todos los elementos FOR de my_set se han impreso en consola")

my_dict= {"Nombre":"Pol", "Edad":35, "Calle":"Carrer Maresme"}
for element4 in my_dict.values():#Para imprimir las llaves no hace falta ponerle el .keys()
    
    print(element4)
    
print("Todos los valores FOR de my_dict se han impreso en consola")
for element4 in my_dict:
    
    print(element4)
    
print("Todas las llaves FOR de my_dict se han impreso en consola")
for element4 in my_dict:
    
    print(element4)
    if element4 == "Edad":
        break
else:   
    print("Todas las llaves FOR de my_dict se han impreso en consola hasta que ha encontrado la edad")

for element4 in my_dict:
    
    print(element4)
    if element4 == "Edad":
        continue
else:   
    print("Todas las llaves FOR de my_dict se han impreso en consola y ha seguido continuando el bucle")