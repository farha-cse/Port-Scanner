import socket

print("=" * 40)
print("Python Port Scanner")
print("=" * 40)

target = input("Enter Target IP or Host: ")

for port in range(1, 101):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    sock.close()