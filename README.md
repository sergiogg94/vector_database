# Vector database

Exploraciones del funcionamiento de milvus para generar una base de datos
vectorial y realizar búsquedas semánticas.

## Contenedor de la base de datos

Para levantar el contenedor Docker de la base de datos correr:

<pre><code>```bash
docker compose up -d
```
</code></pre>

Esto generará 4 contenedores docker, 3 que necesita la base de datos standalone
y 1 que genera la interface gráfica Attu para gestionar la base de datos.

Para entrar a la interface gráfica de Attu ir a la dirección:
https://localhost:8000

## Primeras pruebas

Dentro de la carpeta de primeras pruebas hice un test de una base de datos
con vectores dummy codificados con spacy y creando la colección desde la Attu.

## TO DO

- Construir desde código colecciones para una base de datos de productos
vendidos online.
- Con webscraping generar una base de productos para vectorizar y guardar.
- Con Gradio crear una interface de usuario que busque productos según una
frase query.