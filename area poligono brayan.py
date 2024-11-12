def calculo_area (poligono,base=0,altura=0,lado=0):
    if poligono == "triangulo":
        return (base * altura)/2
    elif poligono == "cuadrado":
        return lado*lado    
    elif poligono == "rectangulo":
        return base*altura 
    else: 
        return ("no pertenece a los poligonos planteados")

poligono=input("Ingresa el poligono a calcular: ")

if poligono == "triangulo": 
    base=float(input(" digita el valor de la base: "))
    altura=float(input(" digita el valor de la altura: "))
    area=calculo_area(poligono,base=base,altura=altura)
elif poligono == "cuadrado":
    lado=float(input("digite el valor del lado"))
    lado=float(input("digite el valor del lado"))
    area=calculo_area(poligono,lado=lado)
elif poligono == "rectangulo":
    base=float(input("digite el valor de la base"))
    altura=float(input("digite el valor de la altura"))
    area=calculo_area(poligono,base=base,altura=altura)
else:
    area="Poligono no pertence al planteado"


print("El area del poligono es: ",area)



