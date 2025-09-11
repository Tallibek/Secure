import socket


HOST = "127.0.0.1"
PORT = 65435


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print(f"Połączono z serwerem: {HOST} na porcie: {PORT}")


while True:

    msg = input("Ty (klient): ")
    client_socket.send(msg.encode())
    if msg.lower() == "exit":
        break

    data = client_socket.recv(1024).decode()
    print(f"Serwer: {data}")


client_socket.close()


