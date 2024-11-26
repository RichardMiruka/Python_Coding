import time

print("Press Enter to start the stopwatch.")
print("Press Ctrl + C to stop the stopwatch.")

try:
    input("Press Enter to start...\n")
    start_time = time.time()  # Record the start time
    
    print("Stopwatch is running. Press Ctrl + C to stop.")
    while True:
        # Display elapsed time dynamically
        elapsed_time = time.time() - start_time
        print(f"Elapsed Time: {round(elapsed_time, 2)} seconds", end="\r")
        time.sleep(0.1)  # Update every 0.1 seconds

except KeyboardInterrupt:
    # Handle Ctrl + C to stop the stopwatch
    print("\nStopwatch stopped.")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total time: {round(elapsed_time, 2)} seconds")

except Exception as e:
    # Handle unexpected errors
    print(f"\nAn error occurred: {e}")

print("\nThank you for using the stopwatch!")
