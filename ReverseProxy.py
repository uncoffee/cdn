import socket

cash_dict = {}

# UDPサーバー
def udp_server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print(f"UDPサーバーが {host}:{port} で起動しました")
    print("-"*50)

    while True:
        data, address = server_socket.recvfrom(1024)
        print(f"受信したデータ: {data.decode('utf-8')} from {address}")

        request = data.decode('utf-8')

        if not cash_dict.get(request) == None:
            #キャッシュにあったから返す。
            print("あったから返すね")
            cash_dict[request]
            server_socket.sendto(result, address)
        
        else:
            #キャッシュになかったから取りに行く。
            print("データを取りに行く")
            result = udp_client(str(request)).encode('utf-8')
            cash_dict[request] = result
            server_socket.sendto(result, address)

        print("-"*50)

# UDPクライアント
def udp_client(request):
    host = '127.0.0.2'
    port = int(request)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = "Hello, UDP Server!"
    client_socket.sendto(message.encode('utf-8'), (host, port))

    data, _ = client_socket.recvfrom(1024)
    print(f"サーバーからの応答: {data.decode('utf-8')}")

    result = data.decode('utf-8')

    client_socket.close()

    return result

if __name__ == "__main__":
    udp_server()
