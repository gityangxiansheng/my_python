from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    submit = SubmitField('Submit')

# 练习：
# 添加：位置网址、营业时间、关闭时间、咖啡评分、wifi评分、电源插座评分字段
# 将咖啡/wifi/电源设置为选择元素，可选择 0 到 5。
#e.g. 你可以使用表情符号 ☕️ /💪/✘/ 🔌
# 将除提交之外的所有字段设为必填项
# 使用验证器检查 URL 字段是否输入了 URL。
# ---------------------------------------------------------------------------

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add')
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open(r'1-100天作业\62dayflask\cafe-data.csv', newline='', encoding='utf-8') as csv_file:

        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
