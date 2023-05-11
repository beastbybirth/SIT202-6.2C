import socket

client_address = "127.0.0.1"
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (client_address, 1234)

user_decision = "Y"
while user_decision.upper() == "Y":
    domain_name = input("Enter domain name for which the IP is needed: ")
    try:
        client_socket.sendto(domain_name.encode(), server_address)
        data, address = client_socket.recvfrom(1024)
        cname, address = client_socket.recvfrom(1024)
        server_ip = data.decode().strip()
        message = "The IP for the {} server is {}".format(cname, server_ip)
        print(message)
    except socket.error as e:
        print("Error: {}".format(e))
    user_decision = input("Continue? (y/n) ")

client_socket.close()
