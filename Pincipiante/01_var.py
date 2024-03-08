#Variables
my_variable = "string"
my_n_variable = 0
my_boo_var = True
my_n_variable = str(my_n_variable)
print(type(my_n_variable))
print(my_n_variable)
print("Hola esta variable es un ", my_variable, "y esta dando" ,my_n_variable, "errores. Todo esto es ", my_boo_var)

#Variables en una misma linia.¡¡ Cuidado con abusar de esta sintaxis!!
name, surname, alias, age = "Pol" , "Navarro" , "Arkaitz" , "29"
print("Mi nombre es",name,surname,", mi alias es", alias, "y tengo ", age, "años.")


#Inputs
name = input('¿Cual es tu nombre?')
surname = input('¿Cual es tu apellido?')
alias = input('¿Cual es tu alias?')
age = input('¿Cual es tu edad?')
print("Mi nombre es",name,surname,", mi alias es", alias, "y tengo ", age, "años.")

#forzamos el tipo¿?
address: str = "Mi dirección"
address= 0 
print(address)

