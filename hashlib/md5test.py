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
