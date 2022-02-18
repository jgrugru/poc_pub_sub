from kombu.mixins import ConsumerMixin
from kombu import Connection


class C(ConsumerMixin):
    def __init__(self, connection):
        self.connection = connection

    def get_consumers(self, Consumer, channel):
        return [
            Consumer(channel, callbacks=[self.on_message], accept=["json"]),
        ]

    def on_message(self, body, message):
        print("RECEIVED MESSAGE: {0!r}".format(body))
        message.ack()


connection = Connection("redis://localhost:6379")
connection.connect()
C(connection).run()
