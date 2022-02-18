from kombu import Connection, Exchange, Queue

connection = Connection("redis://localhost:6379")
connection.connect()
producer = connection.Producer()
exchange = Exchange("test_exchange", type="direct")
task_queue = Queue("tasks", exchange, routing_key="tasks")

# verify the connection is working
print(connection.connected)


producer.publish(
    {"hello": "world"},  # message to send
    exchange=exchange,  # destination exchange
    routing_key=task_queue.routing_key,  # destination routing key,
    declare=[task_queue],  # make sure exchange is declared,
    retry=True,
    retry_policy={
        "interval_start": 0,  # First retry immediately,
        "interval_step": 2,  # then increase by 2s for every retry.
        "interval_max": 30,  # but don't exceed 30s between retries.
        "max_retries": 30,  # give up after 30 tries.
    },
)
