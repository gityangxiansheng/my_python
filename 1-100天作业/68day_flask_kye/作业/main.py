from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/young/py/1-100天作业/68day_flask_kye/作业/instance/users.db'
db = SQLAlchemy()
db.init_app(app)


# CREATE TABLE IN DB
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
 
 
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register',methods=['GET','POST'])
def register():
    print(request.method)
    name = request.form.get('name')
    if request.method == 'POST':
        new_user = User(
        name = name,
        email = request.form.get('email'),
        password = request.form.get('password'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('secrets',name=name ))
    return render_template("register.html")


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        data = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if  data :
            in_password = request.form.get('password')
            password = data.password
            if in_password == password:
                print('登陆成功')
            else:
                print(f'{in_password}密码错误')
        else:
            print(f'{email}账号不存在')
 
    
    
    return render_template("login.html")


@app.route('/secrets')
def secrets():
    name = request.args.get('name')
    return render_template("secrets.html", name=name) 


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
