# M2-RegexWebScrapping
[M2] Actividad: Web Scraping con Expresiones Regulares - Diseño de Lenguajes de Programación

### Descripción del Proyecto
Este script en Python procesa un archivo HTML para extraer información estructurada como nombres de productos y URLs de imágenes. Los datos extraídos se exportan a un archivo CSV. Es ideal para tareas de scraping ligero y manejo eficiente de datos.

#### Cómo Funciona
- Carga del HTML: Se utiliza la función cargar_html para leer el contenido del archivo HTML.
- Procesamiento por buffers: La función procesar_buffer divide el contenido en bloques pequeños para manejar archivos grandes.
- Extracción de productos: Con expresiones regulares, se identifican nombres de productos y URLs de imágenes.
- Exportación a CSV: Los datos extraídos se escriben en un archivo CSV con columnas organizadas.

#### Ejemplo de Uso
- Asegúrate de tener un archivo HTML que será el que se analizará, en el mismo directorio que el script.
- Ejecuta el script.
- Se generará un archivo llamado productos.csv con el siguiente contenido:


#### Ejemplo de Salida (CSV):

```csv
Nombre del Producto,URL de la Imagen
"Producto 1","https://example.com/imagen1.jpg"
"Producto 2","https://example.com/imagen2.jpg"
"Producto 3","https://example.com/imagen3.jpg"
```

#### Requisitos
- Python 3.7+
- Archivo HTML estructurado con los elementos necesarios.

#### Cómo Ejecutarlo
- Clona este repositorio o descarga el archivo Python.
- Asegúrate de que el archivo HTML esté en el mismo directorio que el script.
- Corre el script con:
```
python RegexWebScrapping.py
```
- Encuentra el archivo productos.csv en el mismo directorio.

#### Notas
Este script está diseñado para trabajar con HTML bien estructurado (la regex fue ajustada específicamente para este HTML). Asegúrate de que las etiquetas y clases coincidan con las expresiones regulares.
