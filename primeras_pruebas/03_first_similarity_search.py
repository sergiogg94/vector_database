#! /home/sergiogg/Documentos/personal_projects/vector_db/vdb_env/bin/python3

import spacy
from pymilvus import connections, Collection, MilvusException

# Cargar modelo
model = spacy.load('es_core_news_sm')

# Conectar a la BD de milvus
connections.connect(host='localhost', port='19530')

try:
    # Entrada del usuario par buscar similaridad
    while True:
        user_input=input('\nIntroduzca la descripción del producto que busca' \
                        + '(o escriba "exit" para salir):\n')

        # Quitar si se escribe exit
        if user_input.lower() == 'exit':
            break

        # Vectorizar la entrada del usuario
        query_vector = model(user_input).vector.tolist()

        # Definir parámetros de busqueda
        search_params = {
            'metric_type': 'L2',
            'offset': 0,
            'ignore_growing': False,
            'params': {'nprobe': 10}
        }

        # Conectar a la colección
        collection = Collection('first_test_spacy')

        # Busqueda de vectores más cercanos
        resultado = collection.search(
            data = [query_vector],
            anns_field='description_vector',
            param=search_params,
            limit=3,
            output_fields=['description','category','competitor']
        )

        # Imprimir resultado
        for idx, hit in enumerate(resultado[0]):
            score = hit.distance
            description = hit.entity.description
            cat = hit.entity.category
            cp = hit.entity.competitor
            print(f'{idx + 1}. Producto: {description}. Categoria: {cat}. ' \
                    + f'Competidor: {cp} (distancia: {score})')


except MilvusException as e:
    # Imprimir erro
    print(e)

finally:
    # Desconectar de la BD
    connections.disconnect(alias='localhost')