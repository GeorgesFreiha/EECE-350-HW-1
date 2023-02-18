import socket
import datetime
import uuid
import time

port=12000
serverclientproxy= socket.gethostbyname(socket.gethostname())
connect2= (serverclientproxy,port)
myclient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
myclient.connect(connect2)

addr= input("Enter IP Address: ")
req= "Get http://" + addr + "/HTTP/1.1\n\n"

myclient.send(req.encode())
timetosend=time.time() #Time to send the request

print("Message: ", req, "at time", datetime.datetime.now())
ans=myclient.recv(4096)

timetoreceive=time.time() # Time to receive the request
print("Server answered:",ans, "at time",datetime.datetime.now())

roundtriptime = timetoreceive - timetosend
print("It took " + str(roundtriptime) + " for the whole process")

print("MAC Address: ", hex(uuid.getnode()))