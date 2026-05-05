from random import randint


minimo = int(input("limite minimo:")) 
maximo = int(input("limite maximo:")) 
aleatorio = randint(minimo, maximo) 
print(f"Su numero aleatorio es: {aleatorio}")
if aleatorio %2 != 0:
    print(F"Su numero aleatorio es impar: {aleatorio}")
    aleatorio -= 1 
    if aleatorio < minimo:
        aleatorio = minimo + 1
    print(f"Se genera tablas de mult. del {aleatorio}")
else:
    print(f"Felicitaciones su numero aleatorio es par: {aleatorio}")
print(f"{aleatorio} x 1 = {aleatorio*1}")
print(f"{aleatorio} x 2 = {aleatorio*2}")
print(f"{aleatorio} x 3 = {aleatorio*3}")
print(f"{aleatorio} x 4 = {aleatorio*4}")
print(f"{aleatorio} x 5 = {aleatorio*5}")
print(f"{aleatorio} x 6 = {aleatorio*6}")
print(f"{aleatorio} x 7 = {aleatorio*7}")
print(f"{aleatorio} x 8 = {aleatorio*8}")
print(f"{aleatorio} x 9 = {aleatorio*9}")
print(f"{aleatorio} x 10 = {aleatorio*10}")
print(f"{aleatorio} x 11 = {aleatorio*11}")
print(f"{aleatorio} x 12 = {aleatorio*12}")
