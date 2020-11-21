# js-py ipc benchmark

A small benchmark of some IPC methods between JavaScript and Python.

As always, take benchmarks with a grain of salt.

```
Websocket py-py
Messages:       1000000
Duration:      32.708 s
Average:       32707 ns

Websocket py-js
Messages:       1000000
Duration:       8.900 s
Average:        8900 ns

Unix socket py-py
Messages:       1000000
Duration:       2.187 s
Average:        2187 ns

Unix socket py-js
Messages:       1000000
Duration:       2.244 s
Average:        2244 ns
```

## Usage

Instal Node modules and compile the TypeScript servers:

```sh
npm install
npm run build
```

Setup your python environment to satisfy `requirement.txt`

```sh
# in your python virtual env
pip install -r requirements.txt
```

Then run the benchmark:

```sh
python benchmark.py
```

## More infos

The libraries used for the benchmarks are:

- Websocket js: `sockjs`
- Websocket py: `websockets`
- Unix socket js: Node built in package `net`
- Unix socket py: Python built in `asyncio`
