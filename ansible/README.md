# Ansible 101

# Setup

```sh
python3 -m venv .venv
python3 -m pip install -U pip
pip install ansible
```

# Inventory

`/etc/ansible/hosts` by default. You can also create a file as follows:

```text
webservers:
  hosts:
    foo.example.com:
      ansible_user: debian
      ansible_ssh_private_key_file: /path/to/priv/key
    bar.example.com:
      ...
```

This file is provided to `ansible` with the option `-i`.

- [Full doc](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html)

# Playbook

```yaml
---
- hosts: webservers
  tasks:
    - name: ensure nginx is at the latest version
      apt: name=nginx state=latest
    - name: start nginx
      service:
          name: nginx
          state: started
```

Run it:

```sh
ansible-playbook -i inventory --private-key=.ssh/ed25519 --user=debian playbooks/install_nginx.yaml
```

Note: you can specify the user in the inventory with `ansible_user` and the private key location with `ansible_ssh_private_key_file`.

We get an error because we are not `root` and therefore cannot install anything:

```text
fatal: [foo.example.com]: FAILED! => {"cache_update_time": 1720601547, "cache_updated": false, "changed": false, "msg": "'/usr/bin/apt-get -y -o \"Dpkg::Options::=--force-confdef\" -o \"Dpkg::Options::=--force-confold\"       install 'nginx=1.22.1-9'' failed: E: Could not open lock file /var/lib/dpkg/lock-frontend - open (13: Permission denied)\nE: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), are you root?\n", "rc": 100, "stderr": "E: Could not open lock file /var/lib/dpkg/lock-frontend - open (13: Permission denied)\nE: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), are you root?\n", "stderr_lines": ["E: Could not open lock file /var/lib/dpkg/lock-frontend - open (13: Permission denied)", "E: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), are you root?"], "stdout": "", "stdout_lines": []}
```

```sh
ansible-playbook -i inventory playbooks/install_nginx.yaml -b
```

The option `-b` / `--become` allows to run the tasks as another user (e.g root). This option can be specified task by task; the playbook is now:

```text
---
- hosts: webservers
  tasks:
    - name: ensure nginx is at the latest version
      apt: name=nginx state=latest
      become: yes
    - name: start nginx
      service:
          name: nginx
          state: started
```

# References

- [all modules and plugins](https://docs.ansible.com/ansible/latest/collections/all_plugins.html)