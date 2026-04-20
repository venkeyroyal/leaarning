sudo apt install -y wget apt-transport-https gpg

wget -qO - https://packages.adoptium.net/artifactory/api/gpg/key/public | gpg --dearmor | sudo tee /usr/share/keyrings/adoptium.gpg > /dev/null

echo "deb [signed-by=/usr/share/keyrings/adoptium.gpg] https://packages.adoptium.net/artifactory/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/adoptium.list

sudo apt update

sudo apt install temurin-21-jdk 

echo "deb [trusted=yes] https://pkg.jenkins.io/debian-stable binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list

sudo apt update

sudo apt install jenkins

systemctl status jenkins

sudo systemctl stop jenkins

update-alternatives --config editor

3

sudo mkdir -p /var/cache/Jenkins/tmp

sudo chown -R jenkins:jenkins /var/cache/Jenkins/tmp

systemctl show Jenkins

systemd-analyze verify jenkins.service

sudo systemctl start jenkins

journalctl -u jenkins



