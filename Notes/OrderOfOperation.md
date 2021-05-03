1.  Nearly everything in Ansible can be assumed to be executed in a top-to-bottom order; that is, the operation listed 
    at the top of a file will be accomplished before the operation listed at the bottom of a file. However there are ways
    to influence the order of operation.

    A playbook has only two main operations it can accomplish. It can either run a play, or it can include another playbook 
    from somewhere on the filesystem. The order in which these are accomplished is simply the order in which they appear in 
    the playbook file, from top to bottom.

    It is important to note that while the operations are executed in order, the entire playbook and any included playbooks are 
    completely parsed before any executions. This means that any included playbook file has to exist at the time of the playbook 
    parsing. They cannot be generated in an earlier operation or a play or a script during the execution.

    Within a play, there are a few more operations. While a playbook is strictly ordered from top to bottom, a play has a more 
    nuanced order of operations. Here is a list of the possible operations and the order in which they will happen:
        1. Variable loading
        2. Fact gathering
        3. The pre_tasks execution
        4. Handlers notified from the pre_tasks execution
        5. Roles execution
        5. Tasks execution
        6. Handlers notified from roles or tasks execution
        7. The post_tasks execution
        8. Handlers notified from the post_tasks execution
    
    There is a utility module, meta, which can be used to trigger handler processing at a specific point:

        - meta: flush_handlers
    
    This will instruct Ansible to process any pending handlers at that point before continuing on with the 
    next task or next block of actions within a play.

    Understanding the order and being able to influence the order with flush_handlers is another key skill to 
    have when there is a need for orchestrating complicated actions, where things such as service restarts are 
    very sensitive to order. Consider the initial rollout of a service.