# relq_project2

## 1. System Update and Upgrade
This script automatically updates and upgrades the system whenever it is run. Please note that this script is intended for use only with Linux Debian-based systems.

## 2. Spoofing Detection
The code in this section checks for email spoofing by verifying SPF, DKIM, and DMARC records of an email provided in the .eml format.

Before running the code, ensure the following external libraries are installed:

```bash
pip install dkimpy py3dns dmarc
```


## 3. Network Mapper
This section contains two scripts:

1. `3_ips_of_network_scanner.py`: This script prompts the user to enter a network part of the IP address (e.g., 10.0.2), then scans and lists all available/reachable IP addresses within that network. Note that the script is designed for scanning networks with a /24 prefix.

2. `3_ports_of_ip_scanner.py`: This script asks for an IP address to be scanned (e.g., 10.0.2.5) and also requests the starting and ending port numbers. It then checks which ports (within the given range) are open on the specified IP address.

## 4. Password Generator
This script prompts the user to input the desired length of the generated password, which should be at least 8 characters long. After receiving the length, the script generates a random password that includes at least one uppercase letter, one lowercase letter, one number, and one symbol.

## 5. Email Notification for Banned IPs
This script checks the fail2ban-client jail of sshd and sends an email notification if a banned IP is detected.

Please note that this script needs to be run with sudo privileges to access fail2ban-client.