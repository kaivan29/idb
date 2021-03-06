from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
# Create the Flask application.
app = Flask(__name__)

#app.debug = True

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about.html', methods=['GET'])
def about():
    return render_template('about.html', title="about")


@app.route('/games.html', methods=['GET'])
def games():
    return render_template('games.html', title="games")


@app.route('/reviews.html', methods=['GET'])
def reviews():
    return render_template('reviews.html', title="reviews")


@app.route('/platforms.html', methods=['GET'])
def platforms():
    return render_template('platforms.html', title='platforms')


@app.route('/studios.html', methods=['GET'])
def studios():
    return render_template('studios.html', title='studios')

# Run the Flask app.
if __name__ == '__main__':
    app.run()
