import asyncio

import async_timeout

import aioredis

STOPWORD = "STOP"


async def reader(channel: aioredis.client.PubSub, redis):
    while True:
        try:
            async with async_timeout.timeout(1):
                message = await channel.get_message(ignore_subscribe_messages=True)
                if message is not None:
                    if "Acknowledged" not in message["data"].decode("utf-8"):
                        await redis.publish(
                            "BrokerShow:2",
                            "Acknowledged: " + message["data"].decode("utf-8"),
                        )
                        print(f"(Reader) Message Received: {message}")
                        # if message["data"].decode() == STOPWORD:
                        #     print("(Reader) STOP")
                        #     break
                await asyncio.sleep(0.001)
        except asyncio.TimeoutError:
            pass


async def main() -> None:
    redis = aioredis.from_url("redis://localhost")
    pubsub = redis.pubsub()

    await pubsub.subscribe("BrokerShow:1", "BrokerShow:2")

    future = asyncio.create_task(reader(pubsub, redis))

    await redis.publish(
        "BrokerShow:1", "{'status':'New', 'raw_broker_show':'AMD Feb 150c'}"
    )
    await redis.publish("BrokerShow:2", "World")
    await redis.publish("BrokerShow:1", STOPWORD)

    await future


if __name__ == "__main__":
    asyncio.run(main())
