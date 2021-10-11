# server.py
import socket

ip_address = '192.168.11.4'
port = 8765
buffer_size = 4092

# Socketの作成
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # IP Adress とPort番号をソケット割り当てる
    s.bind((ip_address, port))
    # Socketの待機状態
    s.listen(5)
    # while Trueでクライアントからの要求を待つ
    conn, addr = s.accept()
    while True:
        # 要求があれば接続の確立とアドレス、アドレスを代入
        # データを受信する
        data = conn.recv(buffer_size)
        #print(f"生データ = {data}")
        print(f' addr->{addr} \n data-> {data.decode(encoding="utf-8")}')
        # データを送信する
        conn.sendall(b'I received the data correctly.')