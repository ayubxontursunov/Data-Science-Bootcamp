import sys
import subprocess
import os


if sys.prefix == sys.base_prefix:
    print("❌ Not inside a virtual environment.")
    sys.exit(1)
else:
    print("✅ Running inside a virtual environment.")


required_packages = '\n'.join([
    'beautifulsoup4',
    'pytest'
])

with open('requirements.txt', 'w') as f:
    f.write(required_packages)


subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)


result = subprocess.run([sys.executable, "-m", "pip", "freeze"], capture_output=True, text=True)
installed_packages = result.stdout.strip()


with open('requirements.txt', 'w') as f:
    f.write(installed_packages)


print("\n📦 Installed packages:\n")
print(installed_packages)

# generate zip command
# zip -r virtualenv.zip venv/

# unzip -o virtualenv.zip