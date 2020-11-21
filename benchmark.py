import signal
import asyncio
from asyncio.subprocess import PIPE, create_subprocess_shell

websocket_server_js = "node ./websocket/server.js"
websocket_server_py = "python ./websocket/server.py"
websocket_client_py = "python ./websocket/client.py"
unix_server_js = "node ./unix/server.js"
unix_server_py = "python ./unix/server.py"
unix_client_py = "python ./unix/client.py"


async def benchmark(client_cmd: str, server_cmd: str, benchmark_title: str):
    print(benchmark_title)
    server = await create_subprocess_shell(server_cmd, stdout=PIPE, stderr=PIPE)
    await asyncio.sleep(1)
    client = await create_subprocess_shell(client_cmd, stdout=PIPE, stderr=PIPE)
    await client.wait()
    stdout, _ = await client.communicate()
    print(f"{stdout.decode()}")
    server.send_signal(signal.SIGTERM)
    await server.wait()


async def main():
    await benchmark(websocket_client_py, websocket_server_py, "Websocket py-py")
    await benchmark(websocket_client_py, websocket_server_js, "Websocket py-js")
    await benchmark(unix_client_py, unix_server_py, "Unix socket py-py")
    await benchmark(unix_client_py, unix_server_js, "Unix socket py-js")



asyncio.run(main())
