import os
import time
print ("=======================|INSTALLING DRIVERS|===========================")
print ()

def step1():
  return(
    print ("========================STEP-1=========================") ,
    os.system("cd && sudo apt install bc && sudo rmmod r8188eu.ko && git clone https://github.com/aircrack-ng/rtl8188eus && cd rtl8188eus && sudo -i "),
    os.system('echo "blacklist r8188eu.ko" > "/etc/modprobe.d/realtek.conf" '),
    print ("======================================================="),
    print ("NOW REBOOT YOUR SYSTEM AND RE-RUN THE SCRIPT FOR STEP 2"),
    time.sleep(2))

def step2 ():
  return(
    print ("==============================STEP-2================================") ,
    os.system("cd && cd rtl8188eus && sudo make && sudo make install && sudo modprobe 8188eu"),
    print ("======================================================================"),
    print("NOW REBOOT YOUR SYSTEM AND RE-RUN THE SCRIPT AND START MONITORING MODE"),
    time.sleep(2))
