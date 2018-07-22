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

# install xsel
install_req = "apt-get install -y xsel".split()
sudo = subprocess.Popen(["sudo", "-S"] + install_req, stdout=subprocess.PIPE)
print(sudo.stdout.read())

# copy ssh-key
print("SSH Key kopieren")
cat_cmd = 'cat ~/.ssh./id_rsa.pub'.split()
cat = subprocess.Popen(cat_cmd, stdout=subprocess.PIPE, shell=True)
xsel_cmd = 'xsel -bi'.split()
xsel = subprocess.Popen(xsel_cmd, stdin=cat.stdout, stdout=subprocess.PIPE, shell=False)
print(xsel.stdout.read())
print("SSH Key ist in der Zwischenablage. Auf dieser Seite einfügen: https://github.com/settings/ssh/new ")
wait = input("Enter drücken wenn es weitergehen kann.")

# workspace erzeugen und Repository klonen
print("workspace erzeugen und alltheconfs klonen")
os.mkdir("workspace")
os.chdir("workspace")
git_cmd = 'git clone git@github.com:Syralist/alltheconfs.git'.split()
git = subprocess.Popen(git_cmd, stdout=subprocess.PIPE, shell=False)
print(git.stdout.read())
print("im Verzeichnis ~/workspace/alltheconfs gehts weiter")