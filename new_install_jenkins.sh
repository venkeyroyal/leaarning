#!/bin/bash

set -e

echo "🔹 Installing required packages..."
sudo apt install -y wget apt-transport-https gpg software-properties-common

echo "🔹 Adding Adoptium GPG key..."
wget -qO - https://packages.adoptium.net/artifactory/api/gpg/key/public | gpg --dearmor | sudo tee /usr/share/keyrings/adoptium.gpg > /dev/null

echo "🔹 Adding Adoptium repo..."
echo "deb [signed-by=/usr/share/keyrings/adoptium.gpg] https://packages.adoptium.net/artifactory/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/adoptium.list

echo "🔹 Updating packages..."
sudo apt update

echo "🔹 Installing Java (Temurin 21)..."
sudo apt install -y temurin-21-jdk

echo "🔹 Adding Jenkins repo..."
echo "deb [trusted=yes] https://pkg.jenkins.io/debian-stable binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list

echo "🔹 Updating packages again..."
sudo apt update

echo "🔹 Installing Jenkins..."
sudo apt install -y jenkins

echo "🔹 Checking Jenkins status..."
systemctl status jenkins --no-pager || true

echo "🔹 Stopping Jenkins..."
sudo systemctl stop jenkins

echo "🔹 Setting nano as default editor automatically..."
sudo update-alternatives --set editor /bin/nano

echo "🔹 Creating temp directory..."
sudo mkdir -p /var/cache/Jenkins/tmp

echo "🔹 Setting permissions..."
sudo chown -R jenkins:jenkins /var/cache/Jenkins/tmp

echo "🔹 Showing Jenkins service details..."
systemctl show jenkins

echo "🔹 Verifying service file..."
systemd-analyze verify jenkins.service || true

echo "🔹 Starting Jenkins..."
sudo systemctl start jenkins

echo "🔹 Final status..."
systemctl status jenkins --no-pager

echo "🔹 Showing logs..."
journalctl -u jenkins --no-pager -n 20

echo "✅ Jenkins setup completed successfully!"
