from flask import Flask
import sqlite3
from flask_sqlalchemy import SQLAlchemy

from flask import request



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'



db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    

with app.app_context():
    db.create_all()



@app.route('/')
def hello_world():
    return 'Messaggio di benvenuto"'

@app.route('/user')
def welcomeUser():
    return "welcome User"

@app.route('/contatti')
def shoeContact():
    return "questi sono dei contatti di prova"

@app.route('/add_user', methods=['POST'])
def add_user_post():
    username = request.form.get('username')
    email = request.form.get('email')

    if username and email:
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return 'Utente aggiunto con successo tramite POST!'
    else:
        return 'Errore: username ed email sono richiesti.'

@app.route('/add_user/<username>/<email>')
def add_user_get(username, email):
    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()
    return 'Utente aggiunto con successo tramite GET!'



















if __name__ == '__main__':
    app.run(debug=True)