import socket
import threading
import sys


class Client:
    def __init__(self, c_port):
        self.sock = socket.socket()
        self.sock.connect(('localhost', c_port))
        self.t1 = threading.Thread(target=self.reciever)
        self.t2 = threading.Thread(target=self.sender)

        self.t1.start()
        self.t1.join()
        self.t2.join()

        self.sock.close()

    def reciever(self):
        self.t2.start()

        while self.t2.is_alive():
            msg = self.sock.recv(1024).decode()
            print("Server ->", msg)
            if msg == "Exit!":
                self.sock.close()
                break

    def sender(self):
        while self.t1.is_alive():
            msg = input()
            self.sock.send(msg.encode())
            if msg == "Exit!":
                self.sock.close()
                break


port = int(input("Enter port: "))
c = Client(port)
