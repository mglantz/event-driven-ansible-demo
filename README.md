# Examples of Event-Driven Ansible
This repository stores examples of Event-Driven Ansible, taken from:
[https://www.ansible.com/products/ansible-training#event-driven-automation](https://www.ansible.com/products/ansible-training#event-driven-automation)

To try it out in a lab environment, simply follow the above link or run it in your own environment by cloning this repository.

## Try it out in your own environment
1. Clone this repository
```
git clone https://github.com/mglantz/even-driven-ansible
```
2. Install ansible-rulebook
```
pip3 install ansible-rulebook
dnf install java-17-openjdk
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
```
3. Create an inventory file to run against.
4. Run setup playbook
```
ansible-playbook -i inventory.yml setup-apache.yml
```
5. Run the website-automation example with:
```
ansible-rulebook --rules website-automation.yml -i inventory.yml --verbose
```
6. Disable apache and see rulebook stdout
```
ansible-playbook -i inventory.yml setup-apache.yml -e httpd_state=stopped
```

