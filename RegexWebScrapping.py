import re
import csv

def cargar_html(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        return f.read()

def procesar_buffer(entrada, tamano_buffer):
    entrada = list(entrada)
    inicio_buffer = 0
    while True:
        fin = inicio_buffer + tamano_buffer
        buffer = entrada[inicio_buffer:fin]
        es_final = fin >= len(entrada)

        yield buffer, es_final

        if es_final:
            break

        inicio_buffer += tamano_buffer

def extraer_productos(html):
    regex_nombre = r"<h4>(.*?)</h4>"
    regex_imagen = r"<img src=\"(.*?)\" alt=\"product-image\""
    nombres = re.findall(regex_nombre, html)
    imagenes = re.findall(regex_imagen, html)
    return zip(nombres, imagenes)

def exportar_csv(productos, archivo_salida):
    with open(archivo_salida, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Nombre del Producto', 'URL de la Imagen'])
        writer.writerows(productos)

# Uso de las funciones
archivo_html = "./pagina_html_pacifiko.html"
html_completo = cargar_html(archivo_html)

html_procesado = ""
tamano_buffer = 200
for buffer, es_final in procesar_buffer(html_completo, tamano_buffer):
    html_procesado += "".join(buffer)  # Acumulamos el contenido procesado del buffer

productos = extraer_productos(html_procesado)
exportar_csv(productos, "productos.csv")
