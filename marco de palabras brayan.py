def marco_de_palabras(texto):
    texto = input("Ingresa el texto: ")

    palabras = texto.split()  
    
    longitud = max(len(palabra) for palabra in palabras)
    
    marco = "*" * (longitud + 4)  
    
    print(marco)
    
    for palabra in palabras:
        print("* " + palabra.ljust(longitud) + "*") 
    
    print(marco)

marco_de_palabras("")