# socket.io

## What socket.io is

Socket.IO is a library that enables real-time, bidirectional and event-based communication between the browser and the server. It consists of a `Node.js` server and a javascript client library for the browser. (which can be also run from Node.js)

## What socket.io is not

Socket.IO is not a `WebSocket` implementation. Although Socket.IO indeed uses WebSocket as a transport when possible, it adds some metadata to each packet: `the packet type, the namespace and the ack id` when a message acknowledgement is needed. That is why a WebSocket client will not be able to successfully connect to a Socket.IO server, and a Socket.IO client will not be able to connect to a WebSocket server either. 


- [Protocol Specification](https://github.com/socketio/socket.io-protocol)

- [Socket.IO vs. WebSocket](https://d2.naver.com/helloworld/1336)