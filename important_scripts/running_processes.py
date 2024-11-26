import psutil

# Print table headers for process information
print(f"{'PID':<10} {'NAME':<40} {'STATUS':<20} {'CPU_USAGE':<10} {'MEMORY_USAGE':<10}")
print("-" * 80)

# Iterate through all running processes using psutil
for process in psutil.process_iter(["pid", "name", "status", "cpu_percent", "memory_percent"]):
    try:
        # Retrieve process information
        pid = process.info["pid"]  # Process ID
        name = process.info["name"] or "N/A"  # Process name (default to "N/A" if unavailable)
        status = process.info["status"] or "N/A"  # Process status
        cpu_usage = process.info["cpu_percent"] or 0  # CPU usage percentage (default to 0)
        memory_usage = process.info["memory_percent"] or 0  # Memory usage percentage (default to 0)

        # Print process information in tabular format
        print(f"{pid:<10} {name:<40} {status:<20} {cpu_usage:<10.2f} {memory_usage:<10.2f}")
    
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        # Handle cases where the process no longer exists, cannot be accessed, or is a zombie process
        pass
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")

print("-" * 80)

# Print total CPU and memory usage
total_cpu_usage = psutil.cpu_percent()
total_memory_usage = psutil.virtual_memory().percent

print(f"Total CPU Usage: {total_cpu_usage:.2f}%")
print(f"Total Memory Usage: {total_memory_usage:.2f}%")

print("-" * 80)
print("Thank you for using the process monitor!")
print("Press Enter to exit.")
input()  # Wait for user input before exiting
exit()
