import psutil

# Print table headers
print(
    f"{
        'PID':<10} {
            'NAME':<40} {
                'STATUS':<20} {
                    'CPU_USAGE':<10} {
                        'MEMORY_USAGE':<10}")
print("-" * 80)

# Collect process data
process_list = []
for process in psutil.process_iter(
        ["pid", "name", "status", "cpu_percent", "memory_percent"]):
    try:
        process_list.append({
            "pid": process.info["pid"],
            "name": process.info["name"] or "N/A",
            "status": process.info["status"] or "N/A",
            "cpu_usage": process.info["cpu_percent"] or 0,
            "memory_usage": process.info["memory_percent"] or 0,
        })
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

# Sort processes by memory usage (descending)
process_list.sort(key=lambda x: x["memory_usage"], reverse=True)

# Display processes using significant memory (above 1%)
for proc in process_list:
    if proc["memory_usage"] > 1:
        print(
            f"{proc['pid']:<10} {proc['name']:<40} {proc['status']:<20} "
            f"{proc['cpu_usage']:<10.2f} {proc['memory_usage']:<10.2f}"
        )

# Calculate total usage
total_cpu = sum(proc["cpu_usage"] for proc in process_list)
total_memory = sum(proc["memory_usage"] for proc in process_list)

print("-" * 80)
print(f"Total CPU Usage: {total_cpu:.2f}%")
print(f"Total Memory Usage: {total_memory:.2f}%")
print("-" * 80)
print("Thank you for using the process monitor!")
