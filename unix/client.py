"""A simple websocket python client.
"""
import asyncio
import os
import time


unix_path = "/tmp/bench_unix"


async def listen():
    counter = 0
    t_0 = time.time_ns()
    (reader, writer) = await asyncio.open_unix_connection(unix_path)
    while True:
        message = await reader.readline()
        if len(message) == 0:
            break
        counter += 1
    delta_t = time.time_ns() - t_0
    duration = delta_t/1000000000
    average = int(delta_t / counter)

    print(f"Messages: {counter:>13}")
    print(f"Duration: {duration:>11.3f} s")
    print(f"Average:  {average:>10} ns")
    writer.close()


if not os.path.exists(unix_path):
    print(f"Could not find unix socket: {unix_path}")

asyncio.get_event_loop().run_until_complete(listen())
