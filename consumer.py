from confluent_kafka import Consumer, KafkaError

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'lessa',
    'auto.offset.reset': 'earliest',
}

consumer = Consumer(**conf)
consumer.subscribe(['first_topic'])

# consuming messages
while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue

    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(msg.error())
            break

    breakpoint()

    print(f'Recebeu a mensagem: {msg.value().decode("utf-8")}')

consumer.close()
