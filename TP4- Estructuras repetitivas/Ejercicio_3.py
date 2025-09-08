#Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

suma = 0
for i in range(a + 1, b):
    suma += i

print("La suma es:", suma)
