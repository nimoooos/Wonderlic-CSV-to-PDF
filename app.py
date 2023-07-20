from flask import Flask, render_template
from flask import request  # handle file upload
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)
