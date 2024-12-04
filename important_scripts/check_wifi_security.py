import pywifi
from pywifi import const

def check_wifi_security():
    wifi = pywifi.PyWiFi()  # Initialize pywifi
    iface = wifi.interfaces()[0]  # Get the first wireless network interface

    if iface.status() != const.IFACE_CONNECTED:
        print("You are not connected to any Wi-Fi network.")
        return

    # Get the current Wi-Fi connection
    profile = iface.network_profiles()[0]
    
    print(f"Wi-Fi Name (SSID): {profile.ssid}")

    # Check encryption type
    encryption = "Unknown"
    if profile.akm[0] == const.AKM_TYPE_NONE:
        encryption = "None (Open Wi-Fi)"
    elif profile.akm[0] == const.AKM_TYPE_WPA:
        encryption = "WPA"
    elif profile.akm[0] == const.AKM_TYPE_WPAPSK:
        encryption = "WPA-PSK"
    elif profile.akm[0] == const.AKM_TYPE_WPA2:
        encryption = "WPA2"
    elif profile.akm[0] == const.AKM_TYPE_WPA2PSK:
        encryption = "WPA2-PSK"

    print(f"Encryption: {encryption}")

    # Evaluate security
    if encryption == "None (Open Wi-Fi)":
        print("⚠️ This network is NOT secure. Avoid using sensitive information.")
    elif encryption in ["WPA", "WPA2"]:
        print("✔️ This network uses a strong encryption method.")
    elif encryption == "Unknown":
        print("⚠️ Unable to determine the encryption method. Check manually.")

    # Signal strength (optional check)
    print(f"Signal Strength: {profile.signal} dBm")
    if profile.signal < -70:
        print("⚠️ Weak signal strength may expose you to attacks.")
    else:
        print("✔️ Signal strength is good.")

if __name__ == "__main__":
    check_wifi_security()
