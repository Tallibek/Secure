import socket


HOST = "127.0.0.1"
PORT = 65435

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

server_socket.listen(1)
conn, addr = server_socket.accept()
print(f"Połączono z: {addr}")


while True:

    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"Klient: {data}")

    msg = input("Ty (serwer): ")
    conn.send(msg.encode())
    if msg.lower() == "exit":
        break

conn.close()
server_socket.close()

