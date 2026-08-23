import socket

def grab_banner(ip, port):
    try:
        # Create a socket instance
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a 3-second timeout so it doesn't freeze forever on quiet ports
        s.settimeout(3)
        
        # Connect to the target
        s.connect((ip, port))
        
        # Receive up to 1024 bytes from the target service
        banner = s.recv(1024)
        
        # Decode the raw bytes into a readable text string
        print(f"\n[+] Banner from {ip}:{port} -> {banner.decode().strip()}")
        
        s.close()
    except Exception as e:
        print(f"\n[-] Could not grab banner from {ip}:{port} - {e}")

# Interactive prompt for the user
target_ip = input("Enter target IP address: ")
target_port = int(input("Enter port number: "))

grab_banner(target_ip, target_port)
