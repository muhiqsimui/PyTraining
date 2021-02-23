import pyautogui as piu
import time


####
pesan=['I','Love','You']
n=10

print('Ready')

waktu=5
while (waktu !=0):
	time.sleep(1)
	waktu-=1

for i in range(1,int(n)):
	time.sleep(1)
	for b in range (3):
		piu.typewrite(pesan[b]+'\n')

		
		
