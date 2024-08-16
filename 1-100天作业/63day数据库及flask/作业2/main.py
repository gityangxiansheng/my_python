from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = r"sqlite:///C:\Users\杨年轻\Desktop\py\1-100天作业\63day数据库及flask\作业2\books-collection.db"  

db = SQLAlchemy() 
db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
#新建工作表
# with app.app_context():
#     db.create_all()

with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)