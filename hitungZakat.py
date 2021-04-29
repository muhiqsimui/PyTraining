class zakat:
  def __init__(self,nama,val1,val2):
    self.nama=nama
    self.val1=val1 #gaji perbulan
    self.val2=val2 #tunjangan perbulan
    penghasilan=val1+val2
    print("Jika Penghasilannya "+nama)
    conv(penghasilan)
    total=(val1+val2)*0.025
    print("maka zakatnya "+nama+" : ")
    conv(total)
    print("")
  def conv(nilai):
    nilai="Rp."+f'{nilai:,}'
    print(nilai)


#NAMA PEZAKAT , GAJI PERBULAN, TUNJANGAN PERBULAN
c1=zakat("PAK A",8_000_000,1_000_000)
c2=zakat("PAK B",3_000_000,500_000)
c3=zakat("IBU A",6_000_000,1_000_000)
c4=zakat("IBU B",4_000_000,800_000)
