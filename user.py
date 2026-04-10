import socket

def udp_client():
    host = '127.0.0.1'
    port = 12345
    img = "12345"

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = "Hello, UDP Server!"
    client_socket.sendto(img.encode('utf-8'), (host, port))

    data, _ = client_socket.recvfrom(1024)
    print(f"サーバーからの応答: {data.decode('utf-8')}")
    client_socket.close()

if __name__ == "__main__":
    udp_client()