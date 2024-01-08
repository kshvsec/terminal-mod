import os
import pyfiglet
from datetime import datetime

black = "\033[1;30m"
red = "\033[1;31m"    
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"    
purple = "\033[1;35m"    
cyan = "\033[1;36m"    
white = "\033[1;37m"    

print(f"{green}#{white} CONFIGURE - TERMINAL {green}#{white}")
print(f"{red}<3 # -- github.com/infamous-koala -- # <3{white}")
result = pyfiglet.figlet_format(input(f"{green}[+]{white} Welcome text: "))
symbol = input(f"{green}[+]{white} Command symbol: ")
timenow = datetime.now()

def help():
	print("""Add-on commands:""")

def refresh():
	os.system("clear")
	print(result)
	print(f"{yellow}[-]{white}Time: {timenow.hour}:{timenow.minute}")

def wifiprofile(name):
	os.system()

refresh()
while True:
	x = input(f"{symbol} ")
	if x == "clear":
		refresh()
	else:
		os.system(f"{x}")