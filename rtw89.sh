# Automation script to install wifi drivers for Realtek 8852AE, an 802.11ax device.
# Use only of u have this wifi driver.
# All Credits goes to respective repo owners.

clear
sudo apt-get update
sudo apt-get install make gcc linux-headers-$(uname -r) build-essential git
git clone https://github.com/lwfinger/rtw89.git -b v5
cd rtw89
sudo make
sudo make install 
reboot

