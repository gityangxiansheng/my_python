from flask import Flask,render_template
import requests

datas = requests.get('https://api.npoint.io/25e2c6da3e3adccb1672').json()
# print(datas)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',datas=datas)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<id>')
def post(id):
    bolk=[]
    for data in datas:
        if data['id'] == int(id):
            bolk.append(data)
    return render_template('post.html',bolk=bolk)


if __name__ == "__main__":
    app.run(debug=True)
    
    
