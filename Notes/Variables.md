# Variables

Varaibles can be defined in following different places.

________________________________________________________________________________________

1. Variables can be defined in the playbook. 
   
But this makes the playbook rigid and the playbook cannt be re-used for any other purpose.

---
- name: Example of defining vars in a playbook
  hosts: all
  vars:
    web_package: httpd

________________________________________________________________________________________

2. Variables can also be defined on the hosts.

a. By defining the variables in the inventory. Not a good method.
b. By using the include method.

---
- name: Defining the variable outside the playbook in a variable file and including it in the play
  hosts: all
  vars_files:
    - vars/users.yaml

________________________________________________________________________________________

3. By using the local facts.

________________________________________________________________________________________

*** Some details of the variables:
------------------------------

1. After defining the variables, it can be used later in the playbook.

2. Order of the variable does not matter.

3. Variables can be refferd using this kind of notation {{ web_package }}

4. In conditional statements, no curly braces are needed to refere to a variable values.

    a. when: "'not found' in command_result.err"

    b. {% if ansible_facts['devices']['sdb'] is defined %}
                        OR
       {% if ansible_facts.devices.sdb is defined %}

       Secondary disk size: {{ ansible_facts['devices']['sdb']['size'] }}
       Secondary disk size: {{ ansible_facts.devices.sdb.size }}

5. If the variable is the first element, using quotes is mandatory. Look at the example below

---
- name: Create a user using a variable
  hosts: all
  vars: 
    user: lisa
  tasks:
    - name: Create a user {{ user }}
      user:
        name: "{{ user }}" ##### Since the variable is the first element double quotes is used here.


________________________________________________________________________________________
Variables are of two types:
1. Vars.
2. Facts
    
    
Vars: These are User defined and takes the below mentioned forms.
    a. Role Default Vars.
    b. Inventory Vars: hostvars and groupvars.
    c. Playbook Vars.
    d. Role Vars
    e. Extra Vars at the runtime (injected with the help of -e switch)

Defining Vars                                       Accessing Vars
-------------                                       --------------
port                                                {{ port }}

port1                                               {{ port1 }}

mysql_port                                          {{ mysql_port }}

mysql: #This is a dictionary                        {{ mysql[port] }}
  port: 3306                                        {{ mysql.port }}
  user: mysql
  server: true  

________________________________________________________________________________________

Variable Precedence
-------------------

1. -e key=value                        # Highest Precedence
2. Role Vars                                 |
3. Playbook Vars                             |
4. Host Vars                                 |
5. Group Vars                                |
6. Role Defaults                    # Lowest Precedence

________________________________________________________________________________________

Scopes of Variables:
--------------------

1. Global Scope:  This is when a variable is set from the inventory or the command line. It applies to the entire
                  playbook that you are going to run.
2. Play Scope:    This is applied when it is set from a play. It will only come into action for that specific play
                  where the variable is defined.
3. Host Scope:    This is applied when set in the inventory file or using a host variable inclusion file.






