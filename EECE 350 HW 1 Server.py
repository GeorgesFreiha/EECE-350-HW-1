import socket
import datetime

port = 12000 
mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.bind((socket.gethostname(),port))
mysocket.listen(1)
print("Socket is ready to listen")
while True:
     connectionSocket, addr = mysocket.accept() #server waits on accept() for incoming requests, new socket created on return
     print("Address received from",addr)
     req = connectionSocket.recv(4096).decode() #Transform binary into the link
     addrdest= req.split('/')[2] #Get the IP address required from the client 
     print("Received",addrdest,"At:",datetime.datetime.now())
     
     try:#for errors
         PD=80 #Destination port
         SD=addrdest #Server destination
         connect= (SD,PD) 
         destination= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
         destination.connect(connect)# connect the server distination and the port
         
         destination.send(req.encode()) #Turn request into binary
         print("Sent at time:", datetime.datetime.now())
         
         ans=destination.recv(4096)
         print("Received at time:", datetime.datetime.now())
         
         destination.close() 
         
         connectionSocket.send(ans) #Response sent back to to client
         print("Sent to client at:", datetime.datetime.now())
     except:
        print("An error occured")
        connectionSocket.send("Couldn't process the message, Try Again".encode())
     connectionSocket.close() ##close connection to this client (but not welcoming socket)
    
#https://www.w3schools.com/python/gloss_python_date.asp link used for date and time