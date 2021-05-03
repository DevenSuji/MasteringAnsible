ORDER OF PRECEDENCE OF ANSIBLE.CFG FILE
---------------------------------------

1. /etc/ansible/ansible.cfg is the default.
2. ~/.ansible.cfg if exists will overwrite the default.
3. ./ansibe.cfg is the configuration file in the current Ansible project directory and it will always have precedence if it exists.

