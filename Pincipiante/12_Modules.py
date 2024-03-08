###     Modules     ###

import module #Estamos importando un modulo de un archivo que hemos creado previamente llamado module.py, este archivo es un modulo creado por nosotros y nos sirve para llamar a funciones que esten dentro de este archivo y a la vez tener todo nuestro trabajo mejor estructurado
module.sumValue(3, 2, 4 )
module.printValue("Hola!")

#from 09_functions import sum_two_values # Esto no funcionara porque 09_functions no tiene la nomenclatura correcta para importar funciones en este modulo. La nomenclatura correcta tiene que ser snake_case. Deberiamos renombrar el archivo#


from module import sumValue, printValue
sumValue(3, 2, 4 )
printValue("Hola!")

import math

print(math.pi) #Nos da el numero Pi
print(math.pow(2, 8))#Esto nos ayuda a hacer exponentes


from math import pi as pi_value # Unicamente estamos llamando a la funcion pi de math, renombrandola como pi_value
print(pi_value)

