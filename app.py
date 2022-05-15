#r'C:\WINDOWS\system32\notepad.exe'

import subprocess
import time
import pyautogui

pp = subprocess.Popen('C:\\Users\\solmi\Downloads\\GK6X-v1.18-GUI\\GK6X-v1.18-GUI\\GK6X.exe')
time.sleep(1.5)
pyautogui.write('map\n')
time.sleep(1.5)
pp.terminate()
