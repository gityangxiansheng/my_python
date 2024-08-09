from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    dicts  = requests.get('https://api.npoint.io/94e3ce2297d5624c4f90')
    xx = dicts.json()
    return render_template("index.html",cc=xx)

@app.route('/blog/<id>')
def blog(id):
    ids = int(id)
    dicts  = requests.get('https://api.npoint.io/94e3ce2297d5624c4f90')
    xx = dicts.json()
    return render_template("post.html",cc=xx,ids=ids)


if __name__ == "__main__":
    app.run(debug=True)
    

# dicts  = requests.get('https://api.npoint.io/94e3ce2297d5624c4f90')
# xx = dicts.json()
# for _ in xx :
#     print(_['title'])
#     print(_['subtitle'])