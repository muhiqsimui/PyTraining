#CONTOH FISH BUZZ sederhana

# jika bisa dibagi 3 dan 5 maka fish BUZZ
# jika bisa dibagi 3 fish
# jika bisa dibagi 5 buzz

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
