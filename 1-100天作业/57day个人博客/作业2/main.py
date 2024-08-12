from flask import Flask, render_template
from post import Post
import requests

data = requests.get('https://api.npoint.io/94e3ce2297d5624c4f90').json()
post_list = []
for _ in data:
    post = Post(_['id'],_['title'],_['subtitle'],_['content'])
    post_list.append(post)
    

app = Flask(__name__)

@app.route('/')
def home ():
    return render_template('index.html',post = post_list)

@app.route('/blog/<id>')
def blog(id):
    for post in post_list :
        if post.id == int(id) :
            title = post.title
            subtitle = post.subtitle
            content = post.content
    return render_template('post.html',title=title,subtitle=subtitle,content=content)

if __name__ == '__main__':
    app.run(debug=True)
