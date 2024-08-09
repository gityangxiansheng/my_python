from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login',methods=["POST"])
def login():
    password = request.form['密码']
    us = request.form['账号']
    return f"<h1>账号：{us}，密码：{password}</h1>"

if __name__ == ('__main__'):
    app.run(debug=True)
    
    

