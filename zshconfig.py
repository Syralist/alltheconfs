import subprocess
import os

# install zsh
print("zsh installieren")
install_req = "apt-get install -y zsh".split()
sudo = subprocess.Popen(["sudo", "-S"] + install_req, stdout=subprocess.PIPE)
print(sudo.stdout.read())

# change to zsh
print("zsh als Standard setzen")
chsh_req = "chsh -s /usr/bin/zsh thomas".split()
chsh = subprocess.Popen(["sudo", "-S"] + chsh_req, stdout=subprocess.PIPE)
print(sudo.stdout.read())
print("jetzt neu anmelden!")