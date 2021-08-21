# python function to exit or loop the whole code

import os
import time

def loop () :
  return(
    print(),
    print(),
    print("------------------Returning to main menue------------------------"),
    os.system("python3 go.py"))
    
def exit () :
  return(  
    print(),
    print(),
    print("---------------------Exiting the code------------------------"),   
    os.system("cd && ls"))
     
def home (rdir) :
  return(
    os.system("cd && cd " + rdir + " && ls "))   

def reboot():
  return(
    os.system("reboot"))
