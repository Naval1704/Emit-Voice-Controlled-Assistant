import os
import subprocess as sp

paths = {'notepad' : "C:\\Windows\\notepad.exe", 
         'vscode' : "C:\\Users\\ASUS\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk",
         'cmd' :"C:\\Users\\ASUS\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk",
         'taskManager' : "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Task Manager.lnk",
         'ControlPanel' : "C:\\Users\\ASUS\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel.lnk",
         'Chrome' : "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
         }

def open_camera():
    sp.run( 'start microsoft.windows.camera:', shell=True )

def open_notepad():
    os.startfile( paths['notepad'] )

def open_vscode():
    os.startfile( paths['vscode'] )

def open_cmd():
    os.startfile( paths['cmd'] )

def open_file_explorer():
    os.startfile( paths['Chrome'] )

def open_calculator():
    sp.run('start microsoft.windows.calculator:', shell=True)

def open_task_manager():
    os.startfile( paths['taskManager'] )

def open_control_panel():
    os.startfile( paths['ControlPanel'] )
