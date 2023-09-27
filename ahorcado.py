
import random
def ahorcado(word_,found_):
    letter=(input("Ingresar una letra a buscar: ")).lower()
    for i in word_:
        if(letter==i):
            found_+=i;   
    
    return found_

def show(word_,found_):
    #creo una variable para mostrar el ahorcado en su estado actual
    show_=""
    for i in word_:
        if found_=="":
            show_+="_"
        else:
            aux=0
            for j in found_:
                if(i==j):
                    show_+=i
                    aux+=1
                    break
            if (aux==0):
                show_+="_"    
    return show_   
                        
                        
        

                         
words=["teclado", "mause", "monitor", "procesador", "bug", "funcion", "error", "variables","bucle"]

option=""
#creo un bucle while para el menu del juego
while(option!="b"):
    #muestro el menu juego
    print("a) Nuevo juego")
    print("b) salir")

    option=(input()).lower() #lo paso a minuscula
    
    if (option=="a"):#se ingresa opcion "a" 
        tries=3 #cantidad de intentos
        word=words[random.randrange(8)] #se busca una palabra en el array de forma aleatoria 
        found="" # Creo una variable para guardar las letras encontradas 
        while(tries>0): # El bucle del juego 
            if(word==show(word,found)):# Si la palabra es igual a lo que devuelve show se termina 
                break         
            print(show(word,found)) # Muestra el estado actual del ahorcado   
            aux=ahorcado(word,found)# Guardo el el estado en el que se encuentra el ahorcado despues de comprobar una letra    
            if(aux==found): #si son iguales (si la lentra ingresada no se encontro en la palabra)  y resta 1 a los intentos       
                tries-=1                                                                      
                print("No se encontro la letra")                                                     
                print("Te quedant",tries,"intentos")                                                              
            else:  # Si no son iguales (si la letra se encontro) se guarda la letra en una variable para saber cuales letras encontro el usuario                                                                                
                found=aux                                                                                       
                print("Bien, sigamos")                                                                     
                                                                                                                                               
                                                                                                                                   
        if(tries>0):    # si sobran intentos gana el usuario      
            print("Muy bien Has ganado")
        else:# si no pierde 
            print("mas suerte para la proxima );")    
        print("---------------------------------------")    
    elif(option=="b"): #sale del juego 
        break
    else:
        input("Error intenta nuevamente")
