import cifdefHill
import cifradocesar
import cifradocreado
import cifradovigenere
import random


#cifrado a emplear de forma aleatoria
# 1--- hill
# 2----cesar
# 3----crack3



def Encriptar(texto):
    #texto = input("Introduzca el texto: ")
    texto=texto.upper()
    
    
    indice= random.randint(1, 3)
    #indice =3
    print(indice)
    
    
    if (indice==1):
        
        texto=cifdefHill.cifrado(texto)
    elif (indice==2):
        texto=cifradocesar.cifradocesar(texto)
    elif (indice==3):
        texto=cifradovigenere.cifrado3(texto)
        
    
    
    texto=str(indice)+'.'+ texto
    
    #print(texto)

    return texto


texto = input("Encriptar: ")

print(Encriptar(texto))