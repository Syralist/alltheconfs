import subprocess
import os

# install packages for coding
print("pakete installieren")
install_req = "apt-get install -y aptitude vim-nox build-essential python3-pip cmake code gimp inkscape kicad".split()
sudo = subprocess.Popen(["sudo", "-S"] + install_req, stdout=subprocess.PIPE)
print(sudo.stdout.read())

# install VS Code extensions
print("VS Code Extensions installieren")
install_req = "code --install-extension".split()
extensions = ["alexcvzz.vscode-sqlite",
        "DotJoshJohnson.xml",
        "efbenson.scad",
        "fallenwood.vimL",
        "James-Yu.latex-workshop",
        "MS-CEINTL.vscode-language-pack-de",
        "ms-python.python",
        "ms-vscode.cpptools",
        "PeterJausovec.vscode-docker",
        "PKief.material-icon-theme",
        "vsciot-vscode.vscode-arduino",
        "vscodevim.vim"]
for ext in extensions:
    sudo = subprocess.Popen(install_req + [ext], stdout=subprocess.PIPE)
    print(sudo.stdout.read())

# install vundle
print("vundle installieren")
install_req = f"git clone https://github.com/VundleVim/Vundle.vim.git {os.path.expanduser('~/.vim/bundle/Vundle.vim')}".split()
cmd = subprocess.Popen(install_req, stdout=subprocess.PIPE)
print(cmd.stdout.read())
print("vim aufrufen und vundle plugins installieren")
install_req = f"vim +PluginInstall +qall".split()
cmd = subprocess.Popen(install_req, stdout=subprocess.PIPE)
print(cmd.stdout.read())
print("youcompleteme compilieren")
os.chdir(os.path.expanduser("~/.vim/bundle/YouCompleteMe"))
install_req = f"python3 ./install.py --clang-completer".split()
cmd = subprocess.Popen(install_req, stdout=subprocess.PIPE)
print(cmd.stdout.read())
