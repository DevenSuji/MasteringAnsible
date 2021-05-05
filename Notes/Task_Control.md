# Task Control

To control the tasks we have various control options in place.

1. Register: It is used to capture the standard output (stdout) into a variable

2. Loop: It is used to loop through a list of items. In the previous Ansible releases the looping was achieved using with_items and it is depricated now. Use loop henceforth.

3. When: It is a condition that is used against facts to derive a boolean result. Apply when condition at the task level.

4. Handler: It is a trigger that makes Handler a conditional task. For eaxmaple If Task A has run successfully then Only Run Task B. Now this task B will be the handler task.