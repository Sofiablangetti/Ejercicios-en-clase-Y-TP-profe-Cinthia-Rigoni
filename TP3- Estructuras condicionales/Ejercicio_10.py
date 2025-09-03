#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("Ingrese su hemisferio (N/S): ").upper()
mes = int(input("Ingrese el número de mes: "))
dia = int(input("Ingrese el día: "))

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    if hemisferio == "N":
        estacion = "Invierno"
    else:
        estacion = "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    if hemisferio == "N":
        estacion = "Primavera"
    else:
        estacion = "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    if hemisferio == "N":
        estacion = "Verano"
    else:
        estacion = "Invierno"
else:
    if hemisferio == "N":
        estacion = "Otoño"
    else:
        estacion = "Primavera"

print("La estación es:", estacion)
