#Ejercicio 1 
print("Ejercicio 1")
print("1-	Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces. ")
pallllll1=input("Ingresar palabra ")
aux55=1
for i in range(10):
    print("impresión", aux55)
    print(pallllll1)
    aux55=aux55+1

#Ejercicio 2
print("Ejercicio 2")
print("2-	Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).")

edadd=int(input("Ingresar tu edad: "))
for i in range(edadd):
    print("Edad:",i+1)

#Ejercicio 3
print("Ejercicio 3")
print("3-	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.")

numeroo=int(input("Ingresar el numero: "))
todossimpares=""
for i in range(numeroo):
   
    if(i+1==numeroo):
        if((1+i)%2!=0):
             todossimpares=todossimpares+str(i+1)
         
    elif((i+1)%2!=0):
        todossimpares=todossimpares+str(i+1)+","

print(todossimpares)      


#Ejercicio 4
print("Ejercicio 4")
print("4- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.")

cuentaatras=int(input("Ingresar cuenta: "))
cuentaatras_=""
for i in range(cuentaatras):
    if(i==cuentaatras-1):
        cuentaatras_=cuentaatras_+str(cuentaatras-i)
    else:    
         cuentaatras_=cuentaatras_+str(cuentaatras-i)+","
print(cuentaatras_)

#Ejercicio 5
print("Ejercicio 5")
print("5-Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.")

invertir=int(input("Ingresar cuanto dinero quiere invertir: "))
interes=int(input("ingresar interes anual en porcentaje del 1 al 100: "))
anosss=int(input("cuantos años: "))

for i in range(anosss):
    print("Ingresos año "+str(i+1))
    print((invertir*interes)/100)
    invertir=invertir+((invertir*interes)/100)
    print("Dinero total año "+str(i+1))
    print(invertir)

#Ejercicio 6
print("Ejercicio 6")
print("6-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.")

alturaa=int(input("Ingresar altura: "))
anchoo="*"
for i in range(alturaa):
    if (i==0):
        print(anchoo)
    else:
        anchoo=anchoo+" "+"*"
        print(anchoo)
            
#Ejercicio 7
print("Ejercicio 7")
print("7-	Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.")

tabla=int(input("¿Que tabla quieres ver? "))
for i in range(10):
    print(str(tabla)+"x"+str(i+1)+"="+str((i+1)*tabla))

#Ejercicio 8
print("Ejercicio 8")
print("8-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.")


alturaa_=int(input("Ingresar altura: "))
anchoo_="1"
quenum_=3
for i in range(alturaa_):
    if (i==0):
        print(anchoo_)
    else:
        anchoo_=str(quenum_)+" "+anchoo_
        print(anchoo_)
        quenum_=quenum_+2

#Ejercicio 9
print("Ejercicio 9")
print("9-	Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.")

contrasena=input("Ingresa una contraseña: ")
salida=False
while(salida==False):
    if(input("Ingresar contraseña ")==contrasena):
        salida=True
        print("Contraseña nuevamente correcta")
    else:
        print("La contraseña ingresada no coincide con la contraseña guardad")


#Ejercicio 10
print("Ejercicio 10")
print("10-	Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.")
    
num=int(input("Ingresar numero primo "))

if(num==1):
    print("no es numero primo")
else:
    ess=num%2
    if(ess>(num%3)):
        ess=num%3
    
    if(ess==0 and num!=2 and num!=3):
        print("no es numero primo")
    else:
        print("es numero primo")

#Ejercicio 11
print("Ejercicio 11")
print("11-	Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.")

palabra=input("Ingresa una palabra: ")


for i in range(len(palabra)):
    print(palabra[len(palabra)-i-1:len(palabra)-i])

#Ejercicio 12
print("Ejercicio 12")
print("12-	Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.")

frase=(input("Ingresar frase: ")).lower()
letra=input("ingresar letra a buscar: ")
letra=letra.lower()

encontro=0
for i in range(len(frase)):
    if (frase[i:i+1]==letra):
        encontro=encontro+1

print("la letra '"+letra+"' se encontro "+str(encontro)+" veces")

#Ejercicio 13
print("Ejercicio 13")
print("13-	Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.")

salir=False
while(salir==False):
    frase=input("ingresar frase ")
    if(frase=="salir"):
        salir=True
    else:
         print(frase+" "+frase[len(frase)-3:len(frase)])
      

#Ejercicio 14
print("Ejercicio 14")
print("14-	Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.")

print("ingesar 2 numeros")
num1=int(input())
num2=int(input())

if (num1%2==0 and num2%2==0):
    print("Los numeros "+str(num1)+" y "+str(num2)+" son pares")
elif(num1%2!=0 and num2%2!=0):
    print("Los numeros "+str(num1)+" y "+str(num2)+" son impares")
elif(num1%2==0 and num2%2!=0):
    print("El numero "+str(num1)+" es par y el numero "+str(num2)+" es impar")
elif(num1%2!=0 and num2%2==0):
    print("El numero "+str(num1)+" es impar y el numero "+str(num2)+" es par")        

#Ejercicio 15  
print("Ejercicio 15")
num=int(input("ingresar un numero entero ")) 

divisores="" 

for i in range(num): 
    if (num%(i+1)==0):
        divisores=divisores+str(i+1)+"," 

print(divisores)

#Ejercicio 16 
print("Ejercicio 16")
ciclos=int(input("cuantos numeros quiere introducir? ")) 

nega=0 

for i in range(ciclos): 
    num=int(input("ingrese numero ")) 
    if (num<0): 
        nega=nega+1 

print("ingreso",nega,"numeros negativos") 


#Ejercicio 17
print("Ejercicio 17")
print("17-  Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).")

phrase=input("Ingresar frase ")
vowels=""

for i in range(len(phrase)):
    if (i==0):
       
        if (phrase[i:i+1] == "a" or phrase[i:i+1] == "e" or phrase[i:i+1] == "i" or phrase[i:i+1] == "o" or phrase[i:i+1] == "u"):
            vowels=vowels+phrase[i:i+1]
    elif(phrase[i:i+1] == "a" or phrase[i:i+1] == "e" or phrase[i:i+1] == "i" or phrase[i:i+1] == "o" or phrase[i:i+1] == "u"):
        aux="True"
        for j in range(len(vowels)):
            if (phrase[i:i+1]==vowels[j:j+1]):
                aux="False"
        
        if (aux=="True"):
            if(vowels==""):
                vowels=vowels+phrase[i:i+1]
            else:
                vowels=vowels+","+phrase[i:i+1]
                
print(vowels)            


#Ejercicio 18
print("Ejercicio 18")
print("18-  Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…")

def fibonacci(num):
    if(num==0):
        return 0
    elif(num==1):
        return 1
    else:
        return(fibonacci(num-1)+fibonacci(num-2))

string=""
for i in range(10):
    if (i==0):
         string=string+str(fibonacci(i))
    else:
         string=string+", "+str(fibonacci(i))
print("Los primeros 10 numeros de fibonacci son: ")
print(string)

         
#Ejercicio 19
print("Ejercicio 19")
print("19-	Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. El programa deberá comprobar que las cantidades ingresadas sean positivas.")

#ahorro
saving=int(input("Ingresar meta de ahorro: "))
#alcancía
piggy_bank=0

while (piggy_bank<saving):
    aux=int(input("¿Cuando dinero quiere ingrear a la alcancía? "))
    if(aux < 0):
        print("No puedes retirar el dinero, aun no llegas a tu meta")
    elif(aux==0):
        print("¿?")
    elif(aux > 0):    
        piggy_bank= piggy_bank + aux
print("llegaste a tu meta de $"+str(piggy_bank))        

         
#Ejercicio 20
print("Ejercicio 20")
print("20-	Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.")
exit=False
addition=0
while(exit==False):
    num=int(input("Ingresar numero entero: "))
    if (num>0):
        addition=addition+num
    elif(num==0):
        exit=True    
print("La sumatoria de todos los numero ingresados es:",addition)


#Ejercicio 21
print("Ejercicio 21")
print("21-	Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.")

exit=False
aux=True
elderly=0
while(exit==False):
    num=int(input("Ingresar numero entero: "))
    if(num==0):
        exit=True
    elif(aux==True):
        elderly=num
        aux=False
    elif(num>elderly):
        elderly=num    
if (elderly==0):
    print("no ingreso un numero valido")
else:
    print("El numero ingresado mas grande fue:",elderly)    

#Ejercicio 22
print("Ejercicio 22")
print("22-	Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.")

exit = False
pair=0

while(exit==False):
    number=int(input("ingresar un numero entero positivo"))
    if(number==-1):
        exit=True
    elif(number>0):
        totalamount=0
        if ((number%2)==0):
            pair+=1
        while(number>0):
            totalamount+=(number%10)
            number/=10
        print("La sumad de las cifras del numero ingresado es:",totalamount)    
    
#Ejercicio 23, 24 

cost = input("Ingrese el monto de la compra o ingrese 0 para terminar ")
cost = int(cost)
totalcost = 0
while cost != 0:
    if cost < 0:
        cost = input("Por favor, ingrese un monto positivo ")
        cost = int(cost)
        continue
    totalcost = totalcost + cost
    cost = input("Ingrese el monto de la compra o ingrese 0 para terminar ")
    cost = int(cost)
   
if totalcost > 1000 :
    discount = totalcost/10
    totalcost = totalcost - discount
   
print("Su precio final es: $", totalcost)

        
#Ejercicio 25
print("Ejercicio 25")
print("25-	Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número. El factorial de 0 es 1.")
print("Ingresar un numero entero positivo para mostrar su factorial")
n=int(input())
def factorial(n):
   if n==0 or n==1:
            result=1
   elif n>1:
            result=n*factorial(n-1)
   return result
print("El factorial de",n," es ",factorial(n))