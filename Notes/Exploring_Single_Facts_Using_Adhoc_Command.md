# Grabbing the Ansible Distribution
ansible all -m setup -a "filter=ansible_distribution"
ansible all -m setup -a "filter=ansible_memfree_mb"