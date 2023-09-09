import re  
import requests
import re

#Obtiene la URL que sera el objetivo
websiete = input("Ingresa la url de la pagina objetivo: \n")

print("Esta es la pagina objetivo: " + websiete)

#Realiza una peticion get
resultado =  requests.get(websiete)

#Convierte la carga util en texto para poder buscar patrones 
html = resultado.text

#Busca el indice donde se encuentra la coincidencia del string "<tittle>"
title_index = html.find("<title>")

#Aumenta la longitud del inidice donde se encontro la coincidencia para encontrar el valor
#Donde comenzara la lectura del texto
start_index = title_index + len("<title>")

#Busca el tag de cierre
end_index = html.find("</title>")

#Realiza un recorte de la cadena de toda la estructura del HTML para encontrar el texto que
#se encuentra en ambas posiciones
print("El contenido de la etiqueta <title> es: "+ html[start_index:end_index])

#Obtiene elementos con tag "<link>" con una expresion regular
for elemento in re.findall("<link(.*?)>", html):
    print("El contenido de la etiqueta <link> es: "+ elemento)