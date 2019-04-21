
# remove old docker
echo "alte Docker Versionen entfernen"
sudo apt-get remove docker docker-engine docker.io containerd runc

# install docker prerequisites
echo "benötigte pakete installieren"
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common

# get key
echo "gpg key installieren und repository hinzufügen"
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) nightly"

# install docker
echo "docker installieren"
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io

# add user to group
echo "user zur docker gruppe hinzufügen"
sudo usermod -aG docker your-user
