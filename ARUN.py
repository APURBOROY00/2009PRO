import os, platform;from time import sleep
try:
   import requests
except:
   os.system('pip install requests')


import requests
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('clear')
    print ('WELCOME 64 BIT PAID USER..!')
    sleep (2)
    from APRO import Token_token
    Token_token()

elif bit == '32bit':
    os.system('clear')
    print('WELCOME 32 BIT PAID USER..!')
    sleep (2)
    from APRO import Token_token
    Token_token()