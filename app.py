from flask import Flask, render_template, redirect, url_for, session, request, flash
from flask_sqlalchemy import SQLAlchemy
import hashlib
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = './static/images/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.secret_key = "kakwdk982ukiajkds"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
salt = "kfjwej2849"


#DB Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

#Database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    passhash = db.Column(db.String)
    name = db.Column(db.String)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cdn', methods=['GET', 'POST'])
def cdn():
    if request.method == 'POST':
        if request.form.get('email'):
            user = User.query.filter_by(email=request.form.get('email')).first()
            if user is not None:
                passhash = hashlib.md5(request.form.get('password').encode())
                if user.passhash == passhash.hexdigest():
                    session['logged_in'] = True
                    session['user_id'] = user.id
                    return redirect(url_for('cdnControlpanel'))
                else:
                    flash('Feil epost/passord.')
                    return render_template('cdn.html')
            else:
                flash('Feil epost/passord.')
                return render_template('cdn.html')
        else:
            flash('Feil epost/passord.')
            return render_template('cdn.html')
    elif request.method == 'GET':
        if session.get('logged_in'):
            return redirect(url_for('cdnControlpanel'))
        else:
            return render_template('cdn.html')

@app.route('/cdn-controlpanel', methods=['GET', 'POST'])
def cdnControlpanel():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filenamea
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(request.url)

    elif request.method == 'GET':
        if session.get('logged_in'):
            directory = r'./static/images/'
            urls = []
            for filename in os.listdir(directory):
                if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
                    urls.append(os.path.join(directory, filename))
                else:
                    continue
            return render_template('cdn.controlpanel.html', urls=urls)


@app.route('/logout')
def logout():
    session.pop('logged_in')
    session.pop('user_id')
    return redirect(url_for('index'))





