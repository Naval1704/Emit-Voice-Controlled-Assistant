import os
import subprocess as sp

paths = {'notepad' : "C:\\Windows\\notepad.exe", 
         'vscode' : "C:\\Users\\ASUS\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk",
         'cmd' :"C:\\Users\\ASUS\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\cmd.exe",
         'taskManager' : "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\taskmgr.exe",
         'ControlPanel' : "C:\\Users\\ASUS\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel.lnk",
         'Crome' : "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
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
    os.startfile( paths['Crome'] )

def open_calculator():
    sp.run('start microsoft.windows.calculator:', shell=True)

def open_task_manager():
    os.startfile( paths['taskManager'] )

def open_control_panel():
    os.startfile( paths['ControlPanel'] )

def open_registry_editor():
    os.system('regedit')

def open_windows_update():
    os.system('ms-settings:windowsupdate')

def open_cmd_as_admin():
    os.system('runas /user:Administrator cmd')
