import os
from configparser import ConfigParser, NoSectionError
import pathlib

def getListofDirAndSubdir(root):
    lst = []
    for path, subdirs, files in os.walk(root):
        for name in files:
            if(str.endswith(name,".ini")):
                lst.append(pathlib.PurePath(path, name))
    return lst



rootFolder = os.getcwd()
#rootFolder = "C:\\Users\\STQ\\Documents\\Visual Studio Code\\Python\\Sperimental Ini\\test"

print("Working in: ", rootFolder,"\n")

print("Files found:")
fileList = getListofDirAndSubdir(rootFolder)
for file in fileList:
    fileList[fileList.index(file)] = str(file)
    print(file)


sezione = input("\n\nQuale è la sezione da cercare?: ")
if(sezione == ""):
    print("Parametro non può essere vuoto!\nUscita...")
    exit()

chiave = input("Quale è la chiave da cambiare?: ")
if(chiave == ""):
    print("Parametro non può essere vuoto!\nUscita...")
    exit()
    
valore = input(r"Quale è il nuovo valore?: ")
if(valore == ""):
    print("Parametro non può essere vuoto!\nUscita...")
    exit()


fileCambiati = []
fileNonCambiati = []

config = ConfigParser(strict=False, comment_prefixes="===", allow_no_value=True)

print("Lavorazione...")
for file in fileList:
    #reading original file
    originalFile = ""
    newFile = ""
    
    with open(file, 'r') as fileR:
        originalFile = fileR.read()
    
    config.read(file)
    try:
        config.set(sezione, chiave, valore)
    except NoSectionError:
        print("Sezione mancante: ",file)
    
    with open(file, 'w') as fileW:
        config.write(fileW)
    
    with open(file, 'r') as fileR:
        newFile = fileR.read()
        
    if(originalFile != newFile):
        fileCambiati.append(file)
    else:
        fileNonCambiati.append(file)
        


print("\n\nFile cambiati: ")
print(*fileCambiati, sep="\n")

print("\n\n\nFile non cambiati: ")
print(*fileNonCambiati, sep="\n")

input("\nFinito!\nPremere invio per uscire...")