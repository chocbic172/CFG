import random
print("Hello! Welcome to corrupted file generator!")
print("--------------------------------")
name = input("To start, name your file: \n")
atta = input("Now give it a file extention (like mp4, docx, txt) \n")
size = int(input("How big do you want your file to be, (roughly) in KB? \n"))
print("This file will save into the same folder as this program and will overwrite any previous files with this name.")
cont = input("Are you sure you want to continue (Y/N) \n").upper()
if cont == "N":
    exit()
print("Generating File...")
dire = name+"."+atta
file = open(dire,"w")
file.write("CFG by Me \n")
if size < 1025:
    for i in range(round(size/8)*10000-250000):
        file.write(str(round(random.randint(0,9))))
else:
    for i in range(round(512/8)*10000-250000):
        file.write(str(round(random.randint(0,9))))
    file.close()
    file = open(dire,"r")
    tot = file.read()
    file = open(dire,"w")
    for i in range(int(size/400)):
        file.write(tot)
file.close()
print("Complete")
