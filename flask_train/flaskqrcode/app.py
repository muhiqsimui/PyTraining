from flask import Flask, render_template, request
import requests as r
import pyqrcode
from pyqrcode import QRCode
import io

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/scan',methods=['GET','POST'])

def qrcode():
    gambar=None
    gambar = io.BytesIO()
    textqr=request.form['qrcode']
    link='/member/'+textqr
    url = pyqrcode.create(textqr)
    url.svg(gambar, scale = 8)
    kj=kejutan(textqr)
    
    gambar_content = gambar.getvalue().decode("utf-8") if gambar else None
    return render_template('scan.html',textqr=textqr,gambar_content=gambar_content,kj=kj,link=link)

peserta=['king','rose','joker','thejack','mrheart']
def kejutan(textqr):
    
    
    if textqr in peserta:
        nama=textqr
        result=f'''
        Welcome to the event 
        Mr {nama} i hope you enjoy this day,
        we always take care about VIP
        link 
        '''
    else:
        result=f'''Tidak terdaftar '''
    return result

@app.route('/member/<name>')
def scan_qr(name):
    return name

if __name__ == "__main__":
    app.run(debug=True)
