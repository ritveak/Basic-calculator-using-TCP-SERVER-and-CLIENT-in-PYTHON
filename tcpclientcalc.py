import socket
s= socket.socket()
port =12345
s.connect((socket.gethostname(),port))
msg=input("Hi I am your basic calculator\nWrite the basic calculation that you want me to do: ")
s.send(msg.encode())
b=s.recv(1024).decode()
print ('Solution = ',b)

s.close()