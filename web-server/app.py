from flask import Flask
from google.cloud import pubsub_v1
import time
import random

# Configura el ID de tu proyecto
PROJECT_ID = "pry-pruebas"

# Configura el nombre del tema al que deseas publicar el mensaje
TOPIC_NAME = "topic-videos"


app = Flask(__name__)

@app.route('/')
def home():
    random_value = random.uniform(0, 0.5)

    ###########################################################################
    # Crea un cliente de Pub/Sub
    publisher = pubsub_v1.PublisherClient()

    # Formatea el nombre completo del tema
    topic_path = publisher.topic_path(PROJECT_ID, TOPIC_NAME)

    # El mensaje que deseas publicar
    mensaje = b"Mensaje de prueba."

    # Publica el mensaje en el tema
    future = publisher.publish(topic_path, mensaje)

    # Espera a que el mensaje se publique completamente
    future.result()
    ###########################################################################
    time.sleep(random_value)
    return str(random_value)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)