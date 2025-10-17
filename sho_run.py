

from netmiko import ConnectHandler

import getpass

username = input ('Username: ')
passwd = getpass.getpass('password: ')          # getpass the password and secret
deviceip = input ('ip or domain name?: ')
# enable = getpass.getpass('Please enter the enable secret: ')

Net_device = {                                  # creates connection to router
    "device_type": "cisco_ios",                 # device type
    "ip": deviceip,                             # device IP or (use varible)
    "username": username,               
    "password": passwd,                         # Getpass password 
    "secret": passwd                            # Getpass secret
}

device = input("what is the device?: ")

Connect_Device = ConnectHandler (**Net_device)

Connect_Device.enable()

Issue =  'show run'                                                 # Issue commands here 
Issue2 = 'show ip int br'

Output = Connect_Device.send_command(Issue)

with open(f'C:\\output\\{device}_{deviceip}.txt', "w") as f:        # where the text will be created
    f.write(f'\n{device}_{deviceip}\n')
    f.write(f'\n{Issue}\n')                                         # prints command 
    f.write('-'*75 + '\n')
    f.write(Connect_Device.send_command(Issue) +'\n')               # issues command
    f.write(f'{Issue2}\n')                                          # issues second command
    f.write('-'*75 + '\n')
    f.write(Connect_Device.send_command(Issue2) +'\n')
    f.write('\nEnd of File')
#print('\n')
print('Completed')

Connect_Device.disconnect
