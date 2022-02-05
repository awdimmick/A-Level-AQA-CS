# https://realpython.com/python-sockets/

import socket
import os
import pathlib


def run_server(host='', port=4500):

    print("Running in server mode, listening for connection...")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        sock.listen()
        conn, addr = sock.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received {repr(data)}\nEchoing back...\n")
                conn.sendall(data)


def run_client(remote_host, port=4500):

    print("Running as client, connecting to server...")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((remote_host, port))
        sock.sendall(b'Hello, world')
        data = sock.recv(1024)

    print('Received', repr(data))


if __name__  == "__main__":

    choice = input("Run as (s)erver or (c)lient?\n> ")
    if choice.lower() == "s":
        run_server("127.0.0.1")
    elif choice.lower() == "c":
        run_client("127.0.0.1")

