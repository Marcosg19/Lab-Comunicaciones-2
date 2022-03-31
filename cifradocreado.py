import hamming
import numpy as np;


def cifrado3(texto):

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
    print(diccionario_letras)

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


def descifrado3(texto):
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
#HOLA COMO ESTAS ESTA ES PRUEBA DE TEXTO

    #texto = input("Introduzca el texto para el Descifrado cesar:    ");


    texto=hamming.serial_Ascii(texto) # convierte de serial a ascii

    #print(texto)




    mensaje=""

    for c in texto:
    
        mensaje=mensaje+diccionario_letras[c]
        # print(c,"   ",diccionario_letras[c] )
        pass



    return mensaje


#texto = input("Introduzca el texto para el cifrado cesar:    ")

#print (cifrado3(texto))


#texto = input("Introduzca el texto para el DEScifrado cesar:    ")

#print (descifrado3(texto))