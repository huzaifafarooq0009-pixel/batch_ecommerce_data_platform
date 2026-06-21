from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

order = {
    "order_id": 1,
    "customer_id": 10,
    "product_id": 5,
    "quantity": 2
}

producer.send("orders_topic", order)

producer.flush()

print("Order sent successfully!")