import pyautogui as piu
import time

print("ready")
piu.alert('Mulai program')
time.sleep(3)



piu.hotkey('win','r')
time.sleep(0.5)
piu.typewrite("cmd")
time.sleep(0.5)
piu.hotkey('enter')
time.sleep(0.5)
piu.typewrite("ping 8.8.8.8 -t")
time.sleep(0.5)
piu.hotkey('enter')
time.sleep(0.5)
piu.alert('berhasil ping')
