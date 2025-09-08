#Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario.

n = int(input("Ingrese un número positivo: "))
suma = 0

for i in range(n + 1):
    suma += i

print("La suma es:", suma)
