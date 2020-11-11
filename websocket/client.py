"""A simple websocket python client.
"""
import asyncio
import websockets
import time

url = "ws://localhost:8100"


async def listen():
    counter = 0
    t_0 = time.time_ns()
    async with websockets.connect(url) as websocket:
        async for message in websocket:
            counter += 1
    delta_t = time.time_ns() - t_0
    average = int(delta_t / counter)
    print(f"Took {average}ns par message")


asyncio.get_event_loop().run_until_complete(listen())
