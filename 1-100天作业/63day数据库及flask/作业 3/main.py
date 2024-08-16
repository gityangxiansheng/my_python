from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pymysql


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = r"sqlite:///C:\Users\杨年轻\Desktop\py\1-100天作业\63day数据库及flask\作业3\books-collection.db"
db = SQLAlchemy(app=app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False) 
    
    def serialize(self):  
        return {  
            'id': self.id,  
            'title': self.title,  
            'author': self.author,  
            'rating': self.rating  
        } 

with app.app_context():
    db.create_all()
 
all_books = Book.query.all() 
books_list = [Book.serialize() for book in all_books]  
print(books_list)

@app.route('/')
def home():
    return render_template("index.html",all_books=books_list)


@app.route("/add",methods = ["GET","POST"])
def add():
    if request.method == "POST":
        new_book = Book(title=request.form["name"], author=request.form["authot"], rating=request.form["rating"])
        db.session.add(new_book) 
        db.session.commit() 
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

