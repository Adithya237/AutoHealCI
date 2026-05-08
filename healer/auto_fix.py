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

    # Fix extra colon after semicolon
        if ");:" in line:

            print("Extra colon detected")

            line = line.replace(");:", ");")

            print("Extra colon removed automatically")

    # Fix missing semicolon
        if "System.out.println" in line:

                stripped = line.strip()

            if not stripped.endswith(";"):

                print("Missing semicolon detected")

                line = line.rstrip() + ";\n"

                print("Semicolon added automatically")

        fixed_lines.append(line)

    with open(java_file, "w") as file:
        file.writelines(fixed_lines)

    print("Retrying Maven build...")

    result = os.system(
        "cd sample-java-app/sampleapp && mvn clean install"
    )

    if result == 0:
        print("Build healed successfully!")

    else:
        print("Healing attempt failed")

else:

    print("Cleaning Maven cache...")
    os.system("rm -rf ~/.m2/repository")

    print("Retrying build...")
    os.system("cd sample-java-app/sampleapp && mvn clean install")

print("Healing attempt completed")