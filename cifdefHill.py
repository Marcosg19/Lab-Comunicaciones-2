import hamming
import cifradohill
import descifradohill
import numpy as np



def cifrado(texto):

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



def descifrado(texto):

    

    texto=descifradohill.serial_a_Ascii(texto)

    TextoDescodificado=descifradohill.descodhill26(texto)


    texto=texto[0:texto.find(',')]

    #print("\n\n\r El dato con cifrado hill es:     ",texto)



    cuenta=0
    for c in texto:
        cuenta=cuenta+1
        if(c==" "):
            TextoDescodificado = TextoDescodificado[:(cuenta-1)] + ' ' + TextoDescodificado[(cuenta-1):]
            


    #print("\n\n\r El mensaje descodificado es:  ",TextoDescodificado)

    return TextoDescodificado


#texto= input('Ingrese mensaje a cifrar: ')
#print(cifrado(texto))

#print(descifrado(input('Ingrese bits a descifrar: ')))