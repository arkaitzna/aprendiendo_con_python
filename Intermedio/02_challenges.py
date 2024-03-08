###     Challenges     ###

"""Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz"."""

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0: #Esta bien que primero pongamos la condición más restrictiva y sigamos por esta línia hasta el else
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
    
fizzbuzz()

"""/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */"""

def is_anagrama(first_word, second_word):
    if first_word.lower() == second_word.lower():
        return False
    elif sorted(first_word.lower()) == sorted(second_word.lower()): #sorted() nos ayuda a ordenar con un mismo criterio, en este caso como vemos en el print de abajo lo ordena alfabeticamente
        return True 
    else:
        return False

print(is_anagrama("amor", "roma"))
print(sorted("amor".lower()))
print(sorted("roma".lower()))

"""/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */"""
 
def my_fibonacci():
    first = 0 
    next = 1
    
    for i in range (0,51):
        print(first)
        fib= first + next
        first = next
        next = fib
        
        
my_fibonacci()
