class User:
  def __init__(self,name,tipe):
    self.name=name
    self.tipe=tipe

  def upgradeTipe(self,tipe):
    self.tipe=tipe

user1=User("Iqbal","Programmer")
user2=User("Dita Karang","Idol")
user3=User("Tzuyu","Singer")
user4=[User("Joy","RV member"),User("Irene","RV member"),User("Wendy","RV Member")]



def bias():
  for i in range(len(user4)):
    print(user4[i].name)

print(user1.name+" Have "+str(len(user4))+" bias then ")
bias()

user4[2].upgradeTipe("Girlfriend")
print(user1.name+" <3 "+user4[2].name+" Cause she is my "+user4[2].tipe)
