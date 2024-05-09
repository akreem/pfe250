from time import sleep
from netmiko import ConnectHandler
import paramiko

def HostnameFunc(router_p,verification):
    try:
        router = router_p
        
        # Create an ssh connection and set terminal length 0
        conn = paramiko.SSHClient()
        conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        conn.connect(router, username="amine", password="amine123")
        router_conn = conn.invoke_shell()
        
        print('Successfully connected to %s' % router)

        if verification == 'configuration':
            router_conn.send('show ip running-config\n')

        elif verification == 'route':
            router_conn.send('show ip route Running\n')

        elif verification == 'vrf':
            router_conn.send('show ip vrf\n')

        elif verification == 'protocols':
            router_conn.send('show ip protocols\n')

        # Read the output, decode into UTF-8 (ASCII) text, and print
        return router_conn.recv(5000).decode("utf-8")
    
    except Exception as e:
        return f'An error occurred {e}'

def eigrpFunc(hostip,eigrpprocid,network_i):
    device = {
    'device_type': 'cisco_ios',
    'host': hostip,
    'username': 'amine',
    'password': 'amine123',
    'secret': 'amine123'
    }
    myssh = ConnectHandler(**device)
    hostname = myssh.send_command('show run | i host')
    x = hostname.split()
    device = x[1]
    #eigrpprocid = input('EIGRP Process ID #: ')
    routereigrp = 'router eigrp ' + eigrpprocid
    config_commands = [routereigrp]
    output = myssh.send_config_set(config_commands)
    print(output)
    #network_i = input('Please specify the network and mask to enable[10.1.0.0]: ')
    network_e = 'network ' + network_i
    config_commands = [routereigrp,network_e]
    output = myssh.send_config_set(config_commands)
    print(output)
    return('Router \"' + device + '\" configured')

def ospfFunc(hostip,ospfprocid,network_i,area_id):
    device = {
    'device_type': 'cisco_ios',
    'host': hostip,
    'username': 'amine',
    'password': 'amine123',
    'secret': 'amine123'
    }
    myssh = ConnectHandler(**device)
    hostname = myssh.send_command('show run | i host')
    x = hostname.split()
    device = x[1]
    #ospfprocid = input('OSPF Process ID #: ')
    routerospf = 'router ospf ' + ospfprocid
    config_commands = [routerospf]
    output = myssh.send_config_set(config_commands)
    print(output)
    #network_i = input('Please specify the network and mask to enable[10.1.0.0 0.0.255.255]: ')
    #area_id = input('Enter the area to assign this network to: ')
    network_e = 'network ' + network_i + ' area ' + area_id
    config_commands = [routerospf,network_e]
    output = myssh.send_config_set(config_commands)
    print(output)
    return('Router \"' + device + '\" configured')

def changehostnameFunc(iprouter,hostname):
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
    return('Router \"' + device + '\" configured')

def set_interfaceFunc(iprouter,interface,description,network,Masque):
    device = {
    'device_type': 'cisco_ios',
    'ip': iprouter,        
    'username': 'amine',     
    'password': 'amine123',     
    'secret': 'secret', 
    }
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    #interface= input('Interface à configurer: ')
    #description= input('description : ' )
    description_conf= 'description' +' '+ description
    #network = input(' Network : ')
    #Masque = input(' Masque: ')
    network_conf= 'ip add' +' '+ network +' '+ Masque
    interface_conf= 'interface' +' ' + interface
    interface_config = [interface_conf,description_conf,network_conf,'no shutdown','exit']
    output = net_connect.send_config_set(interface_config)
    # Disconnect from the device
    net_connect.disconnect()
    return output


def rip_Func(hostip,network_i):
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

    routerrip = 'router rip '
    network_e = 'network ' + network_i
    config_commands = [routerrip,
                            network_e]
    output = myssh.send_config_set(config_commands)
    return output + 'Router \"' + device + '\" configured'

def vrfcreate(hostip,vrf_id,rd_id,rt_id,interface,ip_int):
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
    vrf = "ip vrf" + " " + vrf_id
    rd = "rd " +" "+ rd_id +':'+ rt_id
    rt = "route-target"+" "+"both"+" "+ rd_id + ":" + rt_id
    inte="int"+" "+interface
    int_f="ip vrf forwarding"+" "+vrf_id
    ip_add="ip add"+" "+ip_int
    config_commands = [vrf, rd, rt, inte, int_f, ip_add
                        ]
    output = myssh.send_config_set(config_commands)
    return output + 'Router \"' + device + '\" configured'
