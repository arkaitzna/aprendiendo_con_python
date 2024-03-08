## conditionals

my_condition = 7

if my_condition: ##Es lo mismo que if my_condition == True:
    print("Se ejecuta la condicion de if")
print("La ejecucion continua")


my_other_condition = 5 * 2

if my_other_condition < 11 or my_condition == 9:
    print("El valor es menor a 11 y la otra condicion es igual a 7")
elif my_other_condition == 10: #Si pusieramos if comprovaria las 2 condiciones
    print("Es igual a 10")
else:
    print("Error")
print("La ejecucion continúa")

my_string=""
if not my_string:
    print("Mi cadena de texto es vacia")
    
if not my_string == "Me cadena de textooo":
    print("Los textos no coinciden")

