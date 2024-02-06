import socket
from _thread import *
import concurrent.futures
from colorama import Fore

host = '127.0.0.1'
port = 1555
ThreadCount = 0

# def client_handler(connection):
#     connection.send(str.encode('handle'))
#     while True:
#         data = connection.recv(2048)
#         message = data.decode('utf-8')
#         if message == 'BYE':
#             break
#         reply = f'Server: {message}'
#         connection.sendall(str.encode(reply))
#     connection.close()

# def accept_connections(ServerSocket):
#     while True:
#         Client, address = ServerSocket.accept()
#         print('Connected to: ' + address[0] + ':' + str(address[1]))
#         # start_new_thread(client_handler, (Client,))
#         with concurrent.futures.ThreadPoolExecutor() as exe:
#             exe.submit(client_handler, Client)

# def start_server(host, port):
#     while True:
#         ServerSocket = socket.socket()
#         try:
#             ServerSocket.bind((host, port))
#         except socket.error as e:
#             print(str(e))
#         print(f'Server is listing on the port {port}...')
#         ServerSocket.listen()

#         accept_connections(ServerSocket)

# start_server(host, port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def createConnection():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen()
    print("Server listening ...{}")
    while True:
        client, addr = sock.accept()
        print(Fore.GREEN + f"Connection established on ...{addr}")
        msg = "handle"
        msg_routing(client, msg)
        handle_recv = client.recv(2048).decode('utf-8')
        
        while handle_recv != "quit":
            if True:
                print(Fore.BLUE + f"{handle_recv} {Fore.GREEN}joined the platform .")
                break
            msg_recv = client.recv(2048).decode('utf-8')
            msg_routing(client, str(msg_recv).encode('utf-8'))

# def handle_msg(msg):
#     handle_recv = sock.recv(2048).decode('utf-8')
#     print(handle_recv)


def msg_routing(clients, msg):
    clients.sendall(str(msg).encode('utf-8'))
    hosts_available = []
    for client in clients:
        hosts_available.append(client)
    print(len(hosts_available))


createConnection()
