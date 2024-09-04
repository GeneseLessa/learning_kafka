# Kafka Basics with Python

Este pequeno projeto consiste basicamente em um consumer e um producer escritos em python com o objetivo inicial de apenas aprender sobre kafka.

## Modo de uso

Para usar o código neste repositório você basicamente precisa rodar os conteineres do zookeper e kafka no docker. Para este caso eu minimizei o uso de RAM. Basta realizar o build e up dos containeres:

```
$ docker compose up -d
```

Em seguida, basta rodar os scripts consumer.py e producer.py.
