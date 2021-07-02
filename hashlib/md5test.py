import hashlib

def enc(text):
  textutf=text.encode('utf8')
  hash=hashlib.md5(textutf)
  hexa=hash.hexdigest()
  print('Encode :',textutf)
  print('md5 try :',hash)
  print('complete hash:',hexa)
  dec(textutf)
  
def dec(text):
  textutf=text.decode('utf8')
  print('.....DECODE.....')
  print('decode utf8 :',textutf)

def enc2(text):
  print('===================')
  hash=hashlib.md5(text)
  hexa=hash.hexdigest()
  print(hash)
  print(hexa)

enc('halo')
enc2(b'halo')

def encx(text):
  textutf=text.encode('utf8')
  hash=hashlib.md5(textutf)
  hexa=hash.hexdigest()
  text=hexa
  return text

encx('halo')

def login(userlogin,username,pwlogin,password):
  if userlogin==username and pwlogin==password:
    print('ok')
  else:
    print('fail')

user='admin'
pw='admin'
username=encx(user)
password=encx(pw)
# ceritanya inputan user 
listpw=['admin','admin2','admin3','admin']
listus=['admin','admin2','admin','admin']

#=====login masal=====
i=0
for i in range(len(listpw)):
  userlogin=encx(listus[i])
  pwlogin=encx(listpw[i])
  i=i+1
  print(i)
  login(userlogin,username,pwlogin,password)
