###Functions###

def my_function ():
    print("Esto es una funcion")
    
my_function()

def sum_two_values (first_number, second_number):
    print(first_number + second_number)
    
    
sum_two_values(2, 3)
sum_two_values(19, True)
sum_two_values(1.78 , 1.3)


def sum_two_values_return(first_value, second_value):
    return first_value + second_value
my_result = sum_two_values_return(13,89)
print(my_result)


def print_name (name, surname, age):
    print(f"Mi nombre es {name} {surname} y tengo {age} años")

print_name("Pol", "Navarro", 29)
print_name(surname = 'Aragall', name = 'Arkaitz', age = 30)

def print_name_with_default (name, surname, alias = "no tengo alias"):
    if alias == "no tengo alias":
        print(f"Mi nombre es {name} {surname} y {alias}")
    else:
        print(f"Mi nombre es {name} {surname} y mi alias es {alias}")

print_name_with_default('Pol', 'Navarro', 'Ecko')

def print_texts(*text):
    print(text)
print_texts("Hola", "Python", "Pol")

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())
print_upper_texts("Hola", "Python", "Pol")

