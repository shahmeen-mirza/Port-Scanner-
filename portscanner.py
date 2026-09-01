                                    ### Port Scanner ###
import socket

target_input = input ("Enter the website or IP to scan: ")

try:                   
    target_ip = socket.getho stbyname(target_input)
    print ("Succes! Target Ip found! " , target_ip)
    print ("Scanning port from 78 to 82\n")
  
#run a loop
    for port in range (78, 83):
        rider = socket.socket(socket.AF_INET , socket.SOCK_STREAM)    
        rider.settimeout (1.5)      #limit
    
        result= rider.connect_ex ((target_ip, port))          #rider=socket connection act as delieveryboy
        if result == 0:
            print (f"==> ports {port} are Open")
        else:
            print (f"==> ports are {port} Closed")

        rider.close()

except Exception as error:
    print ("Invalid! please check spelling and try again.")
