import socket

#Port and IP Number
PORT = 5000
IP = "100.1.1.1"
#01. Socket Making : socket()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#02. Address & Port : bind()
server.bind((IP, PORT))

#03. Waiting the connection : listen()
server.listen(1)

#04. Getting the socket : accept()
client, addr = server.accept()

#05. Data Yaritori : send(), recv()
client.sendall("こんにちは".encode('utf-8').hex()) #messeage

#06. Closing the connection()
client.close()
server.close()