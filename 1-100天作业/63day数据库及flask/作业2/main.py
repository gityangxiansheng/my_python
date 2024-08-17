from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = r"sqlite:///C:\Users\Administrator\Desktop\BaiduSyncdisk\py\1-100天作业\63day数据库及flask\作业2\books-collection.db"  

db = SQLAlchemy() 
db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    

#读取内容
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    # print(type(all_books))
    # print(all_books[0][])
    # for book in all_books:
    #     print(f"书名： {book.title}, 作者： {book.author}, 评分： {book.rating}")
    # print(type(all_books))

# #读取内容
# with app.app_context():
#     all_books = Book.query.all()
#     print(type(all_books))
#     for book in all_books:
#         print(f"书名： {book.title}, 作者： {book.author}, 评分： {book.rating}")


# # 修改内容1 
# with app.app_context():  
#     # 假设我们要修改ID为1的书的评分  
#     book_to_update = Book.query.get(1)  # 获取ID为1的Book对象  
#     if book_to_update:  # 确保对象存在  
#         book_to_update.rating = 4.5  # 修改评分  
#         db.session.commit()  # 提交更改到数据库  




if __name__ == '__main__':
    app.run()
    
# # 新建工作表
# with app.app_context():
#     db.create_all()
# #新增内容
# with app.app_context():
#     new_book = Book(title="Harry Potter5", author="J. K. Rowling5", rating=9.4)
#     db.session.add(new_book)
#     db.session.commit()