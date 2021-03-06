# Loops

1. The loop key word allows you to iterate through a simple list of items.

2. Before Ansible 2.5, the items keyword was used instead.

3. The loop keyword is the current and latest method of looping.

4. In the previous version of Ansible, the with_* keyword was used for the same purpose.

5. The below mentioned syntax will probably be deprecated in the future versions of Ansible.
  
  A. with_items: Equivalent to the loop keyword.
  
  B. with_file: The item contains a file, which contents is used to loop through.
  
  C. with_sequence: Generates a list of values based on a numeric sequence.
____________________________________________________________________________________________
- name: start some services
  service:
    name: "{{ item }}"
    state: started
  loop:
    - vsftpd
    - httpd

### The list that loop uses can be defined by a variable as well. See the below example
- name: Start some services
  hosts: linuxclients
  vars:
    my_services:
      - httpd
      - vsftpd
  tasks:
    - name: Putting the services in a loop to get them started
      service:
        name: "{{ item }}"
        state: started
      loop: " {{ my_services }}"

### Each item in a loop can be a hash/distionary with multiple keys in each hash/dictionary. See the below example

- name: Create Users Using Loop
  hosts: ansibletower
  tasks:
    - name: Create Users
      user:
        name: "{{ item.name }}"
        state: present
        groups: "{{ item.groups }}"
      loop:
        - name: Saran
          groups: wheel
        - name: Aashish
          groups: users
