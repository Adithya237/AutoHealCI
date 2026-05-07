import os

print("Starting self-healing process...")

print("Cleaning Maven cache...")
os.system("rm -rf ~/.m2/repository")

print("Checking for syntax issues...")

with open("build.log", "r") as file:
    logs = file.read()

if "COMPILATION ERROR" in logs:
    print("Compilation error detected")
    print("Manual developer intervention required")

else:
    print("Retrying Maven build...")
    os.system("cd sample-java-app/sampleapp && mvn clean install")

print("Healing attempt completed")