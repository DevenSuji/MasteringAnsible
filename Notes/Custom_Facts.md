Custom facts allow administratos to dynamically generate variables which are stored as facts

Custom facts are stored in an ini or json file in the /etc/ansible/facts.d directory on the managerd host
    The name of these files must end in .fact

Custom facts are stored in the ansible_facts.ansible_local variable

Use ansible hostname -m setup -a "filter=ansible_local" to display local facts
