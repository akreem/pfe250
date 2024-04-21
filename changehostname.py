from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render
from netmiko import ConnectHandler
iprouter= input('Router IP : ')
hostname= input('nouveau Nom :')
device = {
    'device_type': 'cisco_ios',
    'host': iprouter ,
    'username': 'amine',
    'password': 'amine123',
    'secret': 'amine123',
}
net_connect = ConnectHandler(**device)
net_connect.enable()

nouveau_nom_hote = hostname

net_connect.config_mode()

output = net_connect.send_config_set(['hostname ' + nouveau_nom_hote])

net_connect.exit_config_mode()

output += net_connect.save_config()

print(output)

net_connect.disconnect()
print('Router \"' + device + '\" configured')
print('-'*79)

input("Press ENTER to finish")
