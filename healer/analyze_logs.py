import os

print("Analyzing Jenkins build logs...")

try:
    with open("build.log", "r") as file:
        logs = file.read()

    if "BUILD FAILURE" in logs:
        print("Build failure detected!")

        os.system("python3 healer/auto_fix.py")

    else:
        print("No failures detected")

except FileNotFoundError:
    print("build.log file not found")