def numero_armstrong(numero):
    valor = 0
    for n in str(numero):
        valor += int(n) ** len(str(numero))
        print(valor)
    if numero == int(numero):
        print(numero, "El numero es armstrog")
    else:
        print(numero, "El numero no es armstrong")

valor = int(input("Ingrese un numero: "))
numero_armstrong(valor)









     
        

        

    