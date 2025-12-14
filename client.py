import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "127.0.0.1"
PORT = 5002

client_socket.connect((HOST, PORT))

while True:
    message = input("Enter message: ")

    if message.lower() == "exit":
        break

    client_socket.send(message.encode("utf-8"))

    response = client_socket.recv(1024)
    print("Server:", response.decode("utf-8"))

client_socket.close()
