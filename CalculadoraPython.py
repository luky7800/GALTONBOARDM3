#CALCULADORA DE IMC

#Primero hay que definir las variables
nombre = input("introduce tu nombre:")
a = input("introduce tu apellido paterno: ")
n = input("Introduce tu apellido materno: ")


try:
    edad = int(input("Ingrese su edad: "))
    peso = float(input("Ingrese su peso en Kg: "))
    estatura = float(input("Ingrese su estatura en metros: "))

except: 
    print("Erros en los datos ingresados. El programa espera datos numericos en cada una de las secciones")
    exit()

IMC = peso / (float(estatura)**2)


 #Hacemos las distintas validaciones
if IMC < 15.99 :
        print("Delgadez severa")
elif IMC >= 16.00 and IMC <= 16.99 :
        print("Delgadez moderada")
elif IMC >= 17.00 and IMC <= 18.49:
        print("Delgadez leve")
elif IMC >= 18.50 and IMC <= 24.99 :
        print("Normal")
elif IMC >= 25.00 and IMC <= 29.99:
        print("Sobrepeso")
elif IMC >= 30.00 and IMC <= 34.99:
        print("obesidad leve")
elif IMC >= 35.00 and IMC <= 39.00:
        print("obesidad media")
elif IMC >= 40.00:
        print("obesidad morbida")

#Se imprimen los resultados
print("El nombre y apellidos de quien estacalculando su IMC es: ", nombre , a , n)
print("La edad de quien calcula su IMC es: ", edad )
print("El peso de quien calcula su IMC es de: ", peso)
print("La estatura de quien calcula su IMC es de: ", estatura)
print("Finalmente,", nombre, ",tu IMC es de", IMC )