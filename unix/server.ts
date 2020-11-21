/// A simple websocket typescript server;

import * as net from "net";
import * as fs from "fs";

const unixPath = "/tmp/bench_unix";
const message = "Hello, world!\n";
const nbMessages = 1000000;

// Clean previous socket, is any
if (fs.existsSync(unixPath)) {
    fs.unlinkSync(unixPath);
}

// Create unix server
const unixServer = net.createServer();
unixServer.on("connection", (socket) => {
    console.log("connection");
    for (let i = 0; i < nbMessages; i++) {
        socket.write(message);
    }
    socket.end();
});
unixServer.listen(unixPath, () => {
    console.log(`Listening on: ${unixPath}`);
});

