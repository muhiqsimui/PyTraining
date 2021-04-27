#CONTOH FIZZ BUZZ sederhana

# jika nilai dapat dibagi 3 dan 5 maka tampilkan fizz BUZZ
# jika nilai dapat dibagi 3 maka tampilkan fizz
# jika nilai dapat dibagi 5 maka tampilkan buzz

def fb(nilai):
	if(nilai%3==0):
		if(nilai%5==0):
			print (str(nilai)+" is FIZZ_BUZZ")
		else:
			print(str(nilai)+" is FIZZ")
	elif(nilai%5==0):
		print(str(nilai)+" is BUZZ")
	else:
		print(nilai)

for i in range(1,100+1):
	fb(i)
