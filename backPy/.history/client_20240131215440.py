import socket
import concurrent.futures
import sys
from colorama import Fore 
host = '127.0.0.1'
port = 1519
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def clientInterFace(host, port):
    sock.connect((host, port))    

    while True:
        
        # messages receiving zone
        msg_recv = sock.recv(2046).decode('utf-8')
        if msg_recv is not None and msg_recv == "handle":
            data = input(Fore.BLUE + "#Handle % ")
            sock.send(data.encode('utf-8'))
        else: 
            client, addr = sock.accept()
            msg_rcv = client.recv(2048).decode('utf-8')
            print(msg_rcv)   
        # messages  sending zone
        print(Fore.RED + f'msg recv...{msg_recv}')
          
        dt = input("msg % ") 
       
        while dt != "quit":
            dt = input("msg % ") 
            with concurrent.futures.ThreadPoolExecutor()as p:
                p.submit(handleSending, dt)
            # sock.sendall(dt.encode('utf-8'))


with concurrent.futures.ThreadPoolExecutor() as  ctrl:
    ctrl.submit(clientInterFace, host, port)


def handleSending(msg):
    cl, ad = sock.accept()
    cl.sendall(msg.encode('utf-8'))
