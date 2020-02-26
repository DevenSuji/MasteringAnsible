ANSIBLE BLOCKS
--------------

1. Blocks are used to logically group tasks.
2. Blocks are useful for error handling and when statements: one statement can be  applied to the block that it affects all the tasks in the block.
3. Blocks allow for error handling, combined with the RESCUE and ALWAYS statements.
    - If a task fails, the tasks in the RESCUE task are executed for recovery.
    - Task in ALWAYS will run, regardless of the success or failure of the tasks defines in BLOCK and RESCUE.
    