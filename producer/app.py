import time

from confluent_kafka import Producer
from faker import Faker

# Configurações do Kafka
bootstrap_servers = 'localhost:9092'
topic = 'meu-topico'

# Configurações do produtor
produtor_config = {
    'bootstrap.servers': bootstrap_servers
}

# Criar o produtor
produtor = Producer(produtor_config)

# Função para enviar mensagens ao Kafka


def enviar_mensagem():
    faker = Faker()

    while True:
        nome = faker.name()
        mensagem = nome

        # Enviar a mensagem ao Kafka
        produtor.produce(topic=topic, value=mensagem, callback=callback)

        # Aguardar a confirmação de envio da mensagem
        produtor.flush()

        # Aguardar meio segundo antes de enviar a próxima mensagem
        time.sleep(0.5)

# Função de callback para confirmação de envio da mensagem


def callback(err, msg):
    if err is not None:
        print(f'Erro ao enviar a mensagem: {err}')
    else:
        print(f'Mensagem enviada: {msg.value().decode("utf-8")}')


# Iniciar o envio de mensagens
enviar_mensagem()
