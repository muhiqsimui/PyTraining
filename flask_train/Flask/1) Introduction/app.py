from logging import debug
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    bgs = ['https://wallpapercave.com/wp/wp4202157.jpg',
           'https://asset.kompas.com/crops/ALa0jTUL1pbd1JSMcAJzCWfAOgE=/0x0:780x520/750x500/data/photo/2019/05/02/3681177918.jpg',
           'https://p4.wallpaperbetter.com/wallpaper/46/884/35/bicycle-clouds-reflection-wallpaper-preview.jpg']
    return render_template('home.html', bgs=bgs)


@app.route('/about')
def about():
    posData = [{
        'judul': 'about',
        'isi': 'ini adalah isi about'
    },
        {
        'judul': 'profil',
        'isi': 'ini adalah isi profil'
    }
    ]
    return render_template('about.html', title=posData)


@app.route('/pages/<n>')
def pages(n):
    # return 'page '+n
    return f'pages will return {n}'


if __name__ == '__main__':
    app.run(debug=True)
