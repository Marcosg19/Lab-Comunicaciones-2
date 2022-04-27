import hamming
import numpy as np;


def cifrado3(texto):

    #texto = input("Introduzca el texto para el cifrado cesar:    ")




    diccionario_letras = {'A': 'q', 'a': 'Q', 'Á': '+', 'á': '-',
                          'B': 'w', 'b': 'W',
                          'C': 'e', 'c': 'E',
                          'D': 'r', 'd': 'R',
                          'E': 't', 'e': 'T', 'É': '*', 'é': '/',
                          'F': 'y', 'f': 'Y',
                          'G': 'u', 'g': 'U',
                          'H': 'i', 'h': 'I',
                          'I': 'o', 'i': 'O', 'Í': '#', 'í': '=',
                          'J': 'p', 'j': 'P',
                          'K': 'a', 'k': 'A',
                          'L': 's', 'l': 'S',
                          'M': 'd', 'm': 'D',
                          'N': 'f', 'n': 'F',
                          'Ñ': 'g', 'ñ': 'G',
                          'O': 'h', 'o': 'H', 'Ó': '€', 'ó': '$',
                          'P': 'j', 'p': 'J',
                          'Q': 'k', 'q': 'K',
                          'R': 'l', 'r': 'L',
                          'S': 'ñ', 's': 'Ñ',
                          'T': 'z', 't': 'Z',
                          'U': 'x', 'u': 'X', 'Ú': '%', 'ú': '&',
                          'V': 'c', 'v': 'C',
                          'W': 'v', 'w': 'V',
                          'X': 'b', 'x': 'B',
                          'Y': 'n', 'y': 'N',
                          'Z': 'm', 'z': 'M',
                          ' ': ' ', ',': ',', '?': '?', '¿': '¿', '.': '.', '0': '1', '1': '2' , '2': '3' , '3': '4' , '4': '5' , '5': '6' , '6': '7' , '7': '8', '8': '9', '9': '0'}
    #print(diccionario_letras)

    mensajeCreado=""

    for c in texto:
    
        mensajeCreado=mensajeCreado+diccionario_letras[c]
    
        #print(diccionario_letras.get(c))

        pass



    print(mensajeCreado)


    #memoria=0
    mensaje=""

    for c in mensajeCreado:
    
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
    diccionario_letras = {'A': 'q', 'a': 'Q', 'Á': '+', 'á': '-',
                          'B': 'w', 'b': 'W',
                          'C': 'e', 'c': 'E',
                          'D': 'r', 'd': 'R',
                          'E': 't', 'e': 'T', 'É': '*', 'é': '/',
                          'F': 'y', 'f': 'Y',
                          'G': 'u', 'g': 'U',
                          'H': 'i', 'h': 'I',
                          'I': 'o', 'i': 'O', 'Í': '#', 'í': '=',
                          'J': 'p', 'j': 'P',
                          'K': 'a', 'k': 'A',
                          'L': 's', 'l': 'S',
                          'M': 'd', 'm': 'D',
                          'N': 'f', 'n': 'F',
                          'Ñ': 'g', 'ñ': 'G',
                          'O': 'h', 'o': 'H', 'Ó': '€', 'ó': '$',
                          'P': 'j', 'p': 'J',
                          'Q': 'k', 'q': 'K',
                          'R': 'l', 'r': 'L',
                          'S': 'ñ', 's': 'Ñ',
                          'T': 'z', 't': 'Z',
                          'U': 'x', 'u': 'X', 'Ú': '%', 'ú': '&',
                          'V': 'c', 'v': 'C',
                          'W': 'v', 'w': 'V',
                          'X': 'b', 'x': 'B',
                          'Y': 'n', 'y': 'N',
                          'Z': 'm', 'z': 'M',
                          ' ': ' ', ',': ',', '?': '?', '¿': '¿', '.': '.', '0':'1', '1': '2' , '2': '3' , '3': '4' , '4': '5' , '5': '6' , '6': '7' , '7': '8', '8': '9', '9': '0'}

    diccionario_letras = {v: k for k, v in diccionario_letras.items()} #invierte de llaves a valores

    #texto = input("Introduzca el texto para el Descifrado cesar:    ");


    texto=hamming.serial_Ascii(texto) # convierte de serial a ascii

    #print(texto)




    mensaje=""

    for c in texto:
    
        mensaje=mensaje+diccionario_letras[c]
        # print(c,"   ",diccionario_letras[c] )
        pass



    return mensaje


###texto = input("Introduzca el texto para el cifrado:    ")

###print (cifrado3(texto))


#texto = input("Introduzca el texto para el DEScifrado cesar:    ")

###print (descifrado3(texto))