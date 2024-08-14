#! /home/sergiogg/Documentos/personal_projects/vector_db/vdb_env/bin/python3

from pymilvus import (
    connections,
    Collection,
    FieldSchema,
    CollectionSchema,
    DataType,
    utility,
    MilvusException
)

## Conectar a la BD de milvus
connections.connect('default', host='localhost', port='19530')


## Nombre de la colección
collection_name = 'products'


## Campos para el esquema
# SKU
sku_field = FieldSchema(
    name = 'sku',
    dtype = DataType.VARCHAR,
    max_length = 14,
    description = 'SKU unico del producto',
    is_primary = True
)

# Vector
vector_field = FieldSchema(
    name = 'vector',
    dtype = DataType.FLOAT_VECTOR,
    dim = 384,
    description = 'Vector de la descripcion del producto'
)

# Descripcion
desc_field = FieldSchema(
    name = 'description',
    dtype = DataType.VARCHAR,
    max_length = 200,
    description = 'Descripcion del producto'
)

# Competidor
comp_field = FieldSchema(
    name = 'competitor',
    dtype = DataType.VARCHAR,
    max_length = 50,
    description = 'Competidor que vende el producto'
)

# Categoria
cat_field = FieldSchema(
    name = 'category',
    dtype = DataType.VARCHAR,
    max_length = 100,
    description = 'Categoria del producto'
)

## Definir el esquema de la colección
schema = CollectionSchema(
    fields = [sku_field,vector_field,desc_field,comp_field,cat_field],
    description = 'Vectores de descipciones de productos vendidos online'
)

## Parámetros para el index
index_params = {
    'index_type': 'IVF_FLAT', # Busqueda de vectores con FAISS
    'metric_type': 'COSINE', # Similitud coseno
    'params': {'nlist':128} # Parametros para FAISS
}

# TO DO: Agregar el indice a la colección en el try.


try:
    # Checar si la colección ya existe
    if utility.has_collection(collection_name):
        print(f'Ya existe una colección llamada {collection_name}')
        colecciones = utility.list_collections()
        print('La base de datos contiene las siguientes colecciones:')
        print(colecciones)
    else:
        # Crear colección
        coleccion = Collection(name=collection_name, schema=schema)
        print(f'La colección {collection_name} fue creada correctamente.')

        # Crear index para la colección
        coleccion.create_index(
            field_name='vector',
            index_params=index_params,
            timeout=None
        )

        # Cargar la colección a memoria
        coleccion.load()

        print(f'Se creó y se cargó la colección {collection_name} con las ' \
                + 'siguientes características')
        print(coleccion.describe())


except MilvusException as e:
    print(e)

finally:
    connections.disconnect(alias='localhost')