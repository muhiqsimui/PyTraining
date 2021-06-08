Array = [3,33,23,41,56,22,44,500]


# CARA PANJANG
def sorting(Array):
  for i in range(len(Array)):
    min_array=i
    # print(i)
    for j in range(i+1,len(Array)):
      if (Array[min_array]>Array[j]):
        min_array=j
      Array[i],Array[min_array] = Array[min_array],Array[i]

  print("Urutkan array panjang")
  for i in range(len(Array)):
    print("%d"%Array[i])

# CARA PENDEK
def sorting_sys(Array):
  print("Urutkan Array mudah")
  Array.sort()
  for z in Array:
    print(z)

sorting_sys(Array)

sorting(Array)
