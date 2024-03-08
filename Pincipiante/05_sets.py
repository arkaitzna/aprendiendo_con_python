### Sets    ###


my_set = set()
my_other_set= {"Pol", "Navarro", 35}
print(type(my_other_set))
print(len(my_other_set))


my_other_set.add("Aragall")
print(my_other_set) #Los sets no es una estructura  ordenada
my_other_set.add("Pol")
print(my_other_set) # No admite repetidos

print("Pol" in my_other_set)
print(29 in my_other_set) #¿Esta 29 en este set? False