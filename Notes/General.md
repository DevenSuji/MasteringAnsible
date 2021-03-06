    Inventory
    ---------

    If an inventory file is not defined by a user, then ansible uses the default inventory file located at /etc/ansible/hosts.
    Ansible inventory file can be of ini or json format.

    Inventory with Alias.

    web ansible_host=server1.example.com
    db ansible_host=server1.example.com
    mail ansible_host=server1.example.com
    ad ansible_host=server1.example.com

    In the above example web, db, mail, and ad are alias. When defining alias for a host ensure that ansible_host= is mentioned in front of the hostname.
    Other inventory parameters are:
    1. ansible_connection - ssh/winrm/localhost
    2. ansible_port - 22/5986
    3. ansible_user - root/administrator
    4. ansible_ssh_pass - Password

    In the below example hosts are mentioned along with their parameters in an inventory file.

    Example1

    web ansible_host=server1.example.com ansible_connection=ssh ansible_user=root 
    db ansible_host=server1.example.com ansible_connection=winrm ansible_user=admin ansible_port=5986 ansible_ssh_pass=P@55w0rd
    mail ansible_host=server1.example.com ansible_connection=ssh ansible_user=root
    ad ansible_host=server1.example.com ansible_connection=winrm ansible_user=admin ansible_port=5986 ansible_ssh_pass=P@55w0rd

    Example2

    # Sample Inventory File

    # Web Servers
    web1 ansible_host=server1.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
    web2 ansible_host=server2.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
    web3 ansible_host=server3.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!

    # Database Servers
    db1 ansible_host=server4.company.com ansible_connection=winrm ansible_user=administrator ansible_password=Password123!


    [web_servers]
    web1
    web2
    web3

    [db_servers]
    db1

    [all_servers:children]
    web_servers
    db_servers
    *************************************************************************************************************************
    LOOPS AND WITH_ITEMS

    Loops is the new way of using with_items.

    *************************************************************************************************************************

    ROLES
    -----

    Either the roles directory can be placed on the same level on which the playbook.yml is placed or the default roles directory can 
    be used which is /etc/ansible/roles. If the roles folder is not defined at the same level as the playbook, ansible looks at the 
    default directory /etc/ansible/roles. 

    ANSIBLE GALAXY COMMANDS

    1. ansible-galaxy search <nameOfRole> ---> To search the desired role in Ansible Galaxy.
    2. ansible-galaxy install <nameOfRole> ---> To use the role.
    3. ansible-galaxy list ---> To see the list of roles downloaded.
    4. ansible-config dump | grep ROLE ---> To see the default path of the role.
    5. ansible-galaxy install <RoleName> -p ./roles ---> To download the role from ansible galaxy to the current directory.

    Below are the examples of how to call the role from the playbook

    Example 1
    ---
    - name: Install and Configure MySQL
      hosts: someserver
      roles:
        - geerlingguy.mysql
        - nginx

    Example 2
    ---
    - name: Install and Configure MySQL
      hosts: db-servers
      roles:
        - geerlingguy.mysql

    - name: Install and Configure Web Server
      hosts: web-server
      roles:
        - nginx

*************************************************************************************************************************

ANSIBLE ORDER OF OPERATION

Within a play, there are a few more operations. While a playbook is strictly ordered from top to bottom, 
a play has a more nuanced order of operations. Here is a list of the possible operations and the order 
in which they will happen:

1.  Variable loading
2.  Fact gathering
3.  The pre_tasks execution
4.  Handlers notified from the pre_tasks execution
5.  Roles execution
6.  Tasks execution
7.  Handlers notified from roles or tasks execution
8.  The post_tasks execution
9.  Handlers notified from the post_tasks execution

*****************************************************************************************************

***********************************************************************************************
VARIABLES
---------
If a variable is used at the start of an ITEM then it needs to be double quoted like,
name:
    - "{{ variable1 }}"
    - "{{ variable2 }}"

If a variable is used at the middle of an ITEM the it does not need to be double quoted like,
    - name: Start and Enable {{ firewall_service }}

MAGIC VARIABLES
---------------

- name:
  package:
    name: vsftpd
  when: inventory_hostname in groups["ftpservers"]

***********************************************************************************************
ENABLING ROOT SSH ON UBUNTU
---------------------------

sudo passwd root
sudo passwd -u root 
sudo sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
***********************************************************************************************
LOOPS
-----

*** WITH_ITEMS


This is just an equivalent of foreach loop in PowerShell. See the example below

- name: Ensuring httpd and vsftpd are running
  service:
    name: "{{ item }}"
    state: started
  with_items:
    - httpd
    - vsftpd

The list of items can be provided using variable as well. See the example below

vars:
  web_services:
    - httpd
    - vsftpd

tasks:
  - name: start web services
    service:
      name: "{{ item }}"
      state: started
    with_items: "{{ web_services }}"

Items can be defined as a hash/dictionary, where each item has a multiple keys. Refer to the items using item.key1 and item.key2

- name: Manage users and group membership
  user:
    name: "{{ item.name }}"
    state: present
    groups: "{{ item.groups }}"
  with_items:
    - {name: 'linda', groups: 'students'}
    - {name: 'anna', groups: 'profs'}

Other LOOPS

*** with_file: A list of file names, item is set to the content of each file.

*** with_fileglob: Same as with_file, but allows globbing patterns in the file names.

*** with_sequence: Generates a sequence of items in increasing numerical order. Can work with start and end to define a range,
    using decimal, octal, or hexadecimal integer value.
    
*** with_random_choice: Takes a list, and item is set to one of the list items at random.

***********************************************************************************************
CONDITIONS
----------

1. Equal on strings ---> ansible_machine == "x84_64"
2. Equal on numeric ---> max_memory == 1024
3. Less than        ---> min_memory < 256
4. Greater than     ---> max_memory > 2048
5. Less than or equal to       ---> min_memory <= 256
6. Greater than or equal to       ---> max_memory >= 2048
7. Not equal to       ---> min_memory != 1024
8. Variable exists      ---> myvar is defined
9. Variable does not exist      ---> myvar is not defined
10. Variable is a boolean      ---> myvar
11. Variable is a boolean false       ---> not myvar

Example1

---
- hosts: all
  vars:
    to_install: samba

  tasks: 
    - name: Installing {{ to_install }}
      package:
        name: "{{ to_install }}"
      when: to_install is defined

Example2

---
- hosts: all
  vars:
    my_user: linda

  superusers:
    - root
    - linda

  tasks:
    - name: Run only if Linda is superusers
      user:
        name: "{{ my_user }}"
        groups: wheel
        append: yes
      when: my_user in superusers

Example of When Conditions

1. ansible_system_vendor == "VMware, Inc." and ansible_processor_cores == 1
2. ansible_distribution == "CentOS" or ansible_distribution == "Fedora"
3. (ansible_distribution == "CentOS" and ansible_processor_cores == 1) or (ansible_distribution == "Fedora" and ansible_system_vendor == "VMware, Inc.")

***********************************************************************************************



***********************************************************************************************
ANSIBLE FACTS
--------------
ansible all -m setup -a "filter=ansible_distribution" >>> To capture a particular ansible fact. Here the fact is ansible_distribution
ansible all -m setup >>> To look into all the facts of each machine.

***********************************************************************************************

COMBINING LOOPS AND CONDITIONS

---
- name: Install vsftpd if sufficient space on /var/ftp
  package:
    name: vsftpd
    state: lastest
  with_items: "{{ ansible_mounts }}"
  when: item.mount == "/var/ftp" and item.size.available > 9000000000

  ***********************************************************************************************

  HANDLERS
  --------

  1. A handler is a task that is going to be executed if another task is successfull. 
  2. A handler is a conditional task that only runs after being notified  by another task.
  3. Handlers have a globally unique name and are triggered after all tasks in the playbook.
  4. Apart from that a handler is triggered by one or kore other tasks in the playbook; all of its properties are task properties.
  5. To trigger a handler, the playbook must have a notify: item, that calls the name of the handler.
  6. More than one handler can be called from a task.
  7. Handlers always run in the order in which the handlers section is written, not in the order of how the are called in the plays.
  8. Handlers run after all the other tasks in the playbook runs first. Once all the tasks are run, only then the handlers are run.
  9. Handler names must be globally unique, they are defines in the gloabl area like config variables.
  10. Handlers cannot be included.

***********************************************************************************************

TAGS
----

1. Tags are used at a resource level to give a name to a specific resource.
2. The --tags option is used with ansible-playbook to run only resources with a specific tag.
3. When a task file is included in a playbook, it can be tagged in the include statement.
4. Note that when tagging a role or inclusion, the tag applies to everything in the role or the inclusion.
5. When ansible-playbook --tags 'tagname' is used, only resources marked with those tags will run. This means 
   that if a resource at the same level doesn't have a tag, it won't run.
6. Tags can also be used as --skip-tags 'tagname' to exclude resources with a specific tag.
7. There is a special tag call always. This can be used to make sure a resource is always executed, unless specifically
   excluded with --skip-tags option. 
8. The --tags option has has 3 specific tags as arguments
    ... tagged runs any tagged resources.
    ... untagged excludes all the tagged resources
    ... all runs all tasks (which is default behaviour ans also happens if no tags have been specified)


***********************************************************************************************

ERROR HANDLING
--------------

1. Default behavior: On failure, play execution stops, exceptions are possible.
2. Use ignore_errors to continue after the failure

Example.

---
- package
    name: boris
    state: lastest
  ignore_errors: yes

EXEDCUTION HANDLERS EVEN AFTER TASK FAILURE
-------------------------------------------

1. If a task in a play failes, then no handlers will be executed. This is the default behaviour.
2. Use force_handlers: yes to execute handlers that were triggered by a previous action anyway

Example.

---
- hosts: all
  force_handlers : yes
  tasks: 
    - name: task a
      command: /bin/yes
      notify: handlera
  
  handlers:
    - name: handlera
        command: /bin/true


USING FAILED_WHEN
-----------------
1. failed_when can be used to specify when a command is considered failed.
2. Useful for commands that produce a specific output.

Example.

---
tasks:
  - shell: /usr/local/bin/mkusr.sh
    register: mkusr_result
    failed_when: "'Password missing' in mkusr_result.stdout

USING CHANGED_WHEN
------------------

1. If a module thinks that it changed the state of the affected machine, it will report "changed" status.
2. This is not always true or desired and for that reason may be overwritten or further specified.
3. As a result, the module will not generate a "changed" state.

Example.

- shell: wall 'beep'
  changed_when: false
***********************************************************************************************
ROLES
-----

1. Even simple projects should have their own directory structure.
2. Withing that directory structure you'll have the ansible.cfg, inventory as well as playbooks.
3. If the project grows bigger, variable files as well as includes may be used.
4. Roles can be used to standardize and easily reuse specific parts of ansible.
5. Consider a role as a complete project dedicated to a specific task that is going to be included from the main playbook.
6. Best practices are defined in the Ansible Documentation: https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html


a. Ansible Roles provides uniform ways to load tasks, handlers, and variables from external files.
b. A role typically corresponds to the type of service that is offered(web, databse, etc.)
c. The purpose if to keep the size of playbooks manageable.
d. Roles use a specific directory structure, with locations for defaults, handlers, tasks, templates, and variables.
e. When working with roles, generic profiles are defined in a role.
f. For specific (groups of) servers, specific playbooks may be created to include one or more roles.
g. To manage what should happen, default variables are set in the role, which can be overwritten at the playbook level.
h. To make working with roles easier, community roles can be downloaded from Ansible Galaxy.
i. Roles are defined in a roles directory, which is created in project directory.
j. Jinja2 templates are very useful in roles, as they allow working with flexible parameters that are set as variables or facts.

Role Directory Structure Contents
1. defaults: Contains a main.yml with default values for variables.
2. files: Static files that are referenced by role tasks.
3. handlers: Contains a main.yml with handler definitions.
4. meta: Contains main.yml with information about the rols, including author, license, platforms, and dependencies.
5. tasks: Has a main.yml file with task definitions.
6. vars: Has a main.yml file with role variable definitions.

Understanding Role Variables.
1. Role variables are defines in vars/main.yml.
2. These variables have a high priority and cannot be overridden by inventory variables.
3. Default variables can be defined in defaults/main.yml and have the lowest precedence.
4. Use default variable only if you intend to have the variable overidden somewhere else.
  a. Overriding variables is common as roles are used as templates, where specific variables may be overridden in specific playbook. 

Rough Syntax of using roles.

---
- hosts: server1.example.com
  roles:
    - role1
    - role2

Defining Role Dependencies in meta/main.yml

a. Roles may include other roles.
b. Dependencies are written to the meta/main.yml withing the role.

---
dependencies:
  - { role: apache, port: 80 }
  - { role: mariadb, dbname: addresses, admin_user: bob }



Order Of Execution

a. Normally, tasks in a role execute before the tasks of the playbook using them.
b. Two solutions to override that are:
  1. pre_tasks are performed before roles are applied.
  2. post_tasks are performed after completing all roles.

Pre/Post tasks execution examples.

---
- hosts: server1.example.com
  pre_tasks:
    - debug:
        msg: 'starting'

  roles: 
    - role1
    - role2
  tasks: 
    - debug:
        msg: 'still working'

  post_tasks:
    - debug:
        msg: 'goodbye'

Role Structure Example (motd)

roles/
|-- motd
  |-- defaults
  |   |-- main.yml
  |-- files
  |-- handlers
  |-- tasks
  |   |-- main.yml
  |-- templates
      |-- motd.j2
***********************************************************************************************
DRY RUN

ansible-playbook -C playbook.yaml

      