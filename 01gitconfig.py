import subprocess
import os

# generate ssh-key
print("SSH Key erzeugen")
ssh_cmd = 'ssh-keygen -t rsa -b 4096 -C "thomas.helmke@gmx.de"'.split()
ssh_gen = subprocess.Popen(ssh_cmd, stdout=subprocess.PIPE, shell=True)
print(ssh_gen.stdout.read())

# add ssh-key
print("SSH Key zum Agent hinzufügen")
ssh_cmd = 'ssh-add ~/.ssh/id_rsa'.split()
ssh_add = subprocess.Popen(ssh_cmd, stdout=subprocess.PIPE, shell=True)
print(ssh_add.stdout.read())

# copy ssh-key
print("SSH public key:")
with open(os.path.expanduser("~/.ssh/id_rsa.pub")) as f:
    print(f.read())
print("SSH Key auf dieser Seite einfügen: https://github.com/settings/ssh/new ")
wait = input("Enter drücken wenn es weitergehen kann.")

# install git
print("git installieren")
install_req = "apt-get install -y git".split()
sudo = subprocess.Popen(["sudo", "-S"] + install_req, stdout=subprocess.PIPE)
print(sudo.stdout.read())

# workspace erzeugen und Repository klonen
print("workspace erzeugen und alltheconfs klonen")
os.mkdir("workspace")
os.chdir("workspace")
git_cmd = 'git clone git@github.com:Syralist/alltheconfs.git'.split()
git = subprocess.Popen(git_cmd, stdout=subprocess.PIPE, shell=False)
print(git.stdout.read())
print("im Verzeichnis ~/workspace/alltheconfs gehts weiter")