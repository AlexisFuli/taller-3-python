def eliminar_caracteres (str1,str2):
    out1=""
    out2=""
    for texto in str1:
        if texto not in str2 and texto not in out1:
            out1=out1+texto  
    for texto in str2: 
        if texto not in str1 and texto not in out2:
            out2=out2+texto
    print("Caracteres en str1 pero que no estan en out1: ", out1 )
    print ("Caracteres  en str2 pero que no estan en out2: ",out2 )
str1= input("Ingrese la primera cadena : ")
str2= input("Ingrese la segunda cadena : ")
eliminar_caracteres(str1,str2)  


    