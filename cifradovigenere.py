import hamming
import numpy as np

LETRAS = ("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")    

def cifrado3(mensaje):
    ###mensaje=input("Ingresar mensaje a cifrar: ")
    clave="COMUNICACIONESDOS"
    traducido=[]
    indice_clave=3
    clave=clave.upper()

    mensaje3=""
    
    for symbol in mensaje:
        num=LETRAS.find(symbol.upper())
        if num!=-1:
            num+=LETRAS.find(clave[indice_clave])
            num%=len(LETRAS)
            if symbol.isupper():
                traducido.append(LETRAS[num])
            elif symbol.islower():
                traducido.append(LETRAS[num].lower())
            indice_clave+=1
            if indice_clave==len(clave):
                indice_clave=0
        else:
            traducido.append(symbol)
    
        pass

    mensaje3=('').join(traducido)

    print('Texto cifrado es: ',mensaje3)
    mensaje=""

    for c in mensaje3:
    
        Ruido= np.zeros(15) #vector con ruido
    
        envio= np.zeros(15) #vector 15 caractereres con hamming
        #envio es la matriz de hamming del resultado del hill 26
        envio=hamming.char_hamming1511(c)
        #se crea una copia de envio en ruido
        for n in range(15):
            Ruido[n]=(envio[n])
    
        #Se genera un ruido aleatorio
    
        Ruido=hamming.aleatorio(Ruido)
        mensaje=mensaje+str(hamming.ipr(Ruido))
    
        # # se imprimer valores
        # if (c == ',' and memoria==0):
        #     memoria=1
    
        # if(memoria ==0):
        #     print("  ",c,"        ",hamming.ipr(envio),"       ",hamming.ipr(Ruido))
    
    return mensaje

def descifrado3(mensaje):
    ###mensaje1=input("Ingresar mensaje a descifrar: ")
    clave="COMUNICACIONESDOS"
    traducido=[]
    indice_clave=3
    clave=clave.upper()

    mensaje=hamming.serial_Ascii(mensaje) # convierte de serial a ascii


    for symbol in mensaje:
        num=LETRAS.find(symbol.upper())
        if num!=-1:
            num-=LETRAS.find(clave[indice_clave])
            num%=len(LETRAS)
            if symbol.isupper():
                traducido.append(LETRAS[num])
            elif symbol.islower():
                traducido.append(LETRAS[num].lower())
            indice_clave+=1
            if indice_clave==len(clave):
                indice_clave=0
        else:
            traducido.append(symbol)
    return ('').join(traducido)

###mensaje= input('Ingresar mensaje: ')
###print(cifrado3(mensaje))

###print(descifrado3(mensaje))