import math
import numpy as np;
import random

"""Funcion que genera la paridad de los datos"""
def hamming1511(letra):

    

    datoSinParidad = np.zeros(11)
    #datoSinParidad = letra

    

    """Guardamos los bits de datos"""
    
   
    
    for i in range(0, len(letra)):
        datoSinParidad[i]=letra[i]
        pass

    
 
    d3 = int(datoSinParidad[0])
    d5 = int(datoSinParidad[1])
    d6 = int(datoSinParidad[2])
    d7 = int(datoSinParidad[3])

    d9 =  int(datoSinParidad[4])
    d10 = int(datoSinParidad[5])
    d11 = int(datoSinParidad[6])
    d12 = int(datoSinParidad[7])
    d13 = int(datoSinParidad[8])
    d14 = int(datoSinParidad[9])
    d15 = int(datoSinParidad[10])
 

    """GENERAMOS LA PARIDAD"""


    p1 = d3 ^ d5 ^ d7 ^ d9 ^ d11 ^ d13 ^ d15
    p2 = d3 ^ d6 ^ d7 ^ d10 ^ d11 ^ d14 ^ d15
    p4 = d5 ^ d6 ^ d7 ^ d12 ^ d13 ^ d14 ^ d15
    p8 = d9 ^ d10 ^ d11 ^ d12 ^ d13 ^ d14 ^ d15


    """OBTENEMOS EL DATO CON PARIDAD"""

    datoConParidad= np.zeros(15)

    datoConParidad[0] = p1
    datoConParidad[1] = p2
    datoConParidad[2] = d3 
    datoConParidad[3] = p4
    datoConParidad[4] = d5
    datoConParidad[5] = d6
    datoConParidad[6] = d7
    datoConParidad[7] = p8
    datoConParidad[8] = d9
    datoConParidad[9] = d10
    datoConParidad[10] = d11
    datoConParidad[11] = d12
    datoConParidad[12] = d13
    datoConParidad[13] = d14
    datoConParidad[14] = d15



    return datoConParidad


"""Generamos un error aleatorio para cambiar un bit de los 15 que se envian"""
def aleatorio (entrada):
    

    PosicionAleatoria = random.randint(0, 14)
    ###print("valor aleatorio es:  ",(PosicionAleatoria))
    entrada[PosicionAleatoria]=not(entrada[PosicionAleatoria])

    
    return entrada

"""convierte un array bit a decimal"""
def convertir_a_int(array):
    suma=0
    for i in range (len(array)):
        suma=int(array[i])*(2**(len(array)-1-i))+suma
        #suma=int(array[i])*(2**i)+suma
    return suma
        
"""se detecta y corrigue el error por medio de los bits de paridad"""
def deteccion_de_error(datoConruido):
    
    datoRecibido= datoConruido


    p1 = int( datoRecibido[0] )
    p2 = int( datoRecibido[1] )
    d3 = int( datoRecibido[2] )
    p4 = int( datoRecibido[3] )
    d5 = int( datoRecibido[4] )
    d6 = int( datoRecibido[5] )
    d7 = int( datoRecibido[6] )
    p8 = int( datoRecibido[7] )
    d9 = int( datoRecibido[8] )
    d10 = int( datoRecibido[9] )
    d11 = int( datoRecibido[10] )
    d12 = int( datoRecibido[11] )
    d13 = int( datoRecibido[12] )
    d14 = int( datoRecibido[13] )
    d15= int( datoRecibido[14] )

    """  Se verifica si existio un error por medio de los bits de paridad """
    posError1 =p1 ^ d3 ^ d5 ^ d7 ^ d9 ^ d11 ^ d13 ^ d15
    posError2 = p2 ^ d3 ^ d6 ^ d7 ^ d10 ^ d11 ^ d14 ^ d15
    posError3 = p4 ^ d5 ^ d6 ^ d7 ^ d12 ^ d13 ^ d14 ^ d15
    posError4 = p8 ^ d9 ^ d10 ^ d11 ^ d12 ^ d13 ^ d14 ^ d15

    """ Se obtiene la posicion del error es cero si no existe"""

    posiciondelerrorbin= np.zeros(4)

    posiciondelerrorbin[0] = posError4

    posiciondelerrorbin[1] = posError3

    posiciondelerrorbin[2] = posError2

    posiciondelerrorbin[3] = posError1



    numero= convertir_a_int(posiciondelerrorbin)


    return numero
""" imprime el vector como yo quiero"""

def ipr(matriz):
    valor=""
    for c in matriz:
        valor = valor+str(int(c))
    
    return valor
""" Selecciona los bits de datos quitando los de paridad"""

def recolecta_el_dato(datoRecibido):

    #p1 = int( datoRecibido[0] )
    #p2 = int( datoRecibido[1] )
    #d3 = int( datoRecibido[15] )
    #p4 = int( datoRecibido[3] )
    d5 = int( datoRecibido[2] )
    d6 = int( datoRecibido[5] )
    d7 = int( datoRecibido[6] )
    #p8 = int( datoRecibido[7] )
    d9 = int( datoRecibido[8] )
    d10 = int( datoRecibido[9] )
    d11 = int( datoRecibido[10] )
    d12 = int( datoRecibido[11] )
    d13 = int( datoRecibido[12] )
    d14 = int( datoRecibido[13] )
    d15= int( datoRecibido[14] )
    #d16= int( datoRecibido[2] )


    datoOriginal = str(d5)+str(d6)+str(d7)+str(d9)+str(d10)+str(d11)+str(d12)+str(d13)+str(d14)+str(d15)#+str(d16)
    ###print("datoOriginal es:  ",datoOriginal)
    return datoOriginal
#convierte un caracter ascii y devuelve un haming 1511
def char_hamming1511(c):
    
       
    datobin= np.zeros(11)#guarda el ascii en binario
    envio= np.zeros(15) #vector 15 caractereres con hamming
        #Ruido= np.zeros(15) #vector con ruido
        #envioCorregido= np.zeros(15) #vector ya corregido
    
    
    """CONVIERTE A ASCII"""
    numero= ord(c)
    """CONVIERTE A BINARIO"""
    binario= bin(numero) 
    
    resta=11-(len(binario))
    """Datobin Guarda el codigo binario del ascii"""
    for i in range(2, len(binario)):
        ###print("datobin",resta+i-1,"    i",i)
        datobin[resta+i]=binario[i]
        
    
    ###print(binario,"asi los guarda", datobin,"   resta",resta )

    """calcula la paridad de los datos"""
    envio=hamming1511(datobin)
    
    return envio
        
    
def serial_Ascii (texto):
    memoria=0

    
    ###print("\n\r DATO RECIBIDO        ERROR EN       DATO CORREGIDO      CARACTER RECIBIDO\n")
    
    mensajeParaHill=""

    datoRecibido= np.zeros(15)
    envioCorregido= np.zeros(15)


    texto = input("Introduzca los bits: ")
    texto = texto.upper().strip().replace("", "")


    nbits=len(texto) #calcula la cantidad de bits recibidos

    nchar=nbits/15   #calcula la cantidad de caracteres recibidos

    ###print(nbits,nchar)


    # contadores para serie a paralelo
    cuenta0=0
    cuenta1=15
    mensaje=""

    # convertidor serie a paralelo
    for i in range(0, int( nchar)):
    
        for i in range(cuenta0, cuenta1):
        
            mensaje= mensaje +str(texto[i])
        
        
    
        cuenta0=cuenta1
        cuenta1=cuenta1+15
    
        #se obtiene el dato en paralelo
        datoRecibido=mensaje
        mensaje=""
        #se detecta el error por medio de los bits de paridad
    
        valorRuido=deteccion_de_error(datoRecibido)
    
        #se crea una copia del dato recibido en envioCorregido
        for n in range(15):
            envioCorregido[n]= datoRecibido[n]
    
        #se corrigue el error si es que existe
    
        if(valorRuido>0):
            envioCorregido[valorRuido-1]=not(envioCorregido[valorRuido-1])
        
    
        caracterAsciiBin= recolecta_el_dato(envioCorregido)
        caracterAscii= chr(convertir_a_int(caracterAsciiBin))
        mensajeParaHill=mensajeParaHill+str(caracterAscii)
        
        if (caracterAscii == ',' and memoria==0):
             memoria=1
    
        ###if(memoria ==0):
        
            ###print(datoRecibido,"        ",valorRuido,"        ",ipr(envioCorregido),"             ",caracterAscii)
   
    
    return mensajeParaHill