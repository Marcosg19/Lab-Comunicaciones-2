import hamming
import numpy as np;

def cifradocesar(mensaje):
    
    #mensaje = input('El mensaje a cifrar es: ')

    if mensaje == mensaje.upper():
        abecedario='ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz'
    else:
        abecedario='ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz'

    k=3

    #Variable de texto vacia donde almacenamos el texto ya cifrado
    cifrado=''

    for c in mensaje:
        if c in abecedario:
            cifrado += abecedario[(abecedario.index(c)+k)%(len(abecedario))]
        else:
            cifrado +=c

    print('Texto cifrado es: ', cifrado)

    mensajecesar=""

    for c in cifrado:
    
        Ruido= np.zeros(15) #vector con ruido
    
        envio= np.zeros(15) #vector 15 caractereres con hamming
        #envio es la matriz de hamming del resultado del hill 26
        envio=hamming.char_hamming1511(c)
        #se crea una copia de envio en ruido
        for n in range(15):
            Ruido[n]=(envio[n])
    
        #Se genera un ruido aleatorio
    
        Ruido=hamming.aleatorio(Ruido)
        mensajecesar=mensajecesar+str(hamming.ipr(Ruido))    

    return mensajecesar

def descifradocesar(mensaje):
    #mensaje_d = input('El mensaje a decifrar es: ')

    if mensaje == mensaje:
        abecedariod='ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz'

    n=3

    mensaje=hamming.serial_Ascii(mensaje) # convierte de serial a ascii

    descifrado=''

    for d in mensaje:
        if d in abecedariod:
            descifrado += abecedariod[(abecedariod.index(d)-n)%(len(abecedariod))]
        else:
            descifrado +=d

    return descifrado 
    #print('Texto descifrado es:', descifrado)


#mensaje = input('El mensaje a cifrar es: ')
#print(cifradocesar(mensaje))

#mensaje = input('El mensaje a descifrar es: ')
#print(descifradocesar(mensaje))