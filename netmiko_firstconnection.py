from netmiko import Netmiko
#giving your oject and set a value Netmiko(host , port , username, password, device_type
connection = Netmiko(host='10.0.0.1', port='22', username='FA', password='1234', device_type='cisco_ios')



# sending a command and getting the output
output = connection.send_command('sh ip int brief')
print(output)


# closing the connection
print('Closing connection')
connection.disconnect()