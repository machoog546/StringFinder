import os

print(os.getcwd()) #prints current working Directory
os.chdir('path') #changes dir to whatever 'path' is set as

print(os.listdir()) #prints items in current directory

os.mkdir('c:\\folder') #makes on folder, one level deep
os.makedirs('c:\\folder\\to\\make') #makes top folder and every folder needed to the end if they are missing

os.rmdir('c:\\folder\\to\\make') #only removes end directory, not whole path (just make)
os.rmdirs('c:\\folder\\to\\make') #removes all dirs listed going to end path. (c:\\folder\\to\\make')

os.rename('name1.txt', 'name2.txt')

os.stat('demo.txt') #prints file info for file

print(os.stat('demo.txt')).size #prints size

os.walk() #tuple of 3 values - path, dirs in path, files in path

for dirpath, dirnames, files in os.walk(os.getcwd()):
    print('current path: ', dirpath)
    print('Directories: ', dirnames)
    print('files: ', files)
    print()

os.environ.get('HOME') #used to print home variable

file_path = os.environ.get('HOME') + 'text.txt' #slashes might be missing at the +

file_path = os.path.join(environ.get('HOME') + 'text.txt')

with open(file_path, "w") as F:
    f.wte #write?


os.path.basename('/tmp/test.txt') #grabs filename of any Path
os.path.dirname('/tmp/test.txt') #would print just /tmp
os.path.split('/tmp/test.txt') #splits dir and base into a comma seperated values

os.path.exists('/tmp/test.txt') #cheks if exists

os.path.isdir('/tmp/test.txt') #True of False
os.path.isfile('/tmp/test.txt') #True of False
