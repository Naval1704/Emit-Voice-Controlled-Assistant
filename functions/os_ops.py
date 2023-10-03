import os
import subprocess as sp

paths = { 'notepad' : "C:\\Windows\\notepad.exe", 'vscode' : "C:\\Users\\ASUS\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code" }

def open_camera():
    sp.run( 'start microsoft.windows.camera:', shell=True )

def open_notepad():
    os.startfile( paths['notepad'] )

def open_vscode():
    os.startfile( paths['vscode'])

def open_cmd():
    os.system('start cmd')
