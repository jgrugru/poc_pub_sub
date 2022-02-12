from kombu import Connection

connection = Connection("redis//localhost:6379")
connection.connect()
print(connection.connected)
