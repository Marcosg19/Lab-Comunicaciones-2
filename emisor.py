import cifdefHill
import cifradocesar
import cifradocreado
import cifradovigenere
import random


def Encriptar(texto):
    #texto = input("Introduzca el texto: ")
    texto=texto
    
    
    indice= random.randint(1, 3)
    #indice =3
    print(indice)
    
    
    if (indice==1):
        texto=cifdefHill.cifrado(texto)
    elif (indice==2):
        texto=cifradocesar.cifradocesar(texto)
    elif (indice==3):
        texto=cifradovigenere.cifrado3(texto)
        
    
    texto1 = texto
    texto=str(indice)+'.'+ texto
    
    
    print(texto1)

    return texto


#texto = input("Encriptar: ")

#print(Encriptar(texto))
