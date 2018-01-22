import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5001

def fac(n):
   if n == 1:
       return n
   else:
       return n*fac(n-1)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))    
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    result = fac(int (data))
    print "received data:", data
    print "Result:", result
    sock.sendto(str(result), addr)


