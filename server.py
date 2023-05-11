import socket
dns_table = {"www.chitkara.edu.in": "192.168.1.1",
             "www.deakin.edu.au": "192.168.1.2",
             "www.google.com": "192.168.1.3",
             "www.faceboook.com": "192.168.1.4"}

cname_record = {"www.chitkara.edu.in": "host.chitkara.com",
                "www.deakin.edu.au": "host.deakin.com",
                "www.google.com": "host.google.com",
                "www.facebook.com": "host.facebook.com"}

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Server is running")
client_socket.bind(("127.0.0.1", 1234))
while True:
    try:
        data, address = client_socket.recvfrom(1024)
        message = format(address) + " requested to fetch data"
        print(message)
        data = data.decode()
        ip = dns_table.get(data, "Data not found").encode()
        cname = cname_record.get(data, "none").encode()
        send_ip = client_socket.sendto(ip, address)
        send_cname = client_socket.sendto(cname, address)
    except socket.error as e:
        print("Error: {}".format(e))
