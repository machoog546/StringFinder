import os, colorama
from colorama import Fore,Back,Style

colorama.init()
logo = """   _____ __       _                _______           __
  / ___// /______(_)___  ____ _   / ____(_)___  ____/ /__  _____
  \__ \/ __/ ___/ / __ \/ __ `/  / /_  / / __ \/ __  / _ \/ ___/
 ___/ / /_/ /  / / / / / /_/ /  / __/ / / / / / /_/ /  __/ /
/____/\__/_/  /_/_/ /_/\__, /  /_/   /_/_/ /_/\__,_/\___/_/
                      /____/                                    """
print(Fore.GREEN + logo + Style.RESET_ALL + "v.01\n")
print()

whereAmI = os.getcwd() #defaults to current location if none given

searchDir = input("-Directory to search? Leave blank for current:\n")
if searchDir != "":
    whereAmI = searchDir


reply = input("-Include sub dirs? (yes or NO): ")
if reply == "yes" or "y":
    #use os to get all folders in Directory
    print("\nNow looking at files in " + "\'" + whereAmI + "\' and it's child directories.\n\n")
elif reply == "no" or "n":
    print("\nCurrently looking only at log files in folder path " + "\'" + whereAmI + "\'.\n\n")
    pass

# Append a directory separator if not already present
if not (whereAmI.endswith("/") or whereAmI.endswith("\\")):
    whereAmI = whereAmI + "/"


print("Type in the phrase(s) you want to look for seperated by ' ^ '.\n\n")
search_str = input("Look for: ")
search_str = search_str.split(" ^ ")
print("\n\n")

if whereAmI == "./":
    answer = input("Path not found. (1)Exit or (2)Continue? - ")
    if answer == "1":
        quit()
    elif answer == "2":
        print("Continuing...\n\n")




"""
Just place any directories you want to exclude in the exclude list like exclude = [‘Archive’, ‘Old’] and it will skip over those folders in real time.
"""

for folder, subfolders, files in os.walk(whereAmI):
    for file in files:
        if file.endswith('.txt') or file.endswith('.text') or file.endswith('.log') or file.endswith('.out'):
            fo = open(whereAmI + files) # Open file for reading
            try:                            # Due to encoding error, I'm making it skip a set encoding.
                readFile = fo.read()            # Read the first line from the file
            except:
                #print("Decode error. Ignoring.\n")     *Use for debug only.
                pass
            for phrase in search_str:
                if phrase in readFile:
                    print(readFile + " seams to contain search phrase\n\n" + phrase + "\n\n" +"Please review.\n=====================================\n\n")
            fo.close()          # Close the


usedJustToExit = input('Press enter or return to exit.')

"""modified from file(s) found at:
http://www.opentechguides.com/how-to/article/python/59/files-containing-text.html
https://stackoverflow.com/questions/13779526/python-finding-substring-within-a-list
https://stackoverflow.com/questions/30444105/better-way-to-find-absolute-paths-during-os-walk
"""
