import hamming
import numpy as np;
import math

modulo=26


def imprimir_matriz(charar): #funcion utilizada para imprimir matrices
    for i in range (2):
        for j in range (2):
            print(int(charar[i][j]), "\t", end='')
        print("\n")



#Descifrar
    #Solicitar Datos
    
def descodhill26(Texto):
    
    ncoma =Texto.find(',')
    gia = Texto

    Texto=Texto[0:ncoma]
    gia=gia[ncoma+1:len(gia)]
    #Texto = input ("Por favor introduzca el texto a descifrar: ");
    #print(Texto,"     ",gia)

    #Texto = input ("Por favor introduzca el texto a descifrar: ");
    #print(Texto)
    Texto = Texto.upper().replace(" ", "")
    #print("Por favor introduzca la clave (matriz 2x2)");
    Clave = np.empty((2, 2))
    #msj = "";
    m_crip=np.zeros((math.ceil(len(Texto)/2),2))

    Clave[0][0]=11
    Clave[0][1]=8
    Clave[1][0]=3
    Clave[1][1]=7

    #imprimir_matriz(Clave)

    #diccionario_letras = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25, ' ': 26}
    diccionario_letras = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'Ñ': 14,'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, '1':27, '2':28, '3':29, '4':30, '5':31, '6':32, '7':33, '8':34, '9':35, ' ':' '}
    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ123456789 "
    #abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

    #Inversa de una matriz A^-1=1/[A] * (A*)^T
    #Sacar determinantes
    Determinante=Clave[0][0]*Clave[1][1]-Clave[0][1]*Clave[1][0]
    Adjunta = np.zeros((2,2))
    Adjunta[0][0] = Clave[1][1]
    Adjunta[1][1] = Clave[0][0]
    Adjunta[0][1] = -1*Clave[1][0]
    Adjunta[1][0] = -1*Clave[0][1]

    TAdj = np.zeros((2,2))
    TAdj[0][0] = Adjunta[0][0]
    TAdj[1][1] = Adjunta[1][1]
    TAdj[0][1] = Adjunta[1][0]
    TAdj[1][0] = Adjunta[0][1]

    Determinante=Determinante%modulo
    InClave = np.zeros((2,2))
    InClave[0][0] = ((1/Determinante)*TAdj[0][0])%modulo
    InClave[0][1] = ((1/Determinante)*TAdj[0][1])%modulo
    InClave[1][0] = ((1/Determinante)*TAdj[1][0])%modulo
    InClave[1][1] = ((1/Determinante)*TAdj[1][1])%modulo

    i = 0
    j = 0
    while True:
        try:
            if (np.size(m_crip)/2 == j):
                break
            #print(Texto[i]," - ",Texto[i+1])
            m_crip[j][0]=diccionario_letras[Texto[i]]
            m_crip[j][1]=diccionario_letras[Texto[i+1]]
            i+=2
            j+=1
            
        except:
            #print(Texto[i])
            m_crip[j][0] = diccionario_letras[Texto[i]]
            break

    #for i in range(m_crip.length)

    c1 = 0
    c2 = 0
    m1 = 0
    m2 = 0

    descipher=np.zeros(m_crip.shape)
    mensajehill=""
    #print("Texto Descifrado: ")

    for i in range(int(np.size(m_crip)/2)):
        m1 = m_crip[i][0]
        m2 = m_crip[i][1]
        c1 = InClave[0][0]*m1 + InClave[1][0]*m2
        c2 = InClave[0][1]*m1 + InClave[1][1]*m2
        descipher[i][0]=c1%modulo
        descipher[i][1]=c2%modulo
    
        mensajehill= mensajehill+str( abecedario[int(descipher[i][0])])+str(abecedario[int(descipher[i][1])])
        #print(int(cipher[i][0]), " - " , int(cipher[i][1]))
        #print(abecedario[int(descipher[i][0])],"",abecedario[int(descipher[i][1])]," ", end='')   

    #print(mensajehill)


    numero=int(gia)
    mensajehill=mensajehill[0:numero]



    return mensajehill


def serial_to_parAscii (texto):
    memoria=0

    
    #print("\n\r DATO RECIBIDO        ERROR EN       DATO CORREGIDO      CARACTER RECIBIDO\n")
    
    mensajeParaHill=""

    datoRecibido= np.zeros(15)
    envioCorregido= np.zeros(15)


    #texto = input("Introduzca los bits: ")
    texto = texto.upper().strip().replace(" ", "")


    nbits=len(texto) #calcula la cantidad de bits recibidos

    nchar=nbits/15   #calcula la cantidad de caracteres recibidos

    #print(nbits,nchar)


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
    
        valorRuido=hamming.deteccion_de_error(datoRecibido)
    
        #se crea una copia del dato recibido en envioCorregido
        for n in range(15):
            envioCorregido[n]= datoRecibido[n]
    
        #se corrigue el error si es que existe
    
    
    
        if(valorRuido>0):
            envioCorregido[valorRuido-1]=not(envioCorregido[valorRuido-1])
        
    
        caracterAsciiBin= hamming.recolecta_el_dato(envioCorregido)
        caracterAscii= chr(hamming.convertir_a_int(caracterAsciiBin))
        mensajeParaHill=mensajeParaHill+str(caracterAscii)
        
        # if (caracterAscii == ',' and memoria==0):
        #     memoria=1
    
        # if(memoria ==0):
        
        #     print(datoRecibido,"        ",valorRuido,"        ", hamming.ipr(envioCorregido),"             ",caracterAscii)
   
    
    return mensajeParaHill


#entrada = input("Por favor introduzca el texto a Descifrar: ")

#print(descodhill26(entrada))