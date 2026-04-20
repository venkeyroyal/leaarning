#!/bin/bash

set -e

sudo apt install -y wget apt-transport-https gpg software-properties-common

wget -qO - https://packages.adoptium.net/artifactory/api/gpg/key/public | gpg --dearmor | sudo tee /usr/share/keyrings/adoptium.gpg > /dev/null

echo "deb [signed-by=/usr/share/keyrings/adoptium.gpg] https://packages.adoptium.net/artifactory/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/adoptium.list

sudo apt update

sudo apt install -y temurin-21-jdk

echo "deb [trusted=yes] https://pkg.jenkins.io/debian-stable binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list

sudo apt update

sudo apt install -y jenkins

systemctl status jenkins --no-pager || true

sudo systemctl stop jenkins

sudo update-alternatives --set editor /bin/nano

sudo mkdir -p /var/cache/Jenkins/tmp

sudo chown -R jenkins:jenkins /var/cache/Jenkins/tmp

systemctl show jenkins

systemd-analyze verify jenkins.service || true

sudo systemctl start jenkins

systemctl status jenkins --no-pager

journalctl -u jenkins --no-pager -n 20