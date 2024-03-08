new_line_string = "Este es un string \ncon salto de linea"
print(new_line_string)
new_tab_string ="Este es un string\tcon tabulción"
print(new_tab_string)
new_scape_string ="\tEste es un string\nescapado"
print(new_scape_string)


#formateo
name, surname, age= 'pol', 'arkaitz', 29
print('mi nombre es {} {} y tengo {} años.'.format(name, surname, age))
print('mi nombre es %s %s y tengo %d años.' %(name, surname, age))
print('mi nombre es ' + name + ' ' + surname +  ' y tengo ' + str(age) +   ' años.')
print(f'mi nombre es {name} {surname} y tengo {age} años')


#desempaquetando caracteres

language = 'python'
print(len(language))
a, b, c, d, e, f = language
print(a+b+c+d+e+f)

#Division
language_slice= language[0:3]
print(language_slice)
language_slice= language[0:]
print(language_slice)
language_slice= language[-2]
print(language_slice)
language_slice= language[-4]
print(language_slice)
language_slice= language[0:3:5]
print(language_slice)
#Reverse
reverse_language = language[::-1]
print(reverse_language)

#Funciones
print(language.capitalize())
print(language.upper())
print(language.count("p"))
print("1".isnumeric())
print(language.lower().islower())
print(language.upper().isupper())
print(language.startswith("pu"))
print("Py"=="py")






