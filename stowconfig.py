import subprocess

install_stow = "apt-get install stow".split()

sudo = subprocess.Popen(["sudo", "-S"] + install_stow, stdout=subprocess.PIPE)

print(sudo.stdout.read())

stow_cmd = "stow -d stow -t ~ -v 3 git vim zsh tex tmux".split()

stow = subprocess.Popen(stow_cmd, stdout=subprocess.PIPE)

print(stow.stdout.read())