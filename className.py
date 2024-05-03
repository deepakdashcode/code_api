import re
with open('abc.java', 'r') as file:
    java_code = file.read()
pattern = r'public\s+static\s+void\s+main\s*\(\s*String\s*\[\s*\]\s*[a-zA-Z0-9]*\s*\)\s*{'
matches = re.findall(pattern, java_code)
class_name = None
if matches:
    main_method_match = matches[0]
    class_name_pattern = r'class\s+([a-zA-Z][a-zA-Z0-9]*)'
    class_name_match = re.search(class_name_pattern, java_code)
    if class_name_match:
        class_name = class_name_match.group(1)

print("Class with main method:", class_name)
