import socket
import threading
class server:
   def _init_():
    s.serv = socket.socket()
    #socket created
    
    s.serv.bind('localhost',8500)

    s.serv.listen(3)
    s.c, addr = s.serv.accept()
    
    print("Connected to" ,addr)
    
    s.t1 = threading.Thread(target = s.send)
    s.t2 = threading.Thread(target= s.rec)

    s.t2.start()
    s.t2.join()
    s.t1.join()
    
    s.serv.close()

   def rec(s):
       
       s.t1.start()

       while True:
          message = s.t2.recv(1024).decode()
       
          print("Client :",message)

          if message == "Exit":
            print("Connection to server is lost")
            s.serv.close()
            break
   def send(s):

       while s.t2.isalive():
        message = input()
       
        s.t1.send(message.encode())

        if msg == "Exit":
            s.serv.close()
            break
 Ss = server()  



       






         


 

    

    

