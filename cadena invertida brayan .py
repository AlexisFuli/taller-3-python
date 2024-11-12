def texto_invertido(cadena):
    inversa=""
    itera = len(cadena) -1
    while itera >= 0:
        inversa = inversa+cadena [itera]
        itera = itera-1
    return inversa 

texto = input ("Ingresa el texto que desea invertir: ")
print("El texto invertido es: ", texto_invertido(texto))



