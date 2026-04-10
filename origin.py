import socket

# UDPサーバー
def udp_server():
    host = '127.0.0.2'
    port = 12345
    text = "こんにちは"

    utf_8text = text.encode('utf-8')
    if len(utf_8text) > 1024:
        raise Exception

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print(f"UDPサーバーが {host}:{port} で起動しました")

    while True:
        data, address = server_socket.recvfrom(1024)
        print(f"受信したデータ: {data.decode('utf-8')} from {address}")
        server_socket.sendto(utf_8text, address)

if __name__ == "__main__":
    udp_server()