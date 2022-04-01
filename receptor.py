import cifdefHill
import cifradocesar
import cifradovigenere



def Desencriptar(texto):

    #texto = input("Introduzca el texto: ");
    texto=texto
    
    npunto= texto.find(".")
    
    indice= texto[0:npunto]
    
    
    texto=texto[npunto+1:len(texto)]
    
    
    #print(npunto, "  " , indice ,"     ", texto)
    
    #print (indice)
    
    if (indice=='1'):
        
        texto=cifdefHill.descifrado(texto)
        
    elif (indice=='2'):
        #print("aqui")
        texto=cifradocesar.descifradocesar(texto)
    elif (indice=='3'):
        texto=cifradovigenere.descifrado3(texto)

    return texto


texto = input("Desencriptar: ")

print(Desencriptar(texto))