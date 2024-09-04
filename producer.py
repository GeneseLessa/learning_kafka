from confluent_kafka import Producer

# server setup
conf = {'bootstrap.servers': 'localhost:9092'}

producer = Producer(**conf)


def delivery_report(err, msg):
    if err is not None:
        print(f'Mensagem falhou {err}')
    else:
        print(
            f'Mensagem entregue a {msg.topic()} [Partição: {msg.partition()}]'
        )


def send_message(key=0):
    message = input('Digite a sua mensagem: ')

    if message == 'sair':
        return

    key += 1

    producer.produce(
        'first_topic', key=str(key), value=message, callback=delivery_report
    )

    send_message(key)


send_message()

producer.flush()
