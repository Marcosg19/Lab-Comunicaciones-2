import cifdefHill
import cifradocesar
import cifradocreado
import cifradovigenere
import random
import os
import serial


serialcomm = serial.Serial('COM3', 57600)
serialcomm.timeout = 1








def menu(): 
    os.system('clear')
    print("******************************")
    print("* Introduzca el texto        *")
    print("*    a Cifrar                *")
    print("******************************")
    




def Encriptar(texto):
    os.system('clear')
    texto=texto
    
    indice= random.randint(1, 3)
    #indice =3
    

    if (indice==1):
        print("********  Hill     *********************")
    elif (indice==2):
        print("********  Cesar    ********************")
    elif (indice==3):
        print("**********Vigenere ********************")
    
    
    if (indice==1):
        texto=cifdefHill.cifrado(texto)
    elif (indice==2):
        texto=cifradocesar.cifradocesar(texto)
    elif (indice==3):
        texto=cifradovigenere.cifrado3(texto)
        
    
    
    texto=str(indice)+'.'+ texto
    
    

    return texto



while True:
    menu()
    texto = input()
    texto_E=Encriptar(texto)

    print(texto_E)
    serialcomm.write(texto_E.encode())
    input()
   
    