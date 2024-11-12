

def triangulo_2D(tamano):
    for i in range (1,tamano+1):
        print("*" * i) 
    

def cuadrado_2D(tamano):
    for i in range(tamano):
        print("* " * tamano)
        

poligono=input("Ingresa el poligono que desea graficar: ").strip().lower()
tamano=int(input("Ingrese el tamano del poligono: "))

if poligono=="cuadrado":
    cuadrado_2D(tamano)

elif poligono=="triangulo":
    triangulo_2D(tamano)

