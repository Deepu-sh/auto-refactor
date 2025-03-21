import os
import subprocess

def run_command(command):
    """Run a shell command and print output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    return result.stdout

def lint_code():
    """Run Pylint to detect code issues."""
    print("\n🔍 Running Pylint...")
    run_command("pylint --disable=R,C my_script.py")

def check_complexity():
    """Use Radon to find complex functions."""
    print("\n🔍 Checking Code Complexity with Radon...")
    run_command("radon cc my_script.py -a")

def find_unused_code():
    """Detect unused functions & variables."""
    print("\n🔍 Detecting Unused Code with Vulture...")
    run_command("vulture my_script.py")

def find_duplicate_code():
    """Check for duplicate functions."""
    print("\n🔍 Checking Duplicate Code with Flake8...")
    run_command("flake8 --select=D my_script.py")

def format_code():
    """Auto-fix formatting and styling issues."""
    print("\n♻️ Formatting Code with Black and AutoPEP8...")
    run_command("black my_script.py")
    run_command("autopep8 --in-place --aggressive my_script.py")

def refactor_imports():
    """Sort and optimize imports."""
    print("\n♻️ Sorting Imports with isort...")
    run_command("isort my_script.py")

def optimize_code():
    """Run all optimization steps."""
    lint_code()
    check_complexity()
    find_unused_code()
    find_duplicate_code()
    format_code()
    refactor_imports()
    print("\n✅ Code Refactoring Completed!")

if __name__ == "__main__":
    optimize_code()
