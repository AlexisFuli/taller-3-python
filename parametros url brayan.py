
def obtener_parametros(url):
    parametros = []
    i = 0
    while i < len(url):
        if url[i] == "=":
            i += 1  
            valor = ""
            
            while i < len(url) and url[i] != "&" and url[i] != " ":
                valor += url[i]
                i += 1
            
            if valor != "":
                parametros.append(valor)
        else:
            i += 1  

    return parametros

url_usuario = input("Introduce la URL: ")

parametros = obtener_parametros(url_usuario)

print("Parámetros encontrados:")
print(parametros)