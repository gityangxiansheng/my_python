from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = r"sqlite:///C:\Users\Administrator\Desktop\BaiduSyncdisk\py\1-100天作业\63day数据库及flask\作业 3\books-collection.db"
db = SQLAlchemy(app=app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False) 
 
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    all_books = Book.query.all()
    return render_template("index.html",all_books=all_books)\
        
@app.route("/del/<book_id>")
def delete(book_id):
    book = Book.query.filter_by(id=book_id).first()
    print(book.title)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("home"))
    # return  book_id
    # return redirect("home")

@app.route("/add",methods = ["GET","POST"])
def add():
    if request.method == "POST":
        if request.form["name"] and request.form["author"] and request.form["rating"]:
            new_book = Book(title=request.form["name"], author=request.form["author"], rating=request.form["rating"])
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/edit",methods=['GET', 'POST'])
def modify():
    if request.method =="POST":
        if request.form['rating']:
            print(request.form["id"])
            book = Book.query.filter_by(id=request.form["id"]).first()
            book.rating = request.form['rating']
            db.session.commit()
            return redirect(url_for("home"))
    book = Book.query.filter_by(id=request.args.get('book_id')).first()
    return render_template("modify.html",book=book)




if __name__ == "__main__":
    app.run(debug=True)

