import socket
import concurrent.futures
host = '127.0.0.1'
port = 1226

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# def connector():
#     ClientSocket = socket.socket()
#     print('Waiting for connection...')
    
#     while True:
#         try:
#             ClientSocket.connect((host, port))
#         except socket.error as e:
#             print(str(e))
#         incoming = ClientSocket.recv(2048).decode('utf-8')
        
#         with concurrent.futures.ThreadPoolExecutor() as exe:
#             exe.submit(msging, ClientSocket, incoming)
    
# def msging(ClientSocket, incoming):
#     if incoming is not None and incoming.lower() == "handle":
#         get_handle = input("# handle %".encode('utf-8'))
#         ClientSocket.send(get_handle)
        
# connector()

