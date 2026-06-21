from kafka import KafkaProducer
import json
import time

# Connect to Kafka server
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("Kafka Producer Started")

for i in range(10):

    order = {
        "order_id": i,
        "customer_id": 100 + i,
        "amount": 200 + i
    }

    producer.send("orders_topic", order)

    print("Sent:", order)

    time.sleep(1)

producer.flush()