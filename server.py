import socket

# 1. Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Bind the socket to IP and Port
HOST = "127.0.0.1"   # localhost
PORT = 5000

# ✅ Allow reusing the same address
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))

# 3. Listen for incoming connections
server_socket.listen(5)
print(f"[SERVER] Listening on {HOST}:{PORT}...")

while True:
    # 4. Accept a client connection
    client_socket, client_address = server_socket.accept()
    print(f"[CONNECTED] Client connected from {client_address}")

    while True:
        # 5. Receive data from client
        data = client_socket.recv(1024)

        if not data:
            print("[DISCONNECTED] Client disconnected")
            break

        message = data.decode("utf-8")
        print(f"[CLIENT] {message}")

        # 6. Send response back to client
        response = f"Server received: {message}"
        client_socket.send(response.encode("utf-8"))

    # 7. Close client socket
    client_socket.close()
