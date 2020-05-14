# ansible_maschie == "x86_64"
# ansible_distribution_major_version == "8"
# ansible_memfree_mb == 1024
# ansible_memfree_mb < 256
# ansible_memfree_mb < 256
# ansible_memfree_mb <= 256
# ansible_memfree_mb != 512
# my_variable is defined
# my_variable is not defined
# my_variable
# ansible_distribution in supported_distros

# MULTIPLE AND COMPLEX WHEN STATEMENTS

---
- name: Using Multiple Conditions
  hosts: all
  tasks: 
    - name: Installing the package
      package:
        name: httpd
        state: installed
      when: 
        - ansible_distribution == "RedHat"
        - ansible_memfree_mb > 512
        