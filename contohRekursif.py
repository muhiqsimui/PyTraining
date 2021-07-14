#rekursif adalah fungsi yg memanggil dirinya sendiri ok sip
def cetak(x):
  print(x)
  if x>1:
    cetak(x-1)
  elif x<1:
    cetak(x+1)

cetak(5)
