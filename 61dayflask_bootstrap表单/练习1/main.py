from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ContactForm(FlaskForm):
    email = StringField("Email", render_kw={"size": "30"})

app = Flask(__name__)


@app.route("/")
def home():
    froms = ContactForm()
    return render_template('index.html',froms=froms)

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)
