#Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

num = input("Ingrese un número: ")
invertido = num[::-1]
print("Número invertido:", invertido)
