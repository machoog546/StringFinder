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

searchDir = input("-Directory to search? Leave blank for current.\nCurrent is: " + whereAmI + "\n\nSearch Directory:")
if searchDir != "":
    whereAmI = searchDir

if whereAmI == "./":
    answer = input("\nPath not found. (1)Exit or (2)Continue? - ")
    if answer == "1":
        quit()
    elif answer == "2":
        print("\nContinuing...\n\n")

if not (whereAmI.endswith("/") or whereAmI.endswith("\\")):
    whereAmI = whereAmI + "/"

print("\n-Type in the phrase(s) you want to look for seperated by ' ^ '.\n\n")
search_str = input("Look for: ")
search_str = search_str.split(" ^ ")
print("\n\n")

def FullSearch():
    total = 0
    for folder, subfolders, files in os.walk(whereAmI):
        for file in files:
            if file.endswith('.txt') or file.endswith('.text') or file.endswith('.log') or file.endswith('.out'):
                total +=1
                fo = open(os.path.join(folder, file), "r") # Open file for reading
                try:                            # Due to encoding error, I'm making it skip a set encoding.
                    readFile = fo.read()            # Read the first line from the file
                except:
                    #print("Decode error. Ignoring.\n")     *Use for debug only.
                    pass
                for phrase in search_str:
                    if phrase in readFile:
                        print("="*45 + "\n" + file + " contains search phrase\n\n \'" + phrase + "\'\n\n" +"Please review.\n" + "="*45 + "\n\n")
                fo.close()          # Close the
    print(str(total) + " file(s) checked.")
def ParentOnly():
    total = 0
    for file in os.listdir(whereAmI):
        print(file)
        if file.endswith('.txt') or file.endswith('.text') or file.endswith('.log') or file.endswith('.out'):
            total +=1
            fo = open(file, "r")
            try:                            # Due to encoding error, I'm making it skip a set encoding.
                readFile = fo.read()            # Read the first line from the file
            except:
                #print("Decode error. Ignoring.\n")     *Use for debug only.
                pass
            for phrase in search_str:
                if phrase in readFile:
                    print("="*45 + "\n" + file + " contains search phrase\n\n \'" + phrase + "\'\n\n" +"Please review.\n" + "="*45 + "\n\n")
            fo.close()
    print(str(total) + " file(s) checked.")

reply = input("-Include subfolders? Default is yes. (YES or no): ")
if reply == "yes" or reply == "y":
    print("yes")
    #use os to get all folders in Directory
    print("\nNow looking at files in " + "\'" + whereAmI + "\' and it's child directories.\n\n")
    FullSearch()

if reply == "no" or reply == "n":
    print("No")
    print("\nCurrently looking only at log files in folder path " + "\'" + whereAmI + "\'.\n\n")
    ParentOnly()

usedJustToExit = input('Press return to exit.')
