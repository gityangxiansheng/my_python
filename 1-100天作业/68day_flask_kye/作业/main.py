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
# 创建并初始化 LoginManager 实例  
login_manager = LoginManager()  
login_manager.init_app(app)  

# CREATE TABLE IN DB
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
 
 
with app.app_context():
    db.create_all()


#创建回调
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

#主页
@app.route('/')
def home():
    return render_template("index.html")

#注册页面
@app.route('/register',methods=['GET','POST'])
def register():
    print(request.method)
    name = request.form.get('name')
    if request.method == 'POST':
        new_user = User(
        name = name,
        email = request.form.get('email'),
        password = generate_password_hash(request.form.get('password'),method="pbkdf2:sha256",salt_length=8))
        
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('secrets',name=name ))
    return render_template("register.html")

#登陆
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        data = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if  data :
            in_password = request.form.get('password')
            password = data.password
            is_correct = check_password_hash(password, in_password)  
            if is_correct:
                print('登陆成功')
                name = data.name
                return redirect(url_for('secrets',name=name))
            else:
                print(f'{in_password}密码错误')
        else:
            print(f'{email}账号不存在')
 
    
    
    return render_template("login.html")

#欢迎
@app.route('/secrets')
def secrets():
    name = request.args.get('name')
    return render_template("secrets.html", name=name) 


@app.route('/logout')
def logout():
    pass

#下载页
@app.route('/download')
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
