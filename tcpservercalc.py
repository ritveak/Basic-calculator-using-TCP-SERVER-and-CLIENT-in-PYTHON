import socket
s= socket.socket()
port = 12345
s.bind ((socket.gethostname(),port))
s.listen(5)
count=0
while (count<1):
	c,addr=s.accept()
	b=c.recv(1024).decode()
	print ('Recieved expression = ',b)
	e=eval(b)
	a=str(e)
	c.send(a.encode())
	c.close()
	count=count+1
s.close()