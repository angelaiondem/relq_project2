import subprocess
import platform

# Ping to given IP in the network.
def ping(host):
    """
    Ping the specified host to check if it's reachable.
    Returns True if the host is reachable, False otherwise.
    """
    if platform.system().lower() == "windows":
        ping_cmd = ["ping", "-n", "1", "-w", "1000", host]
    else:
        ping_cmd = ["ping", "-c", "1", "-W", "1", host]
    
    try:
        # Run the ping command
        subprocess.run(ping_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

# Ping to all IPs in the network.
def scan_network(network):
    """
    Perform a network scan to discover live hosts.
    """
    live_hosts = []
    for i in range(1, 255):
        host = f"{network}.{i}"
        if ping(host):
            live_hosts.append(host)
    return live_hosts

# Enter the network section of the IP that needs to be scanned.
def main():
    network = input("Enter the network address (e.g., 192.168.1): ")
    print(f"Scanning network {network}.0/24...")
    live_hosts = scan_network(network)
    if live_hosts:
        print("Live hosts found:")
        for host in live_hosts:
            print(host)
    else:
        print("No live hosts found.")

if __name__ == "__main__":
    main()