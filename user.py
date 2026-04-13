import socket

def tcp_client():
    host = '127.0.0.1'
    port = 12345
    img = "12345"

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = "Hello, tcp Server!"
    client_socket.connect((host, port))
    client_socket.send(img.encode('utf-8'))

    request = client_socket.recv(1024).decode('utf-8')
    print(f"サーバーからの応答: {request}")
    client_socket.close()

if __name__ == "__main__":
    tcp_client()