from pac import get_dirs
from pac import install_packages
#from pac import file_operations

import os
import subprocess

home = get_dirs.HOME
print("Kori Installer.")

while True:
    print("\nEnter the directory inside your home where you want to install Kori.")
    install_dir = home + input(">>>")
    print(f"Install Kori in {install_dir}?[y/n]")
    confrm = input(">>>")
    if os.path.isdir(install_dir):
        if 'y' in confrm.lower():
            break
    else:
        print("The given directory does not exist. Please try again.")

if not install_dir[-1] == "/":
    install_dir += "/"

print("Installing python virtualenv.....", end = " ")
install_packages.install({"virtualenv": "pip3 install virtualenv"})
print("done!")

print(f"Creating virtualenv in {install_dir}.....", end = " ")
subprocess.check_output(f"virtualenv -p python3 {install_dir}Kori", shell = True)
print("done!")

