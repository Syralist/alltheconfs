import subprocess
import os
import shutil
import getpass

# install zsh
print("zsh installieren")
install_req = "apt-get install -y zsh".split()
sudo = subprocess.Popen(["sudo", "-S"] + install_req, stdout=subprocess.PIPE)
print(sudo.stdout.read())

# change to zsh
print("zsh als Standard setzen")
chsh_req = f"chsh -s {shutil.which('zsh')} {getpass.getuser()}".split()
chsh = subprocess.Popen(["sudo", "-S"] + chsh_req, stdout=subprocess.PIPE)
print(sudo.stdout.read())
print("jetzt neu anmelden!")