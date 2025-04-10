import json
import re

def static_code_analyzer(file_path):
    issues = []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    malloc_lines = []
    malloc_in_function = {}
    current_function = None

    for idx, line in enumerate(lines, start=1):
        # Track current function
        func_match = re.match(r'\w+\s+\w+\s*\(.*\)\s*\{?', line)
        if func_match:
            current_function = func_match.group().split()[1].split("(")[0]

        # Track malloc calls
        if re.search(r'\bmalloc\b|\bcalloc\b', line):
            malloc_lines.append(idx)
            if current_function:
                malloc_in_function.setdefault(current_function, []).append(idx)

        # Logical bug in findMin
        if 'findMin' in ''.join(lines) and re.search(r'if\s*\(.*>\s*.*\)', line):
            issues.append({"issue": "Potential logical bug", "line": idx, "severity": "low"})

        # Uninitialized variable usage
        if re.search(r'int\s+\w+;', line) and idx+1 < len(lines):
            next_line = lines[idx]
            if 'printf' in next_line and '=' not in lines[idx]:
                issues.append({"issue": "Uninitialized variable usage", "line": idx+1, "severity": "medium"})

        # Division by zero
        if '/' in line and re.search(r'=\s*0;', ''.join(lines[max(idx-3, 0):idx+2])):
            issues.append({"issue": "Potential division by zero", "line": idx, "severity": "high"})

        # Infinite loop
        if re.search(r'while\s*\(.*>=.*0.*\)', line) or 'while (1)' in line:
            issues.append({"issue": "Potential infinite loop", "line": idx, "severity": "high"})

    # Memory leak detection
    for func, malloc_line_numbers in malloc_in_function.items():
        # Check if 'free' is used in that function block
        func_start = None
        func_end = None
        # Find function block
        for i, line in enumerate(lines):
            if func in line and '(' in line and '{' in line:
                func_start = i
            if func_start is not None and '}' in line:
                func_end = i
                break
        func_block = lines[func_start:func_end+1] if func_start and func_end else lines

        if 'free' not in ''.join(func_block):
            for malloc_line in malloc_line_numbers:
                issues.append({
                    "issue": f"Possible memory leak (malloc without free in function '{func}')",
                    "line": malloc_line,
                    "severity": "medium"
                })

    return issues


if __name__ == "__main__":
    c_file_path = "non_faulty_example.c"  # Change file name
    issues_found = static_code_analyzer(c_file_path)
    print(json.dumps(issues_found, indent=4))
