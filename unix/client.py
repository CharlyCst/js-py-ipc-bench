"""A simple websocket python client.
"""
import asyncio
import os
import time


unix_path = "/tmp/bench_unix"
separator = "|".encode("utf8")


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
    duration = int(delta_t/1000)
    average = int(delta_t / counter)

    print("Unix socket")
    print(f"Messages: {counter:>12}")
    print(f"Duration: {duration:>10}ms")
    print(f"Average:  {average:>10}ns")
    writer.close()


if not os.path.exists(unix_path):
    print(f"Could not find unix socket: {unix_path}")

asyncio.get_event_loop().run_until_complete(listen())
