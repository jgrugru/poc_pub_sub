from redis import Redis


# establish redis connection
r = Redis()

# Create subscriber
subscriber = r.pubsub()
subscriber.subscribe('redis_channel')

subscriber1 = r.pubsub()
subscriber1.subscribe('redis_channel')

# Publish message, has to match classical_music
print(r.publish("redis_channel", "This is my message"))
print(r.publish("redis_channel", "This is my message 2"))


# print(subscriber.get_message()["data"])
# print(subscriber.get_message()["data"])
# print(subscriber.get_message()["data"])
