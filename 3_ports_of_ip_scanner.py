import socket

# Scan the port range for the  provided IP address.
def scan_ports(ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.1)  # Adjust timeout as needed
                result = s.connect_ex((ip, port))
                if result == 0:
                    open_ports.append(port)
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
    return open_ports

# Input the IP address and the port range.
def main():
    ip = input("Enter the IP address to scan: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    open_ports = scan_ports(ip, start_port, end_port)
    if open_ports:
        print(f"Open ports on {ip}: {', '.join(map(str, open_ports))}")
    else:
        print(f"No open ports found on {ip}")

if __name__ == "__main__":
    main()