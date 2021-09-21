import os
import time
import vars
import code
import handshake

print(code.VIOLET+"#-----------------------------------------------------------------------------------------#")
print("#-----------------------------------------------------------------------------------------#")
print("#-----------------------------------------------------------------------------------------#")
print("#-----------------------------------------------------------------------------------------#")
print(code.RED+"#------------------"+code.END+code.HIGHLIGHT+code.RED+"=================================================="+code.END+code.RED+"---------------------#")
print("#------------------"+code.END+code.HIGHLIGHT+code.RED+"| WELCOME TO COMPILING SCRIPT BY MST PRODUCTIONS |"+code.END+code.RED+"---------------------#")
print("#------------------"+code.END+code.HIGHLIGHT+code.RED+"=================================================="+code.END+code.RED+"---------------------#"+code.END)
print(code.VIOLET+"#-----------------------------------------------------------------------------------------#")
print("#-----------------------------------------------------------------------------------------#")
print("#-----------------------------------------------------------------------------------------#")
print("#----------------------------------------------------------------------"+code.END+code.HIGHLIGHT+code.RED+"BY: Paras Dhiman --#"+code.END)
print()
time.sleep(1)

print (code.RED+"------------------------------------------------")
print (code.VIOLET+"            Choose your Choice                  ")
print (code.RED+"------------------------------------------------")
print (code.GREEN+"00: Reboot System ")
print ("01: Start Monitor Mode")
print ("02: Stop Monitor Mode ")
print ("03: Grab Wifi Handshake ")
print ("04: Install Drivers for 'TL-WN722N' module ")
print ("05: Install Drivers for Realtek 8852AE module")
print ("06: Install Commonly used tools")
print ("99: Exit the Script"+code.END)

print (code.RED+"=================================================")
inp = int(input(code.CYAN+"Enter your choice :"))
print (code.RED+"=================================================")
print()
os.system("clear")
time.sleep(1)

# Exit
if inp == 0 :
  print(code.RED+"-----------------------------------------------")
  code.exit()

# Start Monitor mode
if inp == 1:
  print(code.YELLOW+"-----------------------------------------------"+code.END)
  start_time = time.time()
  os.system("sudo rmmod r8188eu.ko && sudo modprobe 8188eu")
  print(code.VIOLET+"-----------------------------------------------")
  print(code.YELLOW+"now reconnect your external wifi adapter ")
  print(code.VIOLET+"-----------------------------------------------")
  a = input(code.GREEN+"type 'y' to confirm: "+code.END)
  if a == 'y' or a == "Y":
    print()  
    print (code.BLUE+"=================================================================="+code.END)
    os.system("sudo ifconfig "+vars.intf+" down")
    os.system("sudo airmon-ng check kill")
    os.system("sudo airmon-ng start "+vars.intf)
    os.system("sudo ifconfig "+vars.intf+" up")
    print (code.BLUE+"=================================================================="+code.END)
    os.system (code.CYAN+"iwconfig")
    print(code.GREEN+"---------------------- %s seconds --------------------------" % (time.time() - start_time))
    print ("done")
    time.sleep(3)
    code.loop()
  else :
    print(code.RED+"---------------------WRONG INPUT------------------------------")
    code.loop() 

# Exiting Monitor mode
elif inp == 2:
  start_time = time.time()
  print(code.GREEN+"==================STARTING===================="+code.END)
  print()
  os.system("sudo ifconfig "+vars.intf+" down")
  os.system("sudo iwconfig "+vars.intf+" mode managed")
  os.system("sudo ifconfig "+vars.intf+" up")
  os.system("sudo NetworkManager restart")
  print(code.GREEN+"---------- %s seconds ---------" % (time.time() - start_time))
  print("=================DONE=========================")
  print()
  print(code.YELLOW+"Now re plug-in the Rxternal adapter")
  print(code.GREEN+"==============================================")
  code.loop()

# Grabbing Wifi HandShake
elif inp == 3:
  start_time = time.time()
  handshake.grab1()
  print (code.RED+"=================================================="+code.END+code.GREEN)
  chno = input("enter channel number:")
  w = input("enter capture name :")
  bssid = input("enter BSSID:")
  print (code.RED+"==================================================")
  print()
  print (code.VIOLET+"------------------------------------------------")
  print (code.YELLOW+"            Choose your Choice                  ")
  print (code.VIOLET+"------------------------------------------------")
  print (code.GREEN+"1: For Step-1(finding network and APs ")
  print ("2: For Step-2(De-Authing the clients "+code.END)
  print (code.YELLOW+"==================================================")
  inpt = int(input(code.CYAN+"Enter your choice :"))
  print (code.YELLOW+"==================================================")
  if inpt == 1:
    handshake.grab2(chno,bssid,w)
  elif inpt == 2:
    handshake.aireplay(bssid)
  print (code.GREEN+"-------------------------- %s seconds -----------------------------" % (time.time() - start_time))
  code.loop()

# Installing Drivers
elif inp == 4:
  print (code.RED+"------------------------------------------------")
  print (code.YELLOW+"            Choose your Choice                  ")
  print (code.RED+"------------------------------------------------")
  print (code.CYAN+"1: For Step-1 ")
  print ("2: For Step-2 ")
  print (code.RED+"==================================================")
  inp = int(input(code.CYAN+"Enter your choice :"))
  print (code.RED+"==================================================")
  if inp == 1:
    start_time = time.time()
    install_driv.step1()
    print(code.GREEN+"-------------------------- %s seconds -----------------------------" % (time.time() - start_time))
    code.loop()
  elif inp == 2:
    start_time = time.time()
    install_driv.step2()
    print(code.GREEN+"-------------------------- %s seconds -----------------------------" % (time.time() - start_time))
    code.loop()
  else :
    code.loop()

# Installing Realtek 8852AE, an 802.11ax drivers
elif inp == 6:
  print(code.YELLOW+"Installing Drivers........"+code.END+code.CYAN)
  os.system("./rtw89.sh")

# Installing Tools
elif inp == 6:
  start_time = time.time()
  os.system("install_tool.sh")
  print(code.GREEN+"-------------------------- %s seconds -----------------------------" % (time.time() - start_time))
  code.loop()

# Exit
elif inp == 99:
  code.exit()

else :
  print(code.RED+"---------------WRONG INPUT------------------"+code.END)
  code.loop()  
