"""A simple unix python server.
"""
import asyncio
import os


nb_messages = 1000000
unix_path = "/tmp/bench_unix"


async def serve(reader, writer):
    for _ in range(nb_messages):
        writer.write(("Hello, world!\n").encode("utf8"))
        await writer.drain()
    writer.write_eof()
    # writer.close()
    # await writer.wait_closed()


# Clean previous socket, if any
if os.path.exists(unix_path):
    os.remove(unix_path)

server = asyncio.start_unix_server(serve, unix_path)
asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()
