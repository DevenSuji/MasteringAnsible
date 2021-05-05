# Facts about Ansible_Facts

1. By default, all playbooks perform fact gathering before running the actual plays.
2. You can run fact gathering in an adhoc command using the setup module
3. To show the facts, use the debug module to print the value of the ansible_fact variable.
4. Notice that in facts, a hierarchical relationship is shown where you can use the dotted format to refer to a specific fact.

# How to Enable or Disable facts gathering

File Name: ansible.cfg
By default gathering facts is enabled.

Gathering facts can be disabled by using gather_facts: no under hosts at the playbook level.

Gathering facts can also be disabled by adding gathering = explicit in the ansible.cfg file.

There are three settings that can he set for gathering in the ansible.cfg file.
+ implicit: Which is by default facts gathering is enabled.
+ explicit: Facts gathering is disabled for all playbook runs.
+ smart: It gathers the facts for a machine only once and reuses the same fact.

Even if fact gathering is disabled, it can be enabled again by running the setup module in a task.