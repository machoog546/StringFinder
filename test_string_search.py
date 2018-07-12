#!/usr/bin/python3

import time, os

logo = """  _____ __       _                _______           __
  / ___// /______(_)___  ____ _   / ____(_)___  ____/ /__  _____
  \__ \/ __/ ___/ / __ \/ __ `/  / /_  / / __ \/ __  / _ \/ ___/
 ___/ / /_/ /  / / / / / /_/ /  / __/ / / / / / /_/ /  __/ /
/____/\__/_/  /_/_/ /_/\__, /  /_/   /_/_/ /_/\__,_/\___/_/
					  /____/                                    \n\n"""

def main():

	print("\033[32m " + logo + "\033[37m") #change text color to green then switch to white.

	location = os.getcwd()
	change = dif_dir()

	if change == "1":
		location = where_to()

	items = what_for()

	thinkOfTheKids = include_children(location)

	if thinkOfTheKids == "full": #this will search for the string(s) in all child directories
		full_search(items, location)

	if thinkOfTheKids == "parent":
		parent_only(items, location) #this will only search for string(s) in top level selected

	input("Task complete. Press enter to exit.") #Used to close program


def dif_dir():
	while True:
		lookElseware = input("Would you like to change directories? Please use 1 or 2: \n1) yes \n2) no\n\n")
		#Error with Atom-Python-Run? if you use a letter it doesn't contine with while loop. Just crashes? Works fine if ran from terminal.
		if lookElseware == "1" or lookElseware == "2":
			if lookElseware == "1":
				return "1"
			if lookElseware == "2":
				return "2"

		else:
			print("Please use 1 or 2\n\n")

def where_to():

	where = ""#define it ahead of time so no error when in loop

	while True:
		where = input("\nWhere to? (Enter full path, 'c' to cancel and continue with script, or 'exit' to continue with default)\n\t:")
		if where == "exit":
			os.exit() #kill the script
		if where == "cancel":
			return os.getcwd()

		if not (where.endswith("/") or where.endswith("\\")): #if the directory doesn't end with a slash, add one on next line. if not (false or false) would be a match -->if not (false)
			where += "/"

		if os.path.exists(where):
			return where

		else:
			tryAgain = input("Path not reachable.\n")

def what_for():
	while True:
		search_str = input("Search phrases. Seperate by a comma:\n\t")
		search_str = search_str.split(",")

		if len(search_str) < 1:
			print("Search string/list cannot be empty. Please try again\n\n")
		else:
			return search_str

	pass

def include_children(location):
	reply = "yes"
	while True:
		reply = input("-Include subfolders? Default is yes. (YES or no): ")

		if reply == "yes" or reply == "y" or reply == "":
			print("\nChecking subfolders")
			return "full"

		if reply == "no" or reply == "n":
			print("\nCurrently looking only at log files in folder path " + "\'" + location + "\'.\n\n") #check if this has extra slashes
			return "parent" #this will only search for string(s) in top level selected
		else:
			print("Bad choice. Please choose again.")

def full_search(search_str, location):
	foundInList = {}#as strings are found they will be added to this list with the path and the file name.
	total = 0

	for folders, subfolders, files in os.walk(location): #subfolders not needed. If removed get error. Research later.
		for name in files:
			fullPath = os.path.join(folders, name)
			#print(fullPath) #debug to get file path
			if os.path.isfile(fullPath):
					if fullPath.endswith(".log") or fullPath.endswith(".txt"):
						fileBeingChecked = {fullPath: []}
						""""Ths will be a temp dict that will have a key of the file name, and IF a phrase is found
							we append the prase to the list value. The log file of all the found strings will then have
							the name of the file, it's location, and what phrases found."""
						fo = open(fullPath, "r")            # Open file for reading only #move this
						try:                                # Due to encoding error, I'm making it skip a set encoding.
							fileContents = fo.read()            # Read the whole contents of file in one go.
							fo.close()          # Close the file
						except:
							#print("Decode error. Ignoring.\n")     *Use for debug only.
							pass

						total += 1

						for phrase in search_str:
							if phrase in fileContents:
								fileBeingChecked[fullPath].append(phrase)
								print("String \"" + phrase + "\" found in " + fullPath)

								foundInList.update(fileBeingChecked)

	print("\nFound list")#debug
	for item in foundInList:
		print("\t" + item)#debug?
	print()

	try:
		logFile = open("found.text", "w+") #failing since file doesn't exist. fix
		logFile.write("The following string(s) have been located.\n\n")
		for string in foundInList:
			logFile.write(string + "\n\t")
			for value in foundInList[string]:
				logFile.write(value)
		logFile.close()
	except:
		print("Log output failed.") #make log file down the road?
		pass

	print(str(total) + " file(s) checked.\nLog file, \'found.text\', created in " + os.getcwd())


def parent_only(search_str, location):
	foundInList = {} #as strings are found they will be added to this list with the path and the file name.
	total = 0

	contents = os.listdir(location)
	for item in contents:
		if os.path.isfile(item):
			if item.endswith(".log") or item.endswith(".txt"):
				fileBeingChecked = {item: []}
				""""Ths will be a temp dict that will have a key of the file name, and IF a phrase is found
					we append the prase to the list value. The log file of all the found strings will then have
					the name of the file, it's location, and what phrases found."""
				fo = open(item, "r")            # Open file for reading only
				try:                                # Due to encoding error, I'm making it skip a set encoding.
					fileContents = fo.read()            # Read the whole contents of file in one go.
					fo.close()          # Close the file
				except:
					#print("Decode error. Ignoring.\n")     *Use for debug only.
					pass

				"""fileBeingChecked = {item: []}
				""Ths will be a temp dict that will have a key of the file name, and IF a phrase is found
					we append the prase to the list value. The log file of all the found strings will then have
					the name of the file, it's location, and what phrases found."""

				total += 1

				for phrase in search_str:
					if phrase in fileContents:
						fileBeingChecked[item].append(phrase)
						print("String \"" + phrase + "\" found in " + item)

						foundInList.update(fileBeingChecked)

	print("\nFound list")#debug
	for item in foundInList:
		print("\t" + item)#debug?
	print()

	try:
		logFile = open("found.text", "w+") #failing since file doesn't exist. fix
		logFile.write("The following string(s) have been located.\n\n")
		for string in foundInList:
			logFile.write(string + "\n\t")
			for value in foundInList[string]:
				logFile.write(value)
		logFile.close()
	except:
		print("Log output failed.") #make log file down the road?
		pass

	print(str(total) + " file(s) checked.\nLog file, \'found.text\', created in " + os.getcwd())




main()
