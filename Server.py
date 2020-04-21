import socket
import threading

class Server:

    def __init__(self, s_port):
        self.s_port = s_port
        self.sock = socket.socket()
        self.sock.bind(('localhost', self.s_port))
        self.sock.listen(5)

        self.s, addr = self.sock.accept()

        print("Connection from:", addr[0], addr[1])
        print("Exit! to end connection")

        self.t1 = threading.Thread(target = self.reciever)
        self.t2 = threading.Thread(target = self.sender)

        self.t1.start()
        self.t1.join()
        self.t2.join()

        self.sock.close()

    def reciever(self):
        self.t2.start()

        while self.t2.is_alive():
            msg = self.s.recv(1024).decode()
            print("Client:", msg)

            if msg == "Exit!":
                self.s.close()
                break

    def sender(self):
        while self.t1.is_alive():
            msg = input()
            self.s.send(msg.encode())

            if msg == "Exit!":
                self.s.close()
                break


port = int(input("Enter port to be used: "))
serv = Server(port)
