import os

print("Starting self-healing process...")

with open("build.log", "r") as file:
    logs = file.read()

# Detect compilation error
if "COMPILATION ERROR" in logs:

    print("Compilation error detected")

    java_file = "sample-java-app/sampleapp/src/main/java/com/autoheal/App.java"

    with open(java_file, "r") as file:
        lines = file.readlines()

    fixed_lines = []

    for line in lines:

        # Auto-fix missing semicolon
        if 'System.out.println("AutoHealCI Test")' in line and ';' not in line:
            line = line.strip() + ';\n'
            print("Missing semicolon fixed automatically")

        fixed_lines.append(line)

    with open(java_file, "w") as file:
        file.writelines(fixed_lines)

    print("Retrying Maven build...")

    os.system("cd sample-java-app/sampleapp && mvn clean install")

else:

    print("Cleaning Maven cache...")
    os.system("rm -rf ~/.m2/repository")

    print("Retrying build...")
    os.system("cd sample-java-app/sampleapp && mvn clean install")

print("Healing attempt completed")