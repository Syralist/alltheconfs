import subprocess
import os

# install packages for coding
print("pakete installieren")
install_req = "apt-get install -y aptitude vim-nox build-essentials python3-pip code gimp inkscape".split()
sudo = subprocess.Popen(["sudo", "-S"] + install_req, stdout=subprocess.PIPE)
print(sudo.stdout.read())
