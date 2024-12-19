# Script to retrieve system information using WMI
import platform
import psutil
from datetime import datetime

def system_info():
    print("System Information:")
    print(f"OS Name: {platform.system()} {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Architecture: {platform.architecture()[0]}")
    print(f"Processor: {platform.processor()}")
    print(f"Total Physical Memory: {round(psutil.virtual_memory().total / (1024 ** 2), 2)} MB")
    print(f"Free Physical Memory: {round(psutil.virtual_memory().available / (1024 ** 2), 2)} MB")
    
    # Format boot time
    boot_time_timestamp = psutil.boot_time()
    boot_time = datetime.fromtimestamp(boot_time_timestamp).strftime("%Y-%m-%d %H:%M:%S")
    print(f"System Boot Time: {boot_time}")

if __name__ == "__main__":
    system_info()
    print("Thank you for using the system information tool!")
    input("Press Enter to exit.")
    exit()
    