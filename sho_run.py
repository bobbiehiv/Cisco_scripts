

from netmiko import ConnectHandler

import subprocess

import getpass

passwd = getpass.getpass('Please enter the password: ')   # getpass the password and secret

enable = getpass.getpass('Please enter the enable secret: ')

def Username():                     # use this function to narrow 
    Posistion_counter = 0           # down whoami windows command
    Result = subprocess.getoutput("whoami")
    for words in Result: 
        if words == "\\":
            Posistion = Posistion_counter
            break
        Posistion_counter += 1
    return Result[Posistion + 1: ]
Local_Computer_Username = Username()

# print(Local_Computer_Username)

Net_device = {                         # Creates connection to router
    "device_type": "cisco_ios",        # Device type
    "ip": "192.168.1.230",             # Router IP
    "username": "nixon",               
    "password": passwd,                # Getpass password 
    "secret": enable                   # Getpass secret
}

Connect_Device = ConnectHandler (**Net_device)

Connect_Device.enable()

Issue =  'show run'                    # Issue a command here 

Output = Connect_Device.send_command(Issue)

with open('C:\\Cisco\\Output texts\\shorun.txt', "w") as f:  # where the text will be created
    f.write('Router1 ' +  Issue)
    f.write('\n')
    f.write(Connect_Device.send_command(Issue))
    f.write('\n')
    f.write('\nEnd of File')

print(Output)
print('\n')
print('Completed')


Connect_Device.disconnect



