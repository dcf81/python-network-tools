import socket

target = "127.0.0.1"
ports_to_test = [21, 22, 80, 443, 8080]

print(f"--- Scanning {target} ---")

for port in ports_to_test:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.5)

	result = s.connect_ex((target, port))

	if result == 0:
		print(f"[+] Port {port}: OPEN")
	else:
		print(f"[-] Port {port}: Closed")

	s.close()
