import socket

cash_dict = {}
import socket

# UDPサーバー
def tcp_server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"UDPサーバーが {host}:{port} で起動しました")
    print("-"*50)

    while True:
        client_socket, address = server_socket.accept()
        request = client_socket.recv(1024).decode('utf-8')
        print(f"受信したデータ: {request} from {address}")

        if not cash_dict.get(request) == None:
            #キャッシュにあったから返す。
            print("あったから返すね")
            result = cash_dict[request]
            server_socket.sendto(result, address)
        
        else:
            #キャッシュになかったから取りに行く。
            print("データを取りに行く")
            result = tcp_client(request).encode('utf-8')
            cash_dict[request] = result
            server_socket.sendto(result, address)

        print("-"*50)

# UDPクライアント
def tcp_client(request):
    host = '127.0.0.2'
    port = int(request)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.connect((host, port))
    message = "Hello, TCP Server!"
    client_socket.send(message.encode('utf-8'))

    result = client_socket.recv(1024).decode('utf-8')
    print(f"サーバーからの応答: {result}")

    client_socket.close()

    return result

if __name__ == "__main__":
    tcp_server()
