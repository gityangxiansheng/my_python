from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
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

all_books = []


@app.route('/')
def home():
    return render_template("index.html",all_books=all_books)


@app.route("/add",methods = ["GET","POST"])
def add():
    if request.method == "POST":
        new_book = {
            "book_name" : request.form["name"],
            "authot" : request.form["author"],
            "rating" : request.form["rating"]
        }
        all_books.append(new_book)
        
        
        
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

