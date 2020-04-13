import socket
import threading
class client:
    def _init_():
          c.client = socket.socket()

          c.client.connect('localhost',8500)

          c.t1 = threading.Thread(target = s.send)
          c.t2 = threading.Thread(target= s.rec)

          c.t2.start()
          c.t2.join()
          c.t1.join()

          c.serv.close()

    def rec(c):
       c.t1.start()

       while True:
          message = c.t2.recv(1024).decode()
       
          print("Client :",message)

          if message == "Exit":
            print("Connection to server is lost")
            c.serv.close()
            break
    def send(c):
        
       while c.t2.isalive():
        message = input()
       
        c.t1.send(message.encode())

        if msg == "Exit":
            c.serv.close()
            break
 Cc = client()  