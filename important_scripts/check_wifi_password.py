import subprocess

def get_wifi_password():
    try:
        # Get the current WiFi SSID
        ssid_command = 'powershell.exe -Command "(Get-NetConnectionProfile).Name"'
        ssid = subprocess.check_output(ssid_command, shell=True).decode().strip()

        if not ssid:
            print("No WiFi network connected.")
            return
        
        # Get the WiFi password using netsh
        password_command = f'powershell.exe -Command "netsh wlan show profile name=\\"{ssid}\\" key=clear"'
        output = subprocess.check_output(password_command, shell=True).decode()

        for line in output.split("\n"):
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                print(f"Connected WiFi: {ssid}\nPassword: {password}")
                return

        print(f"Connected WiFi: {ssid}\nPassword: Not found (may be stored elsewhere)")

    except subprocess.CalledProcessError:
        print("Failed to retrieve the WiFi password.")
    except Exception as e:
        print(f"Error: {e}")

get_wifi_password()
