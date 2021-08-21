import os
import time
import vars
import code
import handshake

print("#-----------------------------------------------------------------------------------------#")
print("#-----------------------------------------------------------------------------------------#")
print("#-----------------------------------------------------------------------------------------#")
print("#-----------------------------------------------------------------------------------------#")
print("#------------------==================================================---------------------#")
print("#------------------|           SCRIPT BY MST PRODUCTIONS            |---------------------#")
print("#------------------==================================================---------------------#")
print("#-----------------------------------------------------------------------------------------#")
print("#-----------------------------------------------------------------------------------------#")
print("#-----------------------------------------------------------------------------------------#")
print("#----------------------------------------------------------------------BY: Paras Dhiman --#")
print()
time.sleep(1)

print ("------------------------------------------------")
print ("            Choose your Choice                  ")
print ("------------------------------------------------")
print ("00: Reboot System ")
print ("01: Start Monitor Mode")
print ("02: Stop Monitor Mode ")
print ("03: Grab Wifi Handshake ")
print ("04: Install Drivers for 'TL-WN722N' module ")
print ("05: Install Commonly used tools")
print ("99: Exit the Script")

print("=================================================")
inp = int(input("Enter your choice :"))
print("=================================================")
print()
os.system("clear")
time.sleep(1)

# Exit
if inp == 0 :
  print("-----------------------------------------------")
  code.exit()

# Start Monitor mode
if inp == 1:
  print("-----------------------------------------------")
  start_time = time.time()
  os.system("sudo rmmod r8188eu.ko && sudo modprobe 8188eu")
  print("-----------------------------------------------")
  print("now reconnect your external wifi adapter ")
  print("-----------------------------------------------")
  a = input("type 'y' to confirm: ")
  if a == 'y' or a == "Y":
    print()  
    print ("==================================================================")
    os.system("sudo ifconfig "+vars.intf+" down")
    os.system("sudo airmon-ng check kill")
    os.system("sudo airmon-ng start "+vars.intf)
    os.system("sudo ifconfig "+vars.intf+" up")
    print ("==================================================================")
    os.system ("iwconfig")
    print("---------------------- %s seconds --------------------------" % (time.time() - start_time))
    print ("done")
    time.sleep(3)
    code.loop()
  else :
    print("---------------------WRONG INPUT------------------------------")
    code.loop() 

# Exiting Monitor mode
elif inp == 2:
  start_time = time.time()
  print("==================STARTING====================")
  print()
  os.system("sudo ifconfig "+vars.intf+" down")
  os.system("sudo iwconfig "+vars.intf+" mode managed")
  os.system("sudo ifconfig "+vars.intf+" up")
  os.system("sudo NetworkManager restart")
  print("---------- %s seconds ---------" % (time.time() - start_time))
  print("=================DONE=========================")
  print()
  print("Now re plug-in the Rxternal adapter")
  print("==============================================")
  code.loop()

# Grabbing Wifi HandShake
elif inp == 3:
  start_time = time.time()
  handshake.grab1()
  print ("==================================================")
  chno = input("enter channel number:")
  w = input("enter capture name :")
  bssid = input("enter BSSID:")
  print ("==================================================")
  print()
  print ("------------------------------------------------")
  print ("            Choose your Choice                  ")
  print ("------------------------------------------------")
  print ("1: For Step-1(finding network and APs ")
  print ("2: For Step-2(De-Authing the clients ")
  print ("==================================================")
  inpt = int(input("Enter your choice :"))
  print ("==================================================")
  if inpt == 1:
    handshake.grab2(chno,bssid,w)
  elif inpt == 2:
    handshake.aireplay(bssid)
  print("-------------------------- %s seconds -----------------------------" % (time.time() - start_time))
  code.loop()

# Installing Drivers
elif inp == 4:
  print ("------------------------------------------------")
  print ("            Choose your Choice                  ")
  print ("------------------------------------------------")
  print ("1: For Step-1 ")
  print ("2: For Step-2 ")
  print ("==================================================")
  inp = int(input("Enter your choice :"))
  print ("==================================================")
  if inp == 1:
    start_time = time.time()
    install_driv.step1()
    print("-------------------------- %s seconds -----------------------------" % (time.time() - start_time))
    code.loop()
  elif inp == 2:
    start_time = time.time()
    install_driv.step2()
    print("-------------------------- %s seconds -----------------------------" % (time.time() - start_time))
    code.loop()
  else :
    code.loop()

# Installing Tools
elif inp == 5:
  start_time = time.time()
  os.system("install_tool.sh")
  print("-------------------------- %s seconds -----------------------------" % (time.time() - start_time))
  code.loop()

# Exit
elif inp == 99:
  code.exit()

else :
  print("---------------WRONG INPUT------------------")
  code.loop()  
