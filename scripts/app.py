from flask import Flask, render_template
from scripts.dashboard import app as dash_app

flask_app = Flask(__name__)

@flask_app.route('/')
def index():
    return render_template('index.html')

dash_app.init_app(flask_app)

if __name__ == '__main__':
    flask_app.run(debug=True)
