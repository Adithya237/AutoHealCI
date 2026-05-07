import os

print("Starting self-healing process...")

print("Cleaning Maven cache...")

os.system("rm -rf ~/.m2/repository")

print("Retrying Maven build...")

os.system("cd sample-java-app/sampleapp && mvn clean install")

print("Healing attempt completed")