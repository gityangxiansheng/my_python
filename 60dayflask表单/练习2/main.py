from flask import Flask, render_template,request
import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact",methods=['POST','GET'])
def contact():
    if request.method == 'POST':
        print(request.form)
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
         # 邮件内容
        subject = '有人联系！'
        body = f"""姓名：{name}\n
                    邮箱：{email}\n
                    电话：{phone}\n
                    消息：{message}
                """
        # 构建邮件
        msg = MIMEText(body, 'plain', 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = '@qq.com'
        msg['To'] = '@qq.com'
        
        # 发送邮件
        smtp_server = 'smtp.qq.com'
        smtp_port = 587
        sender_email = '@qq.com'
        password = ''
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, [msg['To']], msg.as_string())
            print('邮件发送成功')
        except smtplib.SMTPException as e:
            print('邮件发送失败:', str(e))
        return render_template("contact.html")
    else:
        return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

# 

 

  
        


if __name__ == "__main__":
    app.run(debug=True, port=5001)
