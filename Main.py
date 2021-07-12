#Hermes
import json
import os
import requests
if os.path.isfile('Settings.txt'):
    with open('Settings.txt') as settings_file:
        read_settings = settings_file.read()
    user = read_settings
    url = f'https://server.duinocoin.com/users/{user}'
    response = requests.get(url)
    if os.path.isfile('GetData.txt'):
        pass
    else:
        with open('GetData.txt', 'w+') as newfile:
            newfile.close()
        pass
    with open('GetData.txt', 'r+') as Data:
        Data.write(response.content.decode('utf-8'))
    file = open('GetData.txt', 'r+')
    ReadFile = file.read()
    JsonLoads = json.loads(ReadFile)
    Balance = JsonLoads['result']['balance']['balance']
    Username = JsonLoads['result']['balance']['username']
    print('[ BALANCE ] : ' + str(Balance))
    print('[ USERNAME ] : ' + str(Username))
    file.truncate(0)
    file.close()
    print('')
    retry = str(input('Wanna try new user? [Y/n]: '))
    if retry == 'Y' or retry == 'y':
        with open('Settings.txt', 'r+') as NewTry:
            NewTry.truncate(0)
            newuser = input('Enter new username: ')
            NewTry.write(newuser)
    elif retry == 'N' or retry == 'n':
        pass
    else:
        pass
else:
    user = input('Enter username: ')
    with open('Settings.txt', 'w+') as Settings:
        Settings.write(user)