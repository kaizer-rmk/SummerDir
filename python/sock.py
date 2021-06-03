import socket
s = socket.socket()
serverip = "192.168.225.54"
serverport = 2222
s.connect( (serverip,serverport) )
s.recv(100)
s.send(b"I m client A")