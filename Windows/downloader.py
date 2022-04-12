import os
import time
import pyfiglet
import requests

banner = pyfiglet.figlet_format("Downloader Agent", "slant")

time.sleep(1)
os.system("clear")
print(banner)                                                   print("\n \n")                                                  
Url = input("Enter Download Url \n >  ")
File = input("\n Enter file name to save \n > ")
time.sleep(2)

r = requests.get(Url)

with open(File, 'wb') as f:
 f.write(r.content)
 f.close

os.system("clear")
print(banner)
print("\n \n")
print("Downloaded 1 File Sucessfully... \n File name :" + File + "\n Download Url :" + Url)
print("\n \n")
i = input("| Program Completed | Press any key to exit ! | \n \n ")
os.system("cls")
