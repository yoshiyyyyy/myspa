from flask import Flask, render_template,request,redirect,flash,send_from_directory
from werkzeug.utils import secure_filename
import requests
import os
import sys
sys.path.append("myspa/backend")
import BuildLane

UPLOAD_FOLDER = '/Users/yoshimasa/projects/myspa/backend/uploads/'

app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
app.config["SECRET_KEY"] = "sample"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/", methods=["GET","POST"])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            flash('ファイルがありません', "failed")
            return redirect(request.url)
        else:
            excel_row = request.form.get('excel_row') 
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            BuildLane.func(filename,int(excel_row))
            return send_from_directory("uploads", filename, as_attachment=True), os.remove('uploads/%s' % filename)
    
          

if __name__ == '__main__':
    app.run(debug=True)