###   Dates   ###

from datetime import datetime

now = datetime.now()

def print_date(date):
    print(date.second)
    print(date.minute)
    print(date.hour)
    print(date.day)
    print(date.month)
    print(date.year)
    print(date.timestamp())

print_date(now)

timestamp = now.timestamp() #Formato standard para darnos el momento exacto

print(timestamp)

#vamos a crear una fecha para el año nuevo 2024
year_2024 = datetime(2024, 1, 1)

print_date(year_2024)


from datetime import time #Nos da la opcion de encapsular tiempo pero no nos va a dar la hora real, aqui podremos "Manejar el tiempo a nuestro antojo", por ejemplo como en un videojuego. O por ejemplo si queremos lanzar a que fecha se lanzo un programa determinado o una noticia

current_time = time(21, 6, 0)


print(current_time.hour)
print(current_time.minute)
print(current_time.second)

#Mi fecha de nacimiento
from datetime import date
born_date = date(1994, 12, 2) #Definimos en que fecha nacimos
print(f"Mi fecha de nacimiento es {born_date.day}-{born_date.month}-{born_date.year}")

current_date =date.today() # Definimos que es la fecha actual con .today()
print(f"La fecha actual es {current_date.day}-{current_date.month}-{current_date.year}")

#modificar fechas
current_date = date(current_date.year + 1, current_date.month + 2, current_date.day + 5)
print(current_date)

diff = now - year_2024
print(diff)

from datetime import timedelta

#Queremos saber cuantas durara un curso. Sabemos la fecha de inicio y la fecha del final del curso

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(200, 100, 100, weeks = 13)

print(f"La duracion del curso es {end_timedelta - start_timedelta}")

duration_timedelta = end_timedelta - start_timedelta
print(f"La duracion del curso es {duration_timedelta}")