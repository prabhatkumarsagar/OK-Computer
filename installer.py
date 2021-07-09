from pac import get_dirs
from pac import install_packages
import os
import subprocess
import shutil

home = get_dirs.HOME
print("""Kori Installer.

Please note that this Installer feature is still under-development and is very much prone to errors, 
so we'd recommend you run the program the traditional way i.e. by running the main.py file in the Kori 
Directory which you might've downloaded. 

So, Please quit this window all along, right this moment! 

But if you still want to continue anyway, Press Enter.""")
input()

while True:
    print("\nEnter the directory inside your home where you want to install Kori. (Note - Please add \"\\\" before the directory name.)")
    install_dir = home + input(">>> ")
    print(f"Install Kori in {install_dir}?[y/n]")
    confrm = input(">>> ")
    if os.path.isdir(install_dir):
        if 'y' in confrm.lower():
            break
    else:
        print("The given directory does not exist. Please try again.")

if os.name=="nt" and install_dir[-1] != "\\":
    install_dir += "\\"

if os.name=="posix" and install_dir[-1] != "/":
    install_dir += "/"


cur_dir = get_dirs.CUR_DIR

print("Installing python virtualenv.....", end = " ")
install_packages.install({"virtualenv": "pip3 install virtualenv"})
print("done!")

print(f"Creating virtualenv in {install_dir}.....", end = " ")
subprocess.check_output(f"virtualenv --system-site-packages -p python3 {install_dir}Kori", shell = True)
install_dir += "Kori/"
print("done!")

print(f"Copying required files to {install_dir}.....", end = " ")
files = ["main.py", "Modules Manual.txt", "Operations Outline.md", "LICENSE", "README.md"]
folder = "pac"
# shutil bug workaround from https://www.semicolonworld.com/question/53896/how-do-i-copy-an-entire-directory-of-files-into-an-existing-directory-using-python
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            if item == "pac":
                shutil.copytree(s, d, symlinks, ignore)

copytree(cur_dir, install_dir)

for i in range((len(files))):
    shutil.copy2(cur_dir + "/" + files[i], install_dir) 
print("Done!")

print(f"Kori has been installed successfully. In order to run Kori, run \n 'source bin/activate' inside {install_dir} and then run 'python main.py'.")