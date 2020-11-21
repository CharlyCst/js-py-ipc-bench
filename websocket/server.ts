/// A simple websocket typescript server;

import * as sock from "sockjs";
import * as http from "http";

const message = "Hello, world!";
const nbMessages = 1000000;

// Websocket server
const wsServer = sock.createServer({prefix: "/bench"});
wsServer.on('connection', (conn) => {
    for (let i = 0; i < nbMessages; i++) {
        conn.write(message);
    }
    conn.close();
})

// Http server
const httpServer = http.createServer();

wsServer.installHandlers(httpServer);
httpServer.listen(8100, "localhost");
