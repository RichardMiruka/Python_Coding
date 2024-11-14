# to run script use sudo python3 connected_to_wifi.py
# sudo pip install scapy
# pip install ipaddress
from scapy.all import ARP, Ether, srp
import ipaddress

def get_connected_devices(ip_range):
    # Create an ARP request packet
    arp = ARP(pdst=str(ip_range))
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    # Send the packet and receive responses
    result = srp(packet, timeout=8, verbose=0)[0]

    # Parse and print the IP and MAC addresses of the devices found
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    return devices

def main():
    # Set your IP range (typically your local network IP with a /24 subnet)
    network = input("Enter your network IP (e.g., 192.168.1.1/24): ")
    try:
        ip_range = ipaddress.ip_network(network, strict=False)
    except ValueError:
        print("Invalid IP range.")
        return

    print("Scanning for devices...")
    devices = get_connected_devices(ip_range)

    if devices:
        print(f"\nDevices connected to the network {network}:")
        for device in devices:
            print(f"IP: {device['ip']}, MAC: {device['mac']}")
    else:
        print("No devices found.")

if __name__ == "__main__":
    main()
