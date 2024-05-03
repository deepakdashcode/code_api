import subprocess


command = "g++ test.cpp && ./a.out"
output = subprocess.check_output(command, shell=True)
output = output.decode("utf-8")
print(output)
