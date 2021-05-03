*** Arrays provide a list of items, where each item can be addressed seperately.

    users:
    - username: linda
      shell: /bin/bash
    - username: lisa
      shell: /bin/tsh

*** Individual items in the array can be addressed, using the {{ var_name[0] }} notation.

*** To access all the variables, you can use with_items ot loop.
