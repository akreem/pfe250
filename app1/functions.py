from time import sleep
import paramiko

def HostnameFunc(router_p):
    try:
        router = router_p
        
        # Create an ssh connection and set terminal length 0
        conn = paramiko.SSHClient()
        conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        conn.connect(router, username="amine", password="amine123")
        router_conn = conn.invoke_shell()
        
        print('Successfully connected to %s' % router)
        
        router_conn.send('show ip route\n')
        sleep(1)  # Wait for the cmd to be sent and processed
        
        # Send the command and wait for it to execute
        router_conn.send(' enable\n')
        sleep(2)
        router_conn.send(' amine123\n')
        sleep(3)
        router_conn.send('configure terminal\n')
        sleep(4)
        # Read the output, decode into UTF-8 (ASCII) text, and print
        return router_conn.recv(5000).decode("utf-8")
    
    except Exception as e:
        return f'An error occurred {e}'