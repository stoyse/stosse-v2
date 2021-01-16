import socket
import os

def Socket(recv, send):
    host = ''
    port = 777
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    while True:
        cli, addr = s.accept()
        print(f'Connection established from: {addr}.')
        raw_data = cli.recv(5000)
        data = raw_data.decode('utf-8')
        Terminal(command=data)
        if send == 'clear':
            cli.send(bytes(str.encode('clear')))


def Terminal(command):
    while True:
        if bytes('socket') == command:
            Socket(recv=False, send=False)
        if bytes('clear') == command:
            Socket(recv=False, send='clear')


cmd = bytes(input('STOSSE SYSTEM> '))
Terminal(command=cmd)
