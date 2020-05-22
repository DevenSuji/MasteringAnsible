
1. lininfile and blockinfile can be used to apply simple modifications to files.

2. For more advance modifications, use jinja2 templates

3. While using templates, the target files are automatically customized using variables and facts.

4. In a Jinja 2 template, you will find multiple elements

	>>> data
	>>> variables
	>>> expressions
	>>> control structures

5. The variables in the template are replaced with their values when the j2 template is rendered to the target file on the managed hosts.

6. If using variables, they can be specified using the vars section of the playbook.

7. Alternatively, Ansible facts can be used as variables.

8. To prevent Administrators from overwriting the files that are managed by Ansible, set the ansible_managed string.

	>>> First, in ansible.cfg set ansible_managed = Ansible managed
	>>> On top on the Jinja2 template, set the {{ ansible_managed }} variable.
