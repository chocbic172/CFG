import random																																					#Importing Random Module for Number Generation
print("Hello! Welcome to corrupted file generator!")
print("--------------------------------")
name = input("To start, name your file: \n") 																					#Asks for desired file name
atta = input("Now give it a file extention (like mp4, docx, txt) \n")									#Asks for desired file format
size = int(input("How big do you want your file to be, (roughly) in KB? \n"))					#Asks for desired file size (not quite working yet!)
print("This file will save into the same folder as this program and will overwrite any previous files with this name.")
cont = input("Are you sure you want to continue (Y/N) \n").upper()
if cont == "N":
    exit()
print("Generating File...")
dire = name+"."+atta 																																	#Finds file directory
file = open(dire,"w") 																																#Opens file in write mode
file.write("CFG by Me \n")
if size < 1025: 																																			#If size is under 1 mb
    for i in range(round(size/8)*10000-250000): 																			#I tried experimenting... failed :)
        file.write(str(round(random.randint(0,9)))) 																	#Super unefficient random number generator
else:
    for i in range(round(512/8)*10000-250000): 																				#Don't even ask why the round() is still there
        file.write(str(round(random.randint(0,9))))
    file.close() 																																			#I coudn't find a quicker way. Closes file
    file = open(dire,"r") 																														#Opens it in read mode
    tot = file.read() 																																#Saves file to a variable
    file = open(dire,"w") 																														#Opens it in read mode
    for i in range(int(size/400)): 																										#Again I tried to tinker with numbers
        file.write(tot) 																															#Automated copy and paste :)
file.close()
print("Complete")
