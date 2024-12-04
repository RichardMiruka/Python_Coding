"""
Port Scanning Script

Port scanning is a common technique used by hackers to discover open services
running on a host or network device. This technique is useful for identifying
potential vulnerabilities that could be exploited. It is also valuable for
assessing the security of a network by checking for open ports that might
be exploited by attackers.

This script uses the `socket` module to perform a simple port scan on a target
host. It connects to each specified port and checks if it is open or closed.
"""

import socket


def port_scanner(target_host, target_ports):
    """
    Scan specified ports on the given target host.

    Args:
        target_host (str): The IP address or hostname of the target.
        target_ports (list): A list of ports to scan.
    """
    try:
        # Resolve the target hostname to an IP address
        target_ip = socket.gethostbyname(target_host)
        print(f"Scanning target: {target_ip}")
    except socket.gaierror as error:
        print(f"Error resolving hostname: {error}")
        return

    for port in target_ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Set a timeout to avoid hanging on unavailable ports
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))

            if result == 0:
                print(f"Port {port}: Open")
            else:
                print(f"Port {port}: Closed")


if __name__ == "__main__":
    # Define the target host and ports to scan
    TARGET_HOST = "38.0.101.76"
    TARGET_PORTS = [21, 22, 80, 443]

    # Perform the port scanning
    port_scanner(TARGET_HOST, TARGET_PORTS)
