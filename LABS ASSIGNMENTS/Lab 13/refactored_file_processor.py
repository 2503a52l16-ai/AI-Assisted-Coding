# refactored_file_processor.py

import time

def extract_errors(filename):
    # Using generator expression for better memory efficiency
    with open(filename, "r") as file:
        return [line for line in file if "ERROR" in line]

start_time = time.time()

errors = extract_errors("system_logs.txt")

end_time = time.time()
execution_time = end_time - start_time

print("Total Errors:", len(errors))
print(f"Execution Time (Refactored): {execution_time:.6f} seconds")
