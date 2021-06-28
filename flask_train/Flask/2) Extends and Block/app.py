from flask import Flask, render_template
import requests as r
app = Flask(__name__)

url = r.get('https://data.covid19.go.id/public/api/update.json')
dcov = url.json()


@app.route('/')
def index():
    return render_template('index.html', data=dcov)


@app.route('/api')
def covid():
    return f"{dcov['update']['penambahan']}"


# @app.route('/cov/<pilih>')
# def covid(pilih):
#     return f"{dcov['data'][pilih]}"


if __name__ == "__main__":
    app.run(debug=True)
