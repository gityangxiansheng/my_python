from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import *
from email_validator import validate_email, EmailNotValidError

class ContactForm(FlaskForm):
    email = StringField(label='电子邮件', render_kw={"size": "30"},validators=[Email(message="请输入正确的邮箱！")])  # 定义电子邮件字段，显示标签为'Email'，设置输入框宽度为 30
    password = PasswordField(label='密码', render_kw={"size": "30"},validators=[Length(min=8, max=20,message="密码长度8-20位！")]) # 定义密码字段，显示标签为'Password'，设置输入框宽度为 30
    submit = SubmitField(label='按钮')  # 定义提交按钮，显示标签为'Login'

app = Flask(__name__)
app.config['SECRET_KEY'] ='my_secret_key'  # 设置秘密密钥，用于 CSRF 保护

@app.route("/",methods=["GET","POST"] )
def home():
    form = ContactForm()
    if form.validate_on_submit() and form.email.data == "@qq.com" and form.password.data == "12345678":
        return render_template("denied.html")
    elif form.validate_on_submit() :
        return render_template("denied.html")
    return render_template('index.html',form=form)

@app.route("/login",methods=["GET","POST"])
def login():
    return render_template("denied.html")

if __name__ == '__main__':
    app.run(debug=True)
