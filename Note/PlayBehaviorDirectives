When Ansible parses a play, there are a few directives it looks for in order to define various behaviors for a play. 
These directives are written at the same level as the hosts: directive. Here is a description of the subset of the 
keys that can be used:

1.  any_errors_fatal: This Boolean directive is used to instruct Ansible to treat any failure as a fatal error to prevent 
    any further tasks from being attempted. This changes the default, where Ansible will continue until all the tasks are 
    complete or all the hosts have failed.

2.  connection: This string directive defines which connection system to use for a given play. A common choice to make here 
    is local, which instructs Ansible to do all the operations locally, but with the context of the system from the inventory.

3.  gather_facts: This Boolean directive controls whether or not Ansible will perform the fact-gathering phase of the operation, 
    where a special task will run on a host to uncover various facts about the system. Skipping fact gathering, when you are 
    sure that you do not need any of the discovered data, can be a significant time-saver in a larger environment.

4.  max_fail_percentage: This number directive is similar to any_errors_fatal, but is more fine-grained. This allows you to define 
    just what percentage of your hosts can fail before the whole operation is halted.

5.  no_log: This is a Boolean to control whether or not Ansible will log (to the screen and/or a configured log file) the command 
    given or the results received from a task. This is important if your task or return deals with secrets. This key can also be 
    applied to a task directly.

6.  port: This is a number directive to define what port SSH (or an other remote connection plugin) should use to connect unless 
    otherwise configured in inventory data.

7.  remote_user: This is a string directive that defines which user to log in with on the remote system. The default is to connect 
    as the same user that ansible-playbook was started with.

8.  serial: This directive takes a number and controls how many systems Ansible will execute a task on before moving to the next 
    task in a play. This is a drastic change from the normal order of operation, where a task is executed across every system in 
    a play before moving to the next. This is very useful in rolling update scenarios, which will be detailed in later chapters.

9.  become: This is a Boolean directive used to configure whether privilege escalation (sudo or otherwise) should be used on the 
    remote host to execute tasks. This key can also be defined at a task level. Related directives include become_user, 
    become_method, and become_flags. These can be used to configure how the escalation will occur.

10. strategy: This directive sets the execution strategy to be used for the play.      