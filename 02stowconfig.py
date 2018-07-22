import subprocess
import os

# install stow
print("stow installieren")
install_req = "apt-get install -y stow".split()
sudo = subprocess.Popen(["sudo", "-S"] + install_req, stdout=subprocess.PIPE)
print(sudo.stdout.read())

# invoke stow
print("stow ausführen")
path = os.path.join(os.getcwd(), "stow")
os.chdir(path)
stow_packages = "git vim zsh tex tmux".split()
for package in stow_packages:
    stow_cmd = f"stow -t {os.path.expanduser('~')} {package}".split()
    stow = subprocess.run(stow_cmd, stdout=subprocess.PIPE, shell=False)
    print(stow)
