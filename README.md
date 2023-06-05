# Projeto Kafka Producer/Consumer para MBA de Engenharia de Dados FIAP 2023

Este projeto é um exemplo de aplicação que utiliza o Apache Kafka para comunicação entre um Producer (produtor) e um Consumer (consumidor). O Kafka é uma plataforma de distribuído mensageria que permite a transmissão de mensagens em tempo real de forma escalável e tolerante a falhas.

Também pode ser utilizado para realizar streaming de dados.

## Funcionalidades

- O Producer envia mensagens para um tópico específico no Kafka.
- O Consumer consome as mensagens desse tópico e as exibe em um servidor web.
- O servidor web expõe uma API para buscar as mensagens do Kafka.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter as seguintes dependências instaladas:

- Python (versão 3.x)
- Docker Desktop

## Configuração

1. Inicie um cluster Kafka com os brokers configurados através do comando ```docker compose up -d```
2. Certifique-se de que todas as dependências do Python estão instaladas `pip install -r requirements.txt` dentro de cada aplicação.
3. Rode o Producer dentro do diretório **producer** com o comando ```python app.py```
4. Rode o Consumer dentro do diretório **consumer** com o comando ```python app.py```
5. Acesse o consumer através do endereço ```http://127.0.0.1:5000```
