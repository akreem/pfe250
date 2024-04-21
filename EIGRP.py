from netmiko import ConnectHandler
hostip = input('Router IP: ')
device = {
    'device_type': 'cisco_ios',
    'host': hostip,
    'username': 'amine',
    'password': 'amine123',
    'secret': 'amine123',
}

myssh = ConnectHandler(**device)
hostname = myssh.send_command('show run | i host')
x = hostname.split()
device = x[1]

eigrpprocid = input('EIGRP Process ID #: ')
routereigrp = 'router eigrp ' + eigrpprocid
config_commands = [routereigrp
                       ]
output = myssh.send_config_set(config_commands)
print(output)
network_i = input('Please specify the network and mask to enable[10.1.0.0]: ')
network_e = 'network ' + network_i
config_commands = [routereigrp,
                           network_e]
output = myssh.send_config_set(config_commands)
print(output)
   
print('Router \"' + device + '\" configured')
print('-'*79)

input("Press ENTER to finish")
