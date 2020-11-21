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
    duration = delta_t/1000000000
    average = int(delta_t / counter)

    print(f"Messages: {counter:>13}")
    print(f"Duration: {duration:>11.3f} s")
    print(f"Average:  {average:>10} ns")


asyncio.get_event_loop().run_until_complete(listen())
