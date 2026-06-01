import socket
start = int(input("Enter the starting port number: "))
stop = int(input("Enter the ending port number: "))
host = input("Enter the host to scan: ")
for i in range(start, stop+1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    if s.connect_ex((host, i)) == 0:
        try:
            service = socket.getservbyport(i)
        except:
            service = "Unknown"
        print(f"Port {i} is open ({service})")
    s.close()