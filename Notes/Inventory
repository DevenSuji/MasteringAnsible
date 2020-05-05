EXAMPLE OF INVENTORY
--------------------

[local]
localhost ansible_connection=local

[app]
app1
app2

[lb]
lb

[db]
db

[prod:children]
app
lb
db

In the above inventory file, prod group is a group of groups defined with the help of children tag.
***********************************************************************************************
RANGES
------

servername[1:20] >>> This inventory list matches servername1 to servername20.

192.168.[4:5].[0.255] >>> This matches two full class C subnets.

***********************************************************************************************
LIMITING
--------

ansible app1:app2:db:lb:localhost -m ping -o # Here the inventory is defined in ansible.cfg file. ansible.cfg file is placed on the same level of directory from 
where we are running this adhoc command.

ansible all -m ping --limit lb # Here we are asking the command to run only on the node lb.
***********************************************************************************************
EXCLUSION
---------

ansible 'prod:!lb' -m ping

In the above command though lb is part of prod group, however ansible will not execute the command against lb as it is exculded.

ansible 'prod:!lb:!db' -m ping # Example of multiple exclusion.

ansible 'prod[0:2]' -m ping # This methog will execute command on the first three hosts.

ansible 'prod[2:]' -m ping # This methog will execute command only after the first two hosts in the inventory

ansible '~(app|db).*' -m ping # Using regular expression to execute commands only on hosts that have the group name app and db

ansible '~(app|db).*' -m ping -f 1 # -f is fork. This will execute commands against the number of forks mentioned. Here the command will run one at a time.
***********************************************************************************************

USEFUL ADHOC COMMANDS
---------------------

ansible all -a "uptime"
ansible all -a "hostname"
ansible all -a "free"
ansible all -a "free -m"
ansible all -b -a "yum install -y vim" # -b here is become. User will become root here. -a is the argument or the raw command that we want to run on the end node.
ansible all -b -a "useradd apple"
***********************************************************************************************
INVENTORY

1. Example of a machine in the inventory that needs to be connected on a different port.

	host1.example.com:50882
***********************************************************************************************
2. RANGE EXPANSION FUNCTIONALITY.
	
Large number of servers that share a common naming convention.
	host[1:3].example.com
	This is functionally equal to 
	host1.example.com
	host2.example.com
	host3.example.com

Range expansion also supports leading zeros ( [01:03] ) and alphabetic ranges
( [a:z] ). Unfortunately, only the range a:z is supported; that is, you can’t specify a range
such as [aa:dz] , as Ansible does not know how to cope with this. If you need to define a
range like this, you need to use two ranges :
host[a:d][a:z].example.com

If you’re familiar with Python’s slice syntax, this may look familiar to you. As with
slice, you can specify an optional third parameter step :

host[min:max:step].example.com

Step allows you to specify the increment between each host. There aren’t many use
cases for this, but the inventory file supports it nonetheless:

host[1:6:2].example.com

is equivalent to:

host1.example.com
host3.example.com
host5.example.com
***********************************************************************************************

EXAMPLE OF A COMPLEX INVENTORY FILE
-----------------------------------

[web_centos5]
worker1.sikkim.com ansible_user=devensuji ansible_ssh_private_key_file=devensuji.key
worker2.sikkim.com ansible_user=devensuji ansible_ssh_private_key_file=devensuji.key

[web_centos6]
worker[1:2].sikkim.com ansible_user=automation ansible_port=50022 ansible_ssh_private_key_file=/path/to/auto.key

[database_centos6]
db.example.com ansible_user=michael ansible_ssh_private_key_file=/path/to/db.key

[loadbalancer_centos6]
lb.example.com ansible_user=automation ansible_port=50022 ansible_ssh_private_key_file=/path/to/lb.key

[web_centos5]
fe1.example.com ansible_user=michael ansible_ssh_private_key_file=michael.key
fe2.example.com ansible_user=michael ansible_ssh_private_key_file=michael.key

[web_centos6]
web[1:3].example.com ansible_user=automation ansible_port=50022 ansible_ssh_private_key_file=/path/to/auto.key

[database_centos6]
db.example.com ansible_user=michael ansible_ssh_private_key_file=/path/to/db.key

[loadbalancer_centos6]
lb.example.com ansible_user=automation ansible_port=50022 ansible_ssh_private_key_file=/path/to/lb.key

[web:children]
web_centos5
web_centos6

[database:children]
database_centos6

[loadbalancer:children]
loadbalancer_centos6

***********************************************************************************************
DYNAMIC INVENTORY
-----------------
When you call Ansible, it will check to determine if the file passed in as the inventory file is executable. 
If it is, the file will be executed, and Ansible will switch to using its JSON parser to read the incoming data. 
If it’s not executable, it will be read by Ansible with the assumption that it’s in the INI file format, and it 
will fail to be parsed if it is a static JSON file.