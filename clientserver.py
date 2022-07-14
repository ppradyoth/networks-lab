////      Client.py     ////



import socket
s=socket.socket()
port = 6000
s.connect(('127.0.0.1',port))
print(s.recv(1024).decode())
msg  =raw_input("Enter the text to be Conveted : ")
s.send(msg)
print(s.recv(1024).decode())
s.close()
 

  
  
  ////     Server.py /////



import socket
s = socket.socket()
print("Socket successfully created\n")
port = 6000
s.bind(('',port))
print("Socket binded to %s"%(port))
s.listen(5)
print("Socket is Listening")
while 1:
        c,addr = s.accept()
        print("Connection from",addr)
        c.send("Succesfully Connected".encode())
        msg = c.recv(1024).decode().lower()
        c.send(msg)
        c.close()
       break
