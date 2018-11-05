# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 23:19:11 2018

@author: schout
"""

import time
import os
import glob
from xml.etree import ElementTree as et
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def disableBackupEntry(event):
    if maakBackup.get():
        backupFolderEntry.config(state='disabled')
    else:
        backupFolderEntry.config(state='normal')

def askFileDir():
    dir_ = filedialog.askdirectory(initialdir="C:/Users/schout/Desktop/Acceptatie/")
    sourceFolderVar.set(str(dir_))
    
def askTargetDir():
    dir_ = filedialog.askdirectory(initialdir="C:/Users/schout/Desktop/Productie/")
    targetFolderVar.set(str(dir_))
    
def backupTargetDir():
    dir_ = filedialog.askdirectory(initialdir="C:/Users/schout/Desktop/Productie/")
    backupFolderVar.set(str(dir_))
    
def execute():
    print('\n\n\n')
    print("SourceFolder=", sourceFolderVar.get())
    print("TargetFolder=", targetFolderVar.get())
    print("MaakBackup=", maakBackup.get())
    print("BackupFolder=", backupFolderVar.get())
    print("accStringVar=", accStringVar.get())
    print("prodStringVar=", prodStringVar.get())
    print("Optie=", radio1.get())
    
    optie = radio1.get()
    tF = targetFolderVar.get()
    
    # Maak een backup
    if maakBackup.get():
        makeBackup(sourceFolderVar.get(), backupFolderVar.get())
        removeOldBackup(backupFolderVar.get())
    
    if optie == "Alleen XML":
        backupXml(tF)
        print("Alleen XML!!!")
    else:
        print("Deze optie is nog niet ontwikkeld.")

    # Pak de XML en vervang de string
    siteXml = findReplace(sourceFolderVar.get())
    
    
def backupXml(targetZipFolder):
    dt = time.strftime('%Y%m%d - %H%M%S')
    prodXml = targetZipFolder + "/Site.xml"
    prodBackupXml = targetZipFolder + "/Site Backup - {}".format(dt) + ".xml"
    
    # Hernoem de productie XML
    try:
        #os.rename(prodXml, prodBackupXml)
        print("Backup gelukt: {}".format(prodBackupXml))
    except:
        print("Hernoemen mislukt..")


    for backup in glob.glob(targetZipFolder + "/Site Backup - *.xml"):
        print((time.time() - os.path.getmtime(backup)) / 86400)
        
        #check of backup 

    
def findReplace(sourceFolder):
    # Find site.xml file in folder
    siteXml = sourceFolder + "/Site.xml"
        
    try:
        tree = et.parse(siteXml)
        print(tree)
    except: 
        print("{} niet gevonden".format(siteXml))
    
    # Open (parse) the file
    ##tree = et.parse(sourceFile)
    
    # Replace string {} with .. 
    ##tree.find('idinfo/timeperd/timeinfo/rngdates/begdate').text = '1/1/2011'

    # R
    ##tree.write(datafile)
    
    return "hierkomteenxml"

''' Setup TKinter '''
root = Tk()

''' Main informatie '''
root.title("Geoweb Acc -> Prod")
#root.minsize(500,500)
root.wm_iconbitmap('favicon.ico')
root.resizable(width=False, height=False)

''' Bovenste tekst '''

Label(root, text="Titel app en uitleg hierzo").grid(row=0, sticky=N, padx=10, pady=10)    


''' Bron folder selector '''

Label(root, text="Bron folder").grid(row=1, sticky=W, padx=4)

sourceFolderVar = StringVar() 
sourceFolderVar.set("C:/Users/schout/Desktop/Acceptatie/Landelijk_gebied")

sourceFolderEntry = Entry(root, width=100, textvariable=sourceFolderVar)
sourceFolderEntry.grid(row=1, column=2, sticky=W, padx=4)

Button(root, text="...", command=askFileDir).grid(row=1, column=3,  padx=4)


''' Target folder selector '''

Label(root, text="Target folder").grid(row=2, sticky=W, padx=4)

targetFolderVar = StringVar() 
targetFolderVar.set("C:/Users/schout/Desktop/Productie/Landelijk_gebied")

targetFolderEntry = Entry(root, width=100, textvariable=targetFolderVar)
targetFolderEntry.grid(row=2, column=2, sticky=W, padx=4)

Button(root, text="...", command=askTargetDir).grid(row=2, column=3,  padx=4)

''' Acc string '''

Label(root, text="Acceptatie").grid(row=3, sticky=W, padx=4)

accStringVar = StringVar() 
accStringVar.set("geoweb.pzhacc.nl")

accStringEntry = Entry(root, width=100, textvariable=accStringVar)
accStringEntry.config(state='disabled')
accStringEntry.grid(row=3, column=2, sticky=W, padx=4)

''' Productie string '''

Label(root, text="Productie").grid(row=4, sticky=W, padx=4)

prodStringVar = StringVar() 
prodStringVar.set("geoservices.zuid-holland.nl")

prodStringEntry = Entry(root, width=100, textvariable=prodStringVar)
prodStringEntry.config(state='disabled')
prodStringEntry.grid(row=4, column=2, sticky=W, padx=4)

''' Backup Button '''

Label(root, text="Maak backup").grid(row=5, sticky=W, padx=4, pady=10)
maakBackup = BooleanVar()
maakBackup.set(False)

maakBackupCheckButton = Checkbutton(root, variable=maakBackup)
maakBackupCheckButton.bind("<Button-1>", disableBackupEntry)
maakBackupCheckButton.grid(row=5, column=1, sticky=W, padx=1, pady=4)

backupFolderVar = StringVar() 
backupFolderVar.set("/home/test/locatie")

backupFolderEntry = Entry(root, width=100, textvariable=backupFolderVar)
backupFolderEntry.config(state='disabled')
backupFolderEntry.grid(row=5, column=2, sticky=W, padx=4, pady=4)

Button(root, text="...", command=backupTargetDir).grid(row=5, column=3,  padx=4, pady=4)


''' Scope Button '''

Label(root, text="Overig").grid(row=6, column=0, sticky=W, padx=4, pady=4)

radio1 = StringVar()
Radiobutton(root, text="Alleen XML", value="Alleen XML", variable=radio1).grid(row=6, padx=1, column=2, sticky=W)
Radiobutton(root, text="Hele Folder", value="Hele Folder", variable=radio1).grid(row=7, padx=1, column=2, sticky=W)

''' Lets Go Button '''
Button(root, text="Uitvoeren", command=execute).grid(row=8, column=3,  padx=10, pady=10)    

''' Close TKinter zodra user dat besluit '''
root.mainloop()

