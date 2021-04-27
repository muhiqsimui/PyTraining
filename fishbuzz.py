
def fb(nilai):
	if(nilai%3==0):
		if(nilai%5==0):
			print (str(nilai)+" is FISH_BUZZ")
		else:
			print(str(nilai)+" is FISH")
	elif(nilai%5==0):
		print(str(nilai)+" is BUZZ")
	else:
		print(nilai)

for i in range(1,100+1):
	fb(i)
