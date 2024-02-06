import socket
from _thread import *
import concurrent.futures

host = '127.0.0.1'
port = 1226
ThreadCount = 0

hosts_available = []

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


def createConnection():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    print("Server listening ...")
    while True:
        client, addr = sock.accept()
    

def clientHandler(handle):
    if handle is not None:
        hosts_available.append(handle)


def msg_routing(hosts_available, msg):
    hosts_available.sendall('server-stem'.encode('utf-8'))


createConnection()
