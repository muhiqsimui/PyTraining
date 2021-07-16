# TULISAN nya digituin pokoknya gk tau istilah nya ngasal aja

def rev(txt):
  g=int(len(txt)/2)
  print(txt[g:]+txt[:g])
  # if len(txt)%2==0:
  #   print(txt[g:]+txt[:g])
  # else:
  #   print('eror pie iki')

tulisan='sabi lika taki jarbela honpyt engbar'
les =tulisan.split()
for i in range(len(les)):
  rev(les[i])

 

'''
YANG DI ATAS GK TAU ISTILAH NYA 
SEBENARNYA KALO MAU BALIK TULISAN ATAU REVERSE STRING GINI AJA
'''
contohtext='tamvan'
print(contohtext[::-1])
