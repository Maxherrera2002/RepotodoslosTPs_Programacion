
#Ejercicio 1

def experiment(time):
    import random
    camino=random.randint(1,3)
    if (camino==1):
        time+=3
        return experiment(time)
    elif(camino==2):
        time+=5
        return experiment(time)
    elif(camino==3):
        time+=7
        return time

print("-----------------------------------------------")
print("El raton salio en",experiment(0),"minutos")        
 
#Ejercicio 2
def f(n): 
    s = str(n)
    if len(s)<=1: #retora el ultmo caracter (que seria el el primero en el String inicial)
        return s
    return s[-1] + f (int(s[:-1])) #el ultimo caracter se le suma la el resto del array pasado por la funcion     

while True:
    option=int(input("ingresar n "))
    if(option==0):
        break
    else:
        print("n es:",f(option))   