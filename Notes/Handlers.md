# Handlers

1. Handlers allows you to configure playbooks in a way that one task will only run if another task has been running successfully.

2. In other words, It is a conditional task.

3. In order to run the handler, a notify statement is used from the main task to trigger the handler.

4. Handlers are typically used to restart services or reboot hosts.

5. Handlers are executed after running all tasks in a playbook SUCCESSFULLY.

6. Handlers will only run if a task has changed something, so if an OK result instead of a changed result is reported, then the handler will not run.

7. If one of the task fails, then the handler will not run by default. 

8. A handler can be forced to run by using force_handlers: True or ignore_errors: yes

---
- name: Set Up A Web Server
  hosts: linuxclients
  force_handlers: True
  tasks:
    - name: Install HTTPD
      yum:
        name: httpd
        state: latest
    - name: Copy the Index.html file
      copy:
        src: /tmp/index.html
        dest: /var/www/html/index.html
      notify:
        - restart_web
    - name: Copy Nothing. Forcing a failure
      copy:
        src: /tmp/nothing.html
        dest: / var/www/html/nothing.html
  handlers:
    - name: restart_web
      service:
        name: httpd
        state: restarted
