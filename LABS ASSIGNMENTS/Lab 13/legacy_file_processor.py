# legacy_file_processor.py

import time

start_time = time.time()

errors = []
file = open("system_logs.txt", "r")
lines = file.readlines()

for line in lines:
    if "ERROR" in line:
        errors.append(line)

file.close()

end_time = time.time()
execution_time = end_time - start_time

print("Total Errors:", len(errors))
print(f"Execution Time (Legacy): {execution_time:.6f} seconds")
