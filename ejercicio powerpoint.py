
def add_digits(number):
    aux=0
    while number>0:
        aux+=int(number%10)
        number/=10
    return aux


exit=False
#creo la variable
add_optiontotal=0
add_digitstotal=0
cont=0
while(exit==False):
    print("--------------------------------------")
    print("ingresar numero para sumar sus digitos")
    print("ingresa 0 para salir")
    option=int(input())
    add=add_digits(option)
    print("La suma de los digitos de numero "+str(option)+" es: "+str(add))
    add_optiontotal+=option
    add_digitstotal+=add
    if (option==0):
        exit=True
    else:
        cont+=1    

print("-----------------------------------------------------")

print("La cantidad de numeros ingresados fue de:",cont)
print("La suma de todos los numeros ingresados es:",add_optiontotal)
print("La suma de la suma de los digitos de todos los numeros ingresado es de:",add_digitstotal)