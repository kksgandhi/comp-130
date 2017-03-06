#! /bin/bash
if ping  8.8.8.8 -c3
then
echo mask2314 | sudo -S apt-get update -y | lolcat 
sudo -S apt-get upgrade -y | lolcat 
sudo -S apt-get dist-upgrade -y | lolcat 
sudo -S apt-get autoremove -y | lolcat 
sudo aptitude autoclean -y
sudo apt install espeak
else
sleep 30
./update
fi
