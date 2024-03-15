# Ansible

## Contents
1. What is ansible
2. Installing ansible
3. Clone a repo for roles and playbooks
4. Running a playbook
5. Example Playbook
6. Building a playbook
7. My Playbooks

## What is ansible
Ansible is a program for automating other processes. It uses playbooks to run tasks. Tasks are sequences of commands, and are organized into roles, so it is easy to identify what their proposed function is. Ansible allows a web of automated processes to all run with few inputs to command line. Make sure your references to the tasks and roles are cohesive, and the correct order of operations is applied.

## Installing ansible
`sudo apt-get install ansible`

## Clone a repo with preset roles and playbooks
`git clone yourrepo.git`

## Running a playbook
`ansible-playbook playbookname.yml`

## Example Playbook
```
---
- name: Portfolio Playbook
  hosts: localhost
  become: true

  tasks:
    
    - name: Prints Hello World
      ansible.builtin.debug:
        msg:
        - "Hello World"
```

## Making a playbook
See above example of formatting. When making a playbook, first find or make a role for what your objective you hope to achieve is. Then link the specific tasks inside the role into your playbook to perform that objective.  


## My Playbooks:
[ansible](..%2F..%2FLabs%2Fansible)

## Useful task modules

1. ansible.builtin.shell \
https://docs.ansible.com/ansible/latest/collections/ansible/builtin/shell_module.html#ansible-collections-ansible-builtin-shell-module
2. ansible.builtin.debug
https://docs.ansible.com/ansible/latest/collections/ansible/builtin/debug_module.html#ansible-collections-ansible-builtin-debug-module
3. ansible.builtin.include_role:
https://docs.ansible.com/ansible/latest/collections/ansible/builtin/include_role_module.html#ansible-collections-ansible-builtin-include-role-module
4. apt:
https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_module.html#ansible-collections-ansible-builtin-apt-module
5. template:
https://docs.ansible.com/ansible/latest/collections/ansible/builtin/template_module.html#ansible-collections-ansible-builtin-template-module