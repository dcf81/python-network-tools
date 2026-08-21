import socket
import sys

# 1. Get target IP or hostname from user input
target = input("Enter target IP or hostname: ")

# 2. Get port range from user input
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

print("_" * 40)
print(f"Scanning target: {target}")
print(f"Scanning ports: {start_port} to {end_port}")
print("_" * 40)

try:
    # Resolve domain names (like scanme.nmap.org) to an IP address
    target_ip = socket.gethostbyname(target)

    # Loop through the user's requested port range

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) # Wait 0.5 seconds for a response

        result = s.connect_ex((target_ip, port))

        if result == 0:
            print(f"[+] Port {port}: OPEN")

        s.close()

except KeyboardInterrupt:
    print("\n[-] Scan interrupted by user.")
    sys.exit()
except socket.gaierror:
    print("\n[-] Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("\n[-] Could not connect to server.")
    sys.exit()


