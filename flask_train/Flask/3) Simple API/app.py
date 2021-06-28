# !pip install flask
from flask import Flask, render_template
# !pip install Flask-RESTful
from flask_restful import Api, Resource
# !pip install requests
import requests as r

app = Flask(__name__)

api = Api(app)


class BelajarAPI(Resource):
    def get(self):
        return {'data': {
            'name': 'my project',
            'owner': 'muhiq'
        }
        }


api.add_resource(BelajarAPI, '/api')


@app.route('/')
def index():
    return 'ok'


@app.route('/home')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
