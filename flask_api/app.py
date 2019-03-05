from flask import Flask
import models
from resources.courses import courses_api
from resources.reviews import reviews_api

app = Flask(__name__)
app.register_blueprint(courses_api)
app.register_blueprint(reviews_api)

@app.route('/')
def hello():
    return 'hello man'


if __name__ == '__main__':
    models.initialize()
    app.run(debug=True)