from io import StringIO
import sys
stdout = sys.stdout
sys.stdout = StringIO()

try:
    exec("print('Hello, world!')")
finally:
    output = sys.stdout.getvalue()
    sys.stdout = stdout

print("Output is :", output)
