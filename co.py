import socket 


host = ""
port = 3030 

def send(y) :
	y = y.encode()
	with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s : 
		s.connect((host, port))
		s.sendall(y)
	
	


