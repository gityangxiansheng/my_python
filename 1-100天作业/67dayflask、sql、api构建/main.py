from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\Administrator\Desktop\py\1-100天作业\67dayflask、sql、api构建\instance\posts.db'
db = SQLAlchemy()
db.init_app(app)

class In_form(FlaskForm):
    title = StringField(name="文章标题")
    Subtitle = StringField(name="小标题")
    name = StringField(name="作者")
    image_url = StringField(name="图片链接")
    blog_Content = CKEditorField(name="编辑文字")
    submit = SubmitField(label='SUEMIT FOST')  
# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO:在数据库中查询所有帖子。将数据转换为 python 列表。
    posts = db.session.execute(db.select(BlogPost).order_by(BlogPost.id)).scalars().all()
    return render_template("index.html", all_posts=posts)

# TODO: 添加路线,以便您可以单击各个帖子。
@app.route('/show_post/<post_id>')
def show_post(post_id):
    # TODO:根据post_id从数据库中检索博客文章
    requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() 创建新的博客文章
@app.route("/add")
def add_new_post():
    form = In_form()
    return render_template('make-post.html',form=form)


# TODO: edit_post()修改现有的博客文章

# TODO: delete_post()从数据库中删除博客文章

# 以下是之前课程的代码,无需更改。
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
