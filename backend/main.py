from flask import Flask, render_template,request,redirect,flash
from werkzeug.utils import secure_filename
import requests
import os

UPLOAD_FOLDER = '/Users/yoshimasa/projects/myspa/backend/uploads/'

app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')
@app.route("/", methods=["GET","POST"])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            flash('ファイルがありません')
            return redirect(request.url)
        else:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)