ansible-doc -l >>> Gives the list of all the modules

ansible-doc -s user >>> Gives a brief description of the user module.


Module way of writing the adhoc commands

 ansible all -m yum -b -a "name=vim state=present" -o

 ansible prod -b -m group -a "name=admin state=present gid=7045" -o

 ansible 'prod:!db' -m user -b -a "name=abc state=present uid=7045 group=admin" -o

 ansible app -m copy -a "src=happy.txt dest=/tmp/happy.txt mode=0644" -o

IDEMPOTENCE
-----------

In ansible all the modules are idempotent except for few of the modules. Some of them are raw, command, sheell, script and expect modules

Difference between Command and Shell Modules

Command Module:
    1. Does not use Shell.
    2. Does not have access to environment variables.
    3. > < | ; $ operators will not work.
    4. Secure and Recommended.

Shell Module:
    1. Invokes /bin/sh.
    2. Has access to env, variables etc.
    3. > < | ; $ operators will  work.
    4. Use selectively.


Examples:

ansible prod -m command -a "free" | grep -i swap >>> This will work as the the piping is happening on the control node and not on the execution node.

ansible prod -m command -a "free | grep -i swap" >>> This will not work as we are asking for the piping to happen on the execution node itself.

ansible prod -m shell -a "free | grep -i swap" >>> This will work as not we are working with the shell module and piping is allowed as explained above.

ansible prod -m raw -a "free | grep -i swap"

Checking the IDEMPOTENCE.

ansible app -m command -a "mkdir /tmp/dir1"

When you run the above command the second time it errors out stating that it cannot create the directory. Hence it shows that the command module is not Idempotent.

HOWEVER !!!!!
-------------
There is a way to make this command module Idempotent. This is by using creates.

ansible app -m command -a "mkdir /tmp/dir1 creates=/tmp/dir1"

Below is the output. It is evident that we've made the command module Idempotent now.


root@control:/workspace/ansible-bootcamp-code/chap4# ansible app -m command -a "mkdir /tmp/dir1 creates=/tmp/dir1"
 [WARNING]: Found both group and host with same name: db

 [WARNING]: Found both group and host with same name: lb

app1 | SUCCESS | rc=0 >>
skipped, since /tmp/dir1 exists

app2 | SUCCESS | rc=0 >>
skipped, since /tmp/dir1 exists