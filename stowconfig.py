import subprocess

# install requirements
install_req = "apt-get install -y stow python3-pip".split()
sudo = subprocess.Popen(["sudo", "-S"] + install_req, stdout=subprocess.PIPE)
print(sudo.stdout.read())

# install dploy
install_dploy = "pip3 install dploy".split()
sudo = subprocess.Popen(["sudo", "-S"] + install_dploy, stdout=subprocess.PIPE)
print(sudo.stdout.read())

# invoke dploy
stow_packages = "git vim zsh tex tmux".split()
for package in stow_packages:
    dploy_cmd = f"python3 -m dploy stow stow/{package} ~".split()
    stow = subprocess.Popen(dploy_cmd, stdout=subprocess.PIPE, shell=True)
    print(stow.stdout.read())
