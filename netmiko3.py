# from netmiko import Netmiko
# connection = Netmiko(host='10.1.1.10', port='22', username='u1', password='cisco', device_type='cisco_ios')

from netmiko import ConnectHandler
# creating a dictionary for the device to connect to
cisco_device = {
       'device_type': 'cisco_ios',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
       'host': '10.0.0.1',
       'username': 'FA',
       'password': '1234',
       'port': 22,             # optional, default 22
       'secret': 'cisco',      # this is the enable password
       'verbose': True         # optional, default False
       }

# connecting to the device and returning an ssh connection object
connection = ConnectHandler(**cisco_device)

# sending a command and getting the output

#prompt = connection.find_prompt()
#if '>' in prompt:
 #   connection.enable()
output = connection.send_command('sh run')
print(output)
if  not connection.check_config_mode():
    connection.config_mode()


#print(connection.check_config_mode())
#connection.send_command('username u1 secret cisco')

connection.exit_config_mode()
print(connection.check_config_mode())

# closing the connection
print('Closing connection')
connection.disconnect()