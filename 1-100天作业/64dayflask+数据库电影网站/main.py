from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField,SubmitField
from wtforms.validators import DataRequired
import requests
from get_title import get_title
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = r"sqlite:///C:\Users\Administrator\Desktop\py\1-100天作业\64dayflask+数据库电影网站\moive-collection.db"
Bootstrap5(app)
db = SQLAlchemy(app=app)

class EditForm(FlaskForm):
    rating = FloatField("您的评价应在10分以内，如7.5分！",validators=[DataRequired()])
    review = StringField("您的评论！",validators=[DataRequired()])
    submit = SubmitField('Done')
    
class AddForm(FlaskForm):
    title = StringField("请输入电影名称！",validators=[DataRequired()])
    submit = SubmitField('Done')

class Movie(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(250),unique=True,nullable=False)
    year = db.Column(db.String(8),nullable=False)
    description = db.Column(db.String(250))
    rating = db.Column(db.Float)
    ranking = db.Column(db.String(250),unique=True)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(250))
    
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    all_movies = Movie.query.all()    
    return render_template("index.html",movies=all_movies)

@app.route("/edit",methods=["GET",'POST'])
def edit():
    id = request.args.get("id")
    movie = db.get_or_404(Movie,id)
    form = EditForm()
    if request.method == "POST":
        rating = request.form.get('rating')
        review = request.form.get('review')
        movie = Movie.query.filter_by(id=id).first()
        movie.rating = rating
        movie.review = review
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html",movie=movie,form=form)

@app.route("/del",methods=["GET",'POST'])
def dell():
    id = request.args.get("id")
    del_move = Movie.query.filter_by(id=id).first()
    db.session.delete(del_move)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add",methods=["POST","GET"])
def add():
    form = AddForm()
    if request.method == "POST":
        title = request.form.get("title")
        datas = get_title(title)
        print(datas)
        return render_template("select.html",datas=datas)
    return render_template("add.html",form=form)

@app.route("/addscv",methods=["POST","GET"])
def addscv():
    data = request.args.get("data")
    return render_template("indexs.html",data = data)


if __name__ == '__main__':
    app.run()