from confluent_kafka import Producer

# server setup
conf = {"bootstrap.servers": "localhost:9092"}

producer = Producer(**conf)


def delivery_report(err, msg):
    if err is not None:
        print(f"Mensagem falhou {err}")
    else:
        print(f"Mensagem entregue a {
              msg.topic()} [Partição: {msg.partition()}]")


# for i in range(10):
#     producer.produce(
#         "first_topic",
#         key=str(i),
#         value=f"message {i}",
#         callback=delivery_report,
#     )
key = 0


def send_message():
    global key
    key += 1

    message = input("Digite a sua mensagem: ")

    if message == "sair":
        return

    producer.produce(
        "first_topic", key=str(key), value=message, callback=delivery_report
    )

    send_message()


producer.flush()
