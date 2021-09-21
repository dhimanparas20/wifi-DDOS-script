# python function to exit or loop the whole code
import os
import time

# some colors and presets to use 
VIOLET = '\033[95m'
BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
BROWN = '\033[93m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RED = '\033[91m'
END = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
HIGH = '\x1b[6;30;42m'
HIGHLIGHT = '\x1b[6;30;43m'

def loop () :
  return(
    print(),
    print(),
    print(GREEN+"------------------"+HIGHLIGHT+"Returning to main menue"+END+GREEN+"------------------------"+END),
    os.system("python3 go.py"))
    
def exit () :
  return(  
    print(),
    print(),
    print(BROWN+"---------------------"+HIGH+"Exiting the code"+END+BROWN+"------------------------"+END),   
    os.system("cd && ls"))
     
def home (rdir) :
  return(
    os.system("cd && cd " + rdir + " && ls "))   

def reboot():
  return(
    os.system("reboot"))
