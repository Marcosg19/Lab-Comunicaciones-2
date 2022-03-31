'''
import hamming
import numpy as np;


def cifrado2(texto):

    #texto = input("Introduzca el texto para el cifrado cesar:    ")




    diccionario_letras = {'A': 'D', 'a': 'd', 'Á': '+', 'á': '-',
                          'B': 'E', 'b': 'e',
                          'C': 'F', 'c': 'f',
                          'D': 'G', 'd': 'g',
                          'E': 'H', 'e': 'h', 'É': '*', 'é': '/',
                          'F': 'I', 'f': 'i',
                          'G': 'J', 'g': 'j',
                          'H': 'K', 'h': 'k',
                          'I': 'L', 'i': 'l', 'Í': '#', 'í': '=',
                          'J': 'M', 'j': 'm',
                          'K': 'N', 'k': 'n',
                          'L': 'Ñ', 'l': 'ñ',
                          'M': 'O', 'm': 'o',
                          'N': 'P', 'n': 'p',
                          'Ñ': 'Q', 'ñ': 'q',
                          'O': 'R', 'o': 'r', 'Ó': '€', 'ó': '$',
                          'P': 'S', 'p': 's',
                          'Q': 'T', 'q': 't',
                          'R': 'U', 'r': 'u',
                          'S': 'V', 's': 'v',
                          'T': 'W', 't': 'w',
                          'U': 'X', 'u': 'x', 'Ú': '%', 'ú': '&',
                          'V': 'Y', 'v': 'y',
                          'W': 'Z', 'w': 'z',
                          'X': 'A', 'x': 'a',
                          'Y': 'B', 'y': 'b',
                          'Z': 'C', 'z': 'c',
                          ' ': ' ', ',': ',', '?': '?', '¿': '¿', '.': '.'}

    print(texto)

    mensajeCesar=""

    for c in texto:
    
        mensajeCesar=mensajeCesar+diccionario_letras[c]
    
        #print(diccionario_letras.get(c))

        pass



    print(mensajeCesar)


    #memoria=0
    mensaje=""

    for c in mensajeCesar:
    
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






def descifrado2(texto):
    diccionario_letras = {'A': 'D', 'a': 'd', 'Á': '+', 'á': '-',
                          'B': 'E', 'b': 'e',
                          'C': 'F', 'c': 'f',
                          'D': 'G', 'd': 'g',
                          'E': 'H', 'e': 'h', 'É': '*', 'é': '/',
                          'F': 'I', 'f': 'i',
                          'G': 'J', 'g': 'j',
                          'H': 'K', 'h': 'k',
                          'I': 'L', 'i': 'l', 'Í': '#', 'í': '=',
                          'J': 'M', 'j': 'm',
                          'K': 'N', 'k': 'n',
                          'L': 'Ñ', 'l': 'ñ',
                          'M': 'O', 'm': 'o',
                          'N': 'P', 'n': 'p',
                          'Ñ': 'Q', 'ñ': 'q',
                          'O': 'R', 'o': 'r', 'Ó': '€', 'ó': '$',
                          'P': 'S', 'p': 's',
                          'Q': 'T', 'q': 't',
                          'R': 'U', 'r': 'u',
                          'S': 'V', 's': 'v',
                          'T': 'W', 't': 'w',
                          'U': 'X', 'u': 'x', 'Ú': '%', 'ú': '&',
                          'V': 'Y', 'v': 'y',
                          'W': 'Z', 'w': 'z',
                          'X': 'A', 'x': 'a',
                          'Y': 'B', 'y': 'b',
                          'Z': 'C', 'z': 'c',
                          ' ': ' ', ',': ',', '?': '?', '¿': '¿', '.': '.'}

    diccionario_letras = {v: k for k, v in diccionario_letras.items()} #invierte de llaves a valores


    #texto = input("Introduzca el texto para el DEScifrado cesar:    ");


    texto=hamming.serial_Ascii(texto) # convierte de serial a ascii

    #print(texto)

    print(texto)


    mensaje=""

    for c in texto:
    
        mensaje=mensaje+diccionario_letras[c]
        pass

    
    return mensaje








texto = input("Introduzca el texto para el cifrado cesar:    ")

print (cifrado2(texto))


#texto = input("Introduzca el texto para el Descifrado cesar:    ")

print(descifrado2(texto))
'''








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
#descifradocesar(mensaje)