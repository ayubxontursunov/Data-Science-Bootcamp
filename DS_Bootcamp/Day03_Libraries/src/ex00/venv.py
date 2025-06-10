import os

def main():
    venv_path = os.environ.get('VIRTUAL_ENV')
    if venv_path:
        print(f"Your current virtual env is {venv_path}")
    else:
        print("No virtual environment is currently active.")

if __name__ == "__main__":
    main()