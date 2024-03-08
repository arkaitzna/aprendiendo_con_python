### Exception Handling ###

number_one, number_two = "1", 5
try:
    print(number_one + number_two)
    print("No se ha producido el error")
except:
    print("Se ha producido un error")
    
number_one, number_two = "1", 5
#Try, except, else, finnally
try:
    print(number_one + number_two)
    print("No se ha producido el error")
except: #Si no se ejecuta el try se ejecuta el except
    print("Se ha producido un error")
else: #Opcional
    #Se ejecuta si no se produce una excepción
    print("La ejecucion ha tenido exito")
finally: #Opcional
    #Se ejecuta siempre
    print("La ejecución continúa")

# Captura de excepciones por tipo

try:
    print(number_one + number_two)
    print("No se ha producido el error")
#A continuación podemos capturar concretamente los tipos de errores
except TypeError: #Si no se ejecuta el try se ejecuta el except de TypeError únicamente
    print("Se ha producido un TypeError")
except ValueError: #Si no se ejecuta el try se ejecuta el except de ValueError únicamente
    print("Se ha producido un ValueError")
    
#Dar información al usuario sobre el error
try:
    print(number_one + number_two)
    print("No se ha producido el error")
except TypeError as error: 
    print(error)
except Exception as exception:#Nos avisara si hay errores que no son TypeError
    print(exception)
