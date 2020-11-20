"""A simple websocket python client.
"""
import asyncio
import websockets
import time

url = "ws://localhost:8100/bench/websocket"


async def listen():
    counter = 0
    t_0 = time.time_ns()
    async with websockets.connect(url) as websocket:
        async for message in websocket:
            counter += 1
    delta_t = time.time_ns() - t_0
    duration = int(delta_t / 1000)
    average = int(delta_t / counter)

    print("Websocket")
    print(f"Messages: {counter:>12}")
    print(f"Duration: {duration:>10}ms")
    print(f"Average:  {average:>10}ns")


asyncio.get_event_loop().run_until_complete(listen())
