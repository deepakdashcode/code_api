import subprocess

# Compile Java source file
compile_command = "javac abc.java"
subprocess.run(compile_command, shell=True)

# Run compiled Java class file and capture the output
run_command = "java a"
output = subprocess.check_output(run_command, shell=True)

# Decode the byte output to string
output = output.decode("utf-8")

# Print the output
print(output)

# You can now use the 'output' variable in your Python code as needed.
