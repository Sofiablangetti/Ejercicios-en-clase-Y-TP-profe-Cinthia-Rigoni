#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene

num = int(input("Ingrese un número entero: "))
cantidad = len(str(abs(num)))
print("El número tiene", cantidad, "dígitos")
