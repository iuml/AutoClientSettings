# I know the code is sloppy, but it works, cry me a river
import os 
import time
import requests
from pystyle import Colors, Center, Colorate
homedir = os.path.expanduser("~")
log_filename = homedir + "\\AppData\\Local\\Roblox\\Versions\\version-88cfc23f4e7d4e4b\\ClientSettings\\ClientAppSettings.json"

def Dashboard():
   print(Colorate.Horizontal(Colors.blue_to_cyan, (Center.XCenter("""
                    ╔╦╗╔═╗╦ ╦
                    ║║║║╣ ║║║
                    ╩ ╩╚═╝╚╩╝ 

        [LEGIT]                     [CHEATS]                                                         
  [1] FPS Unlocker             [4] Speed Hack
  [2] Optimization v1          [5] ESP (CTRL + F8 FOR MENU)
  [3] Optimization v2          [6] NoclipCamera                                                                                                                        
    """))))
   Choice = input(Colorate.Horizontal(Colors.cyan_to_blue, ("Choice? > ")))
   Main(Choice)
def Main(WriteType):
  if WriteType == "1":
      url = 'https://raw.githubusercontent.com/iuml/AutoClientSettings/main/Settings/FPS-Unlock'
      r = requests.get(url)
      content = r.text
      f = open(log_filename, "w")
      f.write(content)
      f.close()
      print("Installed!")
      time.sleep(3)
      os.system('cls')
      Dashboard()
  elif WriteType == "2": 
     url = 'https://raw.githubusercontent.com/iuml/AutoClientSettings/main/Settings/Optimizationv1'
     r = requests.get(url)
     content = r.text
     f = open(log_filename, "w")
     f.write(content)
     f.close()
     print("Installed!")
     time.sleep(3)
     os.system('cls')
     Dashboard()
  elif WriteType == "3": 
     url = 'https://raw.githubusercontent.com/iuml/AutoClientSettings/main/Settings/Optimizationv2'
     r = requests.get(url)
     content = r.text
     f = open(log_filename, "w")
     f.write(content)
     f.close()
     print("Installed!")
     time.sleep(3)
     os.system('cls')
     Dashboard()
  elif WriteType == "4": 
     url = 'https://raw.githubusercontent.com/iuml/AutoClientSettings/main/Settings/Speed-Hack'
     r = requests.get(url)
     content = r.text
     f = open(log_filename, "w")
     f.write(content)
     f.close()
     print("Installed!")
     time.sleep(3)
     os.system('cls')
     Dashboard()
  elif WriteType == "5": 
     url = 'https://raw.githubusercontent.com/iuml/AutoClientSettings/main/Settings/ESP'
     r = requests.get(url)
     content = r.text
     f = open(log_filename, "w")
     f.write(content)
     f.close()
     print("Installed!")
     time.sleep(3)
     os.system('cls')
     Dashboard()
  elif WriteType == "6": 
     url = 'https://raw.githubusercontent.com/iuml/AutoClientSettings/main/Settings/NoclipCamera'
     r = requests.get(url)
     content = r.text
     f = open(log_filename, "w")
     f.write(content)
     f.close()
     print("Installed!")
     time.sleep(3)
     os.system('cls')
     Dashboard()
  else:
     print('Invalid choice.')
     time.sleep(1)
     os.system('cls')
     Dashboard()
Dashboard()
