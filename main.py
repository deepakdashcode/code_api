from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from io import StringIO
import sys
import subprocess
import re


app = FastAPI()


class Code(BaseModel):
    code: str
    lang: str = "python3"



@app.get("/")
async def root():
    return {"Message" : "Hello World"}

@app.get("/home")
async def home():
    return {"Message" : "You are in home now"}

@app.post("/execute")
async def execute(payLoad: Code):
    if payLoad.lang.lower() == "python3":
        stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            exec(payLoad.code)
        except Exception as e:
            print(str(e))
        finally:
            output = sys.stdout.getvalue()
            sys.stdout = stdout
        print(payLoad)
        return {'Ececuted': f'output generated is {output}'}
    
    if payLoad.lang.lower() in ('c', 'c++', 'cpp'):
        with open('test.cpp', 'w') as f:
            f.write(payLoad.code)
        command = "g++ test.cpp && ./a.out"
        output = subprocess.check_output(command, shell=True)
        output = output.decode("utf-8")
        return {'Ececuted': f'output generated is {output}'}
    
    if payLoad.lang.lower() == 'java':
        java_code = payLoad.code
        # Pattern matching of class name
        pattern = r'public\s+static\s+void\s+main\s*\(\s*String\s*\[\s*\]\s*[a-zA-Z0-9]*\s*\)\s*{'
        matches = re.findall(pattern, java_code)
        class_name = None
        if matches:
            main_method_match = matches[0]
            class_name_pattern = r'class\s+([a-zA-Z][a-zA-Z0-9]*)'
            class_name_match = re.search(class_name_pattern, java_code)
            if class_name_match:
                class_name = class_name_match.group(1)
        
        with open(f'{class_name}.java', 'w') as f:
            f.write(java_code)
        # Pattern Matching ends here
        compile_command = f"javac {class_name}.java"
        subprocess.run(compile_command, shell=True)
        run_command = f"java {class_name}"
        output = subprocess.check_output(run_command, shell=True)
        output = output.decode("utf-8")
        return {'Ececuted': f'output generated is {output}'}
