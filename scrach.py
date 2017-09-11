for folder, subfolders, files in os.walk(whereAmI):
    for file in files:
        if files.endswith('.txt') or files.endswith('.text') or files.endswith('.log') or files.endswith('.out'):
            fo = open(whereAmI + files) # Open file for reading
            try:                            # Due to encoding error, I'm making it skip a set encoding.
                readFile = fo.read()            # Read the first line from the file
            except:
                #print("Decode error. Ignoring.\n")     *Use for debug only.
                pass
            for phrase in search_str:
                if phrase in readFile:
                    print(readFile + " seams to contain search phrase\n\n" + phrase + "\n\n" +"Please review.\n=====================================\n\n")
                    errors += 1
            fo.close()          # Close the







for folder, subfolders, files in os.walk(os.getcwd()):
    for file in files:
        filePath = os.path.abspath(file)
        print(filePath)


for files in os.listdir(whereAmI):
    if files.endswith('.txt') or files.endswith('.text') or files.endswith('.log') or files.endswith('.out'): # Apply file type filter
        fo = open(whereAmI + files) # Open file for reading
        try:                            # Due to encoding error, I'm making it skip a set encoding.
            readFile = fo.read()            # Read the first line from the file
        except:
            #print("Decode error. Ignoring.\n")     *Use for debug only.
            pass
        for phrase in search_str:
            if phrase in readFile:
                print(readFile + " seams to contain search phrase\n\n" + phrase + "\n\n" +"Please review.\n=====================================\n\n")
                errors += 1
        fo.close()          # Close the file
