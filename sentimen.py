API_KEY= # isi api key
API_SECRET_KEY= #api secret
B_TOKEN=0 #gk dipake sekarang kosongin aja
ACCESS_TOKEN=#akses token
ACCESS_SECRET_TOKEN= #akses sekret token

auth = tweepy.OAuthHandler(API_KEY,API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)
api = tweepy.API(auth)

#analisis untuk menilai tweet berkaitan dengan tehyung jimin :3
cari2=api.search(q="tehyung jimin",lang="en", count=10)
for tweet in cari2:
  tp = {}
  tp['tanggal_tweet']=tweet.created_at
  tp['pengguna']=tweet.user.screen_name
  tp['Isi tweet']=tweet.text
  #tclean untuk bersihkan datanya dari simbol simbol tida berguna
  t_clean =' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet.text).split())
  analisis=TextBlob(t_clean)
  # print(analisis.sentiment.polarity)
  
  # Kalo lebih besar dari 0 maka tweet positif kalo persis 0 berarti netral, tapi kalo lebih kecil berarti tweet negatif
  if analisis.sentiment.polarity > 0.0:
    tp['sentimen'] = "positif"
  elif analisis.sentiment.polarity < 0.0:
    tp['sentimen'] = "negatif"
  else:
    tp['sentimen'] = "netral"
  print(tp)
  print(analisis.sentiment.polarity)
