"""A simple websocket python server.
"""
import asyncio
import websockets


nb_messages = 10000


async def serve(websocket, path):
    for _ in range(nb_messages):
        await websocket.send("Hello, world!")


server = websockets.serve(serve, "localhost", 8100)
asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()
