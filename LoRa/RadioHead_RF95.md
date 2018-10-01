# RadioHead_RF95
*RadioHead library code analysis*

## Client
### RF95_client
`rf95` instance를 사용. 즉 `driver`를 직접 선언하고 제어한다. 사용할 수 있는 메소드는 다음과 같다.
* `send`: data array를 보낸다.
* `waitPacketSent`: packet이 완전히 보내질 때까지 기다린다 (send가 완전히 끝날 때까지 프로그램은 이 상태에서 멈춘다: blocking)
* `waitAvailableTimeout`
	* Blocks until a valid message is received or timeout expires
	* Return true if there is a **message available**
	* Works correctly even on millis() rollover
* `recv`: buffer에 받은 message를 채운다. 받은 메시지가 없으면 false를 반환한다.
	
### RF95_reliable_datagram_client
`manager`를 통해서 패킷을 제어한다. `manager`가 처음 생성될 때 `driver`를 지정하여, `manager`를 거쳐서 `driver`를 제어하도록 한다. 사용하는 메소드들은 다음과 같다.
* `sendtoWait`: 지정된 서버로 data array를 데이터 패킷(=datagram)으로 만들어서 전송한다.
* `recvfromAckTimeout`: 메시지가 도착할 때까지 기다렸다가, 받은 메시지의 내용을 buffer에 기록한다. 여기서는 reliability를 위해 `ACK` 패킷을 추가적으로 보내서 정상적으로 ‘받았음’을 서버에 알려준다.

## Server
### RF95_server
마찬가지로 `rf95` instance를 사용.
메소드는 `recv`를 먼저 하고 `send`하는 것 외에는 client와 거의 비슷하다. 이 예제에서는 메시지를 받는 순서만 바뀐다.
* `recv`
* `send`
	
### RF95_reliable_datagram_server
역시 `manager`가 `driver`를 제어하는 형태로 사용되고, 역시 `recvfromAck` 이후 `sendtoWait` 메소드를 활용하여, 클라이언트로부터 메시지를 받고 reply를 보내는 형태가 된다.