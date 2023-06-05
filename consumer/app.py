import threading

from confluent_kafka import Consumer, KafkaError
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Variável global para armazenar as mensagens
mensagens = []
mensagens_lock = threading.Lock()

# Configurações do Kafka
bootstrap_servers = 'localhost:9092'
topic = 'meu-topico'

# Configuração do consumidor
consumidor_config = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'meu-grupo',
    'auto.offset.reset': 'earliest'
}

# Criar o consumidor
consumidor = Consumer(consumidor_config)
consumidor.subscribe([topic])

# Função para consumir mensagens do Kafka


def consumir_mensagens():
    while True:
        mensagem = consumidor.poll(1.0)

        if mensagem is None:
            continue
        if mensagem.error():
            if mensagem.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(f'Erro ao consumir a mensagem: {mensagem.error().str()}')
                break

        with mensagens_lock:
            mensagem_dict = {
                'tópico': mensagem.topic(),
                'partição': mensagem.partition(),
                'offset': mensagem.offset(),
                # 'chave': mensagem.key().decode('utf-8') if mensagem.key() is not None else None,
                'valor': mensagem.value().decode('utf-8') if mensagem.value() is not None else None
            }
            mensagens.append(mensagem_dict)
            print(mensagem.value().decode('utf-8'))


# Iniciar a thread do consumidor
thread_consumidor = threading.Thread(target=consumir_mensagens)
thread_consumidor.start()

# Rota principal


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Rota para obter e remover uma mensagem do array


@app.route('/api/mensagem', methods=['GET'])
def obter_mensagem():
    with mensagens_lock:
        if len(mensagens) > 0:
            mensagem = mensagens.pop(0)
            return jsonify(mensagem)
        else:
            return jsonify({'mensagem': 'Nenhuma mensagem disponível'})


# Executar o servidor Flask
if __name__ == '__main__':
    app.run(port=8000)
