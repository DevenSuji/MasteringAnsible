YAML PRIMER
-----------

YAML mainly consists of these components
1. Begin/End Tags --- and ...
---
- name: Some Playbook
  yum:
    name: nmap
    state: present
...

2. Lists : package, file and user is defines as list in the below example
---
-   name: 
    hosts:
    become:
    tasks:
        - package
        - file
        - user
...

3. Dictionaries: package, file and user are Dictionaries below having a key and a value pair
---
-   name: 
    hosts:
    become:
    tasks:
        - package: name=apache state=present
        - file: name=ntpd.conf src=file/ntpd.conf dest=/etc/ntpd.conf
        - user: name=dojo state=present
...

4. Indentation: You do know about this.

5. Line Foldings
    There are two styles of line folding. This is used when the dictionary is too long to fit in a line

    Style 1 Using > |
---
- name: Configure app hosts
  hosts: app
  become: true
  tasks:
    - package: name=apache state=present

    - copy: > # Line folding using >. This considers the complete code as one line.
        name=ntpd.conf
        src=files/ntpd.conf
        dest=/etc/ntpd.conf

    - user: | # Line folding using |. This considers the complete code as one line.
        name=dojo
        uid=5001
        home=/home/dojo
        state=present
...

    Style 2 Using :

---
- name: Configure app hosts
  hosts: app
  become: true
  tasks:
    - package: name=apache state=present

    - copy: Line folding using :. This considers the complete code as one line.
        name: ntpd.conf
        src: files/ntpd.conf
        dest: /etc/ntpd.conf

    - user: 
        name: dojo
        uid: 5001
        home: /home/dojo
        state: present
...

Playbook Options:

ansible-playbook systems.yml --list-hosts >>> Lists the hosts that ansible will run the playbook against.

ansible-playbook systems.yml --list-tasks >>> Lists the name of the tasks that ansible playbook has.

ADDING TAGS INSIDE THE PLAYBOOKS
--------------------------------

---
- name: Base System Configuration
  hosts: prod
  become: true
  tasks:
    - name: Create Admin User
      user: 
        name: admin
        uid: 5001
        state: present
      tags:
        - admin

    - name: Remove the user dojo
      user: 
        name: dojo
        state: absent

    - name: Install tree
      yum:
        name: tree
        state: present

    - name: Install ntp
      yum:
        name: ntp
        state: present


ansible-playbook systems.yml --list-tags >>> Lists the tags give to each play in the playbook.

ansible-playbook systems.yml --check >>>> Dry Run

ansible-playbook systems.yml --step >>>> Run the play step by step

ansible-playbook systems.yml --start-at-task="Name_Of_Task" >>>> Starts the play from the task name of the task mentioned and play all the tasks after it as well

ansible-playbook systems.yml --limit app >>>> Limiting the playbook to execute against the group app only.

