def conversor_tiempo(Dias, Horas, Minutos, Segundos):
    Milisegundos= (Dias*86400000)+(Horas*3600000)+(Minutos*60000)+(Segundos*1000)
    int = (Dias, Horas, Minutos, Segundos)
    return Milisegundos

Dias = int(input("Ingresa la cantidad de dias: "))
print ( "Los milisegundos de los dias es: ",Dias*86400000)
Horas = int(input("Ingresa la cantidad de horas: "))
print ("Los milisegundos de las horas es:",Horas*3600000)
Minutos = int(input("Ingresa la cantidad de minutos: "))
print ("Los milisegundos de los minutos es:",Minutos*60000)
Segundos = int (input("Ingresa la cantidad de segundos: "))
print ("Los milisegundos de los segundos es:",Segundos*1000)

valrototal=conversor_tiempo(Dias,Horas,Minutos,Segundos)

print ("El valor total de los valores que proporcionaste es igual a: ",valrototal)

    