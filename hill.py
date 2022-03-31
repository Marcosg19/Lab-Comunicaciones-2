#import math
import numpy as np;
#import random
import hamming
import cifradohill
import descifradohill


def cifrado1(texto):

    #texto = input("Introduzca el texto: ");

    #print("\n El texto a enviar es:   ",texto,"\n")

    texto=cifradohill.EncripHamming(texto) # CONVIERTE A HILL
    #print("Texto con cifrado hill:    ",texto,"\n")
    mensaje=""

    #print("\n\rEnvio        codigo hamming1511       Envio con ruido aleatorio\n")

    memoria=0


    for c in texto:
    
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
    
        # se imprimer valores
        # if (c == ',' and memoria==0):
        #     memoria=1
    
        # if(memoria ==0):
        #     print("  ",c,"        ",hamming.ipr(envio),"       ",hamming.ipr(Ruido))
    
    
    
    return mensaje
    #print("\n El mensaje con seguridad hill y correccion de error Hamming es:\r\n\n",mensaje)


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
    
    
def descifrado1(texto):

    


    texto=serial_to_parAscii(texto)

    TextoDescodificado=descifradohill.descodhill26(texto)


    texto=texto[0:texto.find(',')]

    #print("\n\n\r El dato con cifrado hill es:     ",texto)



    cuenta=0
    for c in texto:
        cuenta=cuenta+1
        if(c==" "):
            TextoDescodificado = TextoDescodificado[:(cuenta-1)] + ' ' + TextoDescodificado[(cuenta-1):]