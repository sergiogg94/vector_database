import spacy
import pandas as pd

nlp = spacy.load('es_core_news_sm')

ejemplos_chatgpt = [
    ('Televisión LED 55" 4K Ultra HD Smart TV', 'Electrónica'),
    ('Lavadora de carga frontal 9 kg con tecnología Inverter', 'Electrodomésticos'),
    ('Laptop con procesador Intel i5, 8GB RAM, 256GB SSD', 'Informática'),
    ('Smartphone con pantalla de 6.5" y cámara triple 48MP', 'Telefonía'),
    ('Auriculares inalámbricos con cancelación de ruido', 'Accesorios'),
    ('Cámara digital réflex con lente 18-55mm', 'Fotografía'),
    ('Tableta gráfica con lápiz táctil', 'Tecnología'),
    ('Microondas digital con grill 23L', 'Electrodomésticos'),
    ('Refrigerador de doble puerta No Frost 500L', 'Electrodomésticos'),
    ('Reloj inteligente con monitor de frecuencia cardíaca', 'Tecnología'),
    ('Cafetera de cápsulas con espumador de leche', 'Cocina'),
    ('Consola de videojuegos 1TB con mando inalámbrico', 'Videojuegos'),
    ('Aspiradora robot con mapeo inteligente', 'Hogar'),
    ('Máquina de coser portátil con 12 puntadas', 'Hogar'),
    ('Horno eléctrico con convección 45L', 'Cocina'),
    ('Licuadora de alta potencia 1500W', 'Cocina'),
    ('Plancha de vapor vertical', 'Hogar'),
    ('Barra de sonido con subwoofer inalámbrico', 'Electrónica'),
    ('Router inalámbrico de doble banda', 'Tecnología'),
    ('Impresora multifuncional láser', 'Oficina'),
    ('Taladro inalámbrico 20V con 2 baterías', 'Herramientas'),
    ('Set de maletas rígidas 3 piezas', 'Viaje'),
    ('Colchón queen size de espuma viscoelástica', 'Hogar'),
    ('Silla ergonómica de oficina con soporte lumbar', 'Mobiliario'),
    ('Escritorio de oficina en L', 'Mobiliario'),
    ('Lámpara de escritorio LED regulable', 'Iluminación'),
    ('Bicicleta estática plegable con monitor de pulso', 'Ejercicio'),
    ('Gafas de realidad virtual con mando', 'Tecnología'),
    ('Monitor de 27" Full HD con panel IPS', 'Informática'),
    ('Altavoz Bluetooth portátil con resistencia al agua', 'Electrónica'),
    ('Cepillo de dientes eléctrico con cabezales de repuesto', 'Cuidado personal'),
    ('Freidora de aire sin aceite 5.5L', 'Cocina'),
    ('Set de cuchillos de cocina de acero inoxidable', 'Cocina'),
    ('Sartén antiadherente de 28 cm', 'Cocina'),
    ('Olla de presión eléctrica multifuncional 6L', 'Cocina'),
    ('Máquina para hacer palomitas retro', 'Cocina'),
    ('Cortapelos recargable con múltiples cabezales', 'Cuidado personal'),
    ('Estación meteorológica digital', 'Hogar'),
    ('Termómetro digital sin contacto', 'Salud'),
    ('Humidificador ultrasónico con luz nocturna', 'Hogar'),
    ('Ventilador de torre con control remoto', 'Hogar'),
    ('Tostadora de acero inoxidable 2 rebanadas', 'Cocina'),
    ('Reproductor de DVD con HDMI', 'Electrónica'),
    ('Cámara de seguridad inalámbrica 1080p', 'Seguridad'),
    ('Cerradura inteligente con huella digital', 'Seguridad'),
    ('Proyector de cine en casa 4K', 'Electrónica'),
    ('Teclado mecánico retroiluminado', 'Informática'),
    ('Ratón inalámbrico ergonómico', 'Informática'),
    ('Mochila para portátil 15.6" impermeable', 'Accesorios'),
    ('Telescopio astronómico con trípode', 'Ocio'),
    ('Mando a distancia universal para TV y dispositivos', 'Electrónica'),
    ('Dispensador de agua fría y caliente', 'Hogar'),
    ('Secadora de cabello iónica', 'Cuidado personal'),
    ('Báscula de baño digital con análisis corporal', 'Salud'),
    ('Pulsera de actividad con GPS', 'Tecnología'),
    ('Juego de sábanas de algodón 400 hilos', 'Hogar'),
    ('Cama para mascotas grande con cojín', 'Mascotas'),
    ('Casco de bicicleta con luz trasera', 'Deportes'),
    ('Kit de primeros auxilios 100 piezas', 'Salud'),
    ('Detector de humo con alarma sonora', 'Seguridad'),
    ('Botiquín de emergencias con compartimentos', 'Salud'),
    ('Set de jardinería con herramientas y guantes', 'Jardinería'),
    ('Parrilla eléctrica de interior', 'Cocina'),
    ('Máquina de afeitar eléctrica con cabezal pivotante', 'Cuidado personal'),
    ('Guitarra acústica de madera con funda', 'Música'),
    ('Micrófono para PC con trípode', 'Tecnología'),
    ('Tarjeta gráfica Nvidia 8GB', 'Informática'),
    ('Unidad SSD externa 1TB USB 3.1', 'Informática'),
    ('Cargador portátil 20,000 mAh', 'Accesorios'),
    ('Auriculares gaming con micrófono', 'Videojuegos'),
    ('Cámara web HD 1080p', 'Tecnología'),
    ('Controlador MIDI USB para producción musical', 'Música'),
    ('Set de herramientas con maletín 128 piezas', 'Herramientas'),
    ('Dron con cámara 4K y estabilizador', 'Ocio'),
    ('Patinete eléctrico plegable', 'Transporte'),
    ('Andador para bebé con juguetes', 'Infantil'),
    ('Silla de auto para niños con protección lateral', 'Infantil'),
    ('Monitor de bebé con cámara y audio', 'Seguridad'),
    ('Reloj despertador digital con proyector', 'Hogar'),
    ('Máquina de pasta casera', 'Cocina'),
    ('Kit de manicura eléctrica', 'Cuidado personal'),
    ('Gafas de sol polarizadas', 'Moda'),
    ('Guantes de entrenamiento con muñequera', 'Deportes'),
    ('Pelota de yoga antideslizante', 'Ejercicio'),
    ('Bicicleta de montaña con suspensión delantera', 'Deportes'),
    ('Monopatín clásico de madera', 'Ocio'),
    ('Linterna LED recargable', 'Accesorios'),
    ('Prismáticos de largo alcance', 'Ocio'),
    ('Caja fuerte electrónica', 'Seguridad'),
    ('Batería recargable AA 12 pack', 'Accesorios'),
    ('Juego de malabares 3 pelotas', 'Ocio'),
    ('Plancha para el pelo con placas de cerámica', 'Cuidado personal'),
    ('Sandwicheras para 2 sandwiches', 'Cocina'),
    ('Manta eléctrica con control de temperatura', 'Hogar'),
    ('Hervidor de agua de acero inoxidable', 'Cocina'),
    ('Robot de cocina multifunción', 'Cocina'),
    ('Almohada cervical de espuma viscoelástica', 'Hogar'),
    ('Kit de depilación con cera y accesorios', 'Cuidado personal'),
    ('Espejo de aumento con luz LED', 'Cuidado personal'),
    ('Termo para café de acero inoxidable', 'Accesorios')
]

descriptions = [p[0] for p in ejemplos_chatgpt]
cats = [p[1] for p in ejemplos_chatgpt]
competitors = ['walmart']*50 + ['soriana']*50
id_list = range(1,101)

vector_list = []


for desc, cat in ejemplos_chatgpt:
    vector = nlp(desc).vector.tolist()
    vector_list.append(vector)


df = pd.DataFrame({
    'id': id_list,
    'description_vector': vector_list,
    'description': descriptions,
    'category': cats,
    'competitor': competitors
})

df.to_csv('./dummy_data/first_test.csv', index=False)