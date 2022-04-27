import numpy as np;
import math

modulo=26

def imprimir_matriz(charar): #funcion utilizada para imprimir matrices
    for i in range (2):
        for j in range (2):
            print(int(charar[i][j]), "\t", end='')
        print("\n")



# una matriz se define [filas ,columnas]

#Solicitar datos
def codhill27(Texto):
    

    Texto = Texto.upper().strip().replace(" ", "")
    longitud=len(Texto)
    #Texto = Texto.upper()


    if len(Texto)% 2  != 0:
        Texto=Texto+'1'

    #print(Texto)

    Clave = np.empty((2, 2)); 

    Clave[0][0]=11
    Clave[0][1]=8
    Clave[1][0]=3
    Clave[1][1]=7

    m_crip=np.zeros((math.ceil(len(Texto)/2),2))  #calcula el numero de filas, col 2



    #imprimir_matriz(Clave)
    diccionario_letras = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'Ñ': 14,'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, ' ':' '}
    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ "

    cipher=""
    i=0
    j=0
    while True:
        try:
            if (np.size(m_crip) / 2 == j):
                    break
            #print(Texto[i]," - ",Texto[i+1]," - ",diccionario_letras[Texto[i]])
            m_crip[j][0]=diccionario_letras[Texto[i]]
            m_crip[j][1]=diccionario_letras[Texto[i+1]]
            i+=2
            j+=1

        except:
            print(Texto[i])
            m_crip[j][0] = diccionario_letras[Texto[i]]
            break

        #for i in range(m_crip.length)

    c1 = 0
    c2 = 0
    m1 = 0
    m2 = 0

    cipher=np.zeros(m_crip.shape)

    mensajehill=""
    #print("Texto Cifrado")

    for i in range(int(np.size(m_crip)/2)):

        m1 = m_crip[i][0]
        m2 = m_crip[i][1]
        c1 = Clave[0][0]*m1 + Clave[1][0]*m2
        c2 = Clave[0][1]*m1 + Clave[1][1]*m2
        cipher[i][0]=c1%modulo
        cipher[i][1]=c2%modulo
    
        mensajehill= mensajehill+str(abecedario[int(cipher[i][0])])+str(abecedario[int(cipher[i][1])])
    
        
        #print(int(cipher[i][0]), " - " , int(cipher[i][1]))
        # print(abecedario[int(cipher[i][0])],abecedario[int(cipher[i][1])])



    mensajehill=mensajehill+str(',')+str(longitud)
    return mensajehill




def EncripHamming(Texto):
    
    Texto = Texto.upper()
 
    resHamming = Texto.replace(" ", "")
    
    resHamming = codhill27(resHamming)
    
    #index = resHamming.find(' ')
    #resHamming = resHamming[:index] + ' ' + resHamming[index:]
    cuenta=0
    for c in Texto:
        cuenta=cuenta+1
        if(c==" "):
            resHamming = resHamming[:(cuenta-1)] + ' ' + resHamming[(cuenta-1):]
            

        
    
    
    # cartera=""
    # envio=""
    # cuenta=0
    
    # for c in Texto:
    #     cuenta=cuenta+1
        
    #     print (c,"   ", cuenta)
        
        
    #     if(c!=" "):
            
    #         cartera=cartera+c
    #     else:
    #         #print (cartera)
    #         envio=codhill26(cartera)
    #         cartera=""
        
    #     if(cuenta==len(Texto)):
    #          #print (cartera)
    #          envio=codhill26(cartera)
    #          cartera=""
        
        
        
        
    # pass
    
    
    return resHamming
    
    

#entrada = input("Por favor introduzca el texto a Cifrar: ")

#print(EncripHamming(entrada))