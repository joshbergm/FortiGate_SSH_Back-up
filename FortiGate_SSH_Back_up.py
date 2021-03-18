
from netmiko import Connecthandler
import datetime

fw = {'host': '<hostname>',
           'device_type': 'fortinet',
           'ip': '<ip>',
           'username': '<username>',
           'password': '<password>'}

net_connect = Connecthandler(**fw)
output = net_connect.send_command('show full-configuration')

current_time = datetime.datetime.today().strftime('%Y_%m_%d')

with open('<path>' + str(fw['host']) + '_' + str(current_time) + '.cfg', 'w') as f:
    for line in output:
        f.write(line)