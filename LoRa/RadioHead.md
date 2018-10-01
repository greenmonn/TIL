# RadioHead
Library: [GitHub - PaulStoffregen/RadioHead: Packet Radio library for embedded microprocessors](https://github.com/PaulStoffregen/RadioHead)

Docs: [RadioHead: RadioHead Packet Radio library for embedded microprocessors](http://www.airspayce.com/mikem/arduino/RadioHead/)

RadioHead consists of 2 main sets of classes: **Drivers** and **Managers**.

Drivers provide low level access to a range of different packet radios and other packetized message transports.

Managers provide high level message sending and receiving facilities for a range of different requirements.

Every RadioHead program will have an instance of a Driver to provide access to the data radio or transport, and usually a Manager that uses that driver to send and receive messages for the application. **The programmer is required to instantiate a Driver and a Manager**, and **to initialise the Manager**. Thereafter the facilities of the Manager can be used to send and receive messages.

It is also possible to use a Driver on its own, without a Manager, although this only allows unaddressed, unreliable transport via the Driver's facilities.

In some specialised use cases, it is possible to instantiate more than one Driver and more than one Manager.

A range of different common embedded microprocessor platforms are supported, allowing your project to run on your choice of processor.

Example programs are included to show the main modes of use.

## Drivers
* RH_RF95: Supports Long Range (LoRa) with spread spectrum frequency hopping, large payloads etc.


## Managers
* **RHDatagram** Addressed, unreliable variable length messages, with optional broadcast facilities.

* **RHReliableDatagram** Addressed, reliable, retransmitted, acknowledged variable length messages.

* **RHRouter** Multi-hop delivery of RHReliableDatagrams from source node to destination node via 0 or more intermediate nodes, with manual routing.

* **RHMesh** Multi-hop delivery of RHReliableDatagrams with automatic route discovery and rediscovery.
