import subprocess
import os

# install requirements
install_req = "apt-get install -y stow python3-pip".split()
sudo = subprocess.Popen(["sudo", "-S"] + install_req, stdout=subprocess.PIPE)
print(sudo.stdout.read())

# invoke stow
path = os.path.join(os.getcwd(), "stow")
os.chdir(path)
stow_packages = "git vim zsh tex tmux".split()
for package in stow_packages:
    stow_cmd = f"stow -t /home/thomas {package}".split()
    stow = subprocess.run(stow_cmd, stdout=subprocess.PIPE, shell=False)
    print(stow)
