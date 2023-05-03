# Examples of Event-Driven Ansible
This repository stores examples of Event-Driven Ansible, taken from:
[https://www.ansible.com/products/ansible-training#event-driven-automation](https://www.ansible.com/products/ansible-training#event-driven-automation)

To try it out in a lab environment, simply follow the above link or run it in your own environment by cloning this repository.

## Try it out in your own environment
1. Clone this repository
```
git clone https://github.com/mglantz/event-driven-ansible-demo
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
cd event-driven-ansible-demo
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

## Try out demo EDA plugin
1. Clone this repository
```
git clone https://github.com/mglantz/event-driven-ansible-demo
```
2. Copy demo plugin to your module directory.
```
cp event-driven-ansible-demo/ansible/eda/plugins/demo.py ~/.ansible/collections/ansible_collections/ansible/eda/plugins/event_source/
```
3. Run demo rulebook
```
cd event-driven-ansible-demo
ansible-rulebook -i demo_inventory --rulebook demo-rulebook.yml
```
4. Try and edit the demo.py plugin or file-missing/file-exists.yml playbooks to do something smarter.

