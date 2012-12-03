# Author: BlackGuard26
# Date of development: 03-12-2012
# Python Start Menu
import sys
import string
import os

print("1. Google Chrome")
print("2. NotePad++")
print("3. Audacity")
print("4. FileZilla")
print("5. iTunes")
print("6. PuTTY")
print("7. Skype")
print("8. WinSCP")
print("\n")
execute = raw_input("Which program do you want to use: ")
if execute == '1':
	os.chdir('C:\Program Files\Google\Chrome\Application')
	os.system('"C:\Program Files\Google\Chrome\Application\chrome.exe"')
	sys.exit()
elif execute == '2':
	os.chdir('C:\\Program Files\\Notepad++')
	os.system('"C:\\Program Files\\Notepad++\\notepad++.exe"')
	sys.exit()
elif execute == '3':
	os.chdir('C:\\Program Files\\Audacity')
	os.system('"C:\\Program Files\\Audacity\\audacity.exe"')
	sys.exit()
elif execute == '4':
	os.chdir('C:\\Program Files\\FileZilla FTP Client')
	os.system('"C:\\Program Files\\FileZilla FTP Client\\filezilla.exe"')
	sys.exit()
elif execute == '5':
	os.chdir('C:\\Program Files\\iTunes')
	os.system('"C:\\Program Files\\iTunes\\iTunes.exe"')
	sys.exit()
elif execute == '6':
	os.chdir('C:\\Program Files\\PuTTY')
	os.system('"C:\\Program Files\\PuTTY\\putty.exe"')
	sys.exit()
elif execute == '7':
	os.chdir('C:\\Program Files\\Skype\\Phone')
	os.system('"C:\\Program Files\\Skype\\Phone\Skype.exe"')
	sys.exit()
elif execute == '8':
	os.chdir('C:\\Program Files\\WinSCP')
	os.system('"C:\\Program Files\\WinSCP\\WinSCP.exe"')
	sys.exit()