from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from flask_wtf.form import _Auto
from wtforms import StringField, SubmitField,SelectField
from wtforms.validators import DataRequired,URL,AnyOf
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafeme = StringField(label='Cafe name', validators=[DataRequired(message="请输入正确的内容！")])
    
    location = StringField(label='Location', validators=[DataRequired(message="请输入正确的内容！"),URL(message="请输入正确的URL！")])
    
    cafe_open = StringField(label='Open', validators=[DataRequired(message="请输入正确的内容！")])
    
    cafe_closs = StringField(label='Close', validators=[DataRequired(message="请输入正确的内容！")])
    
    choic_wifi = [("",""),("❌️","❌️"),("📶","📶"),("📶📶","📶📶"),("📶📶📶","📶📶📶"),("📶📶📶📶","📶📶📶📶"),("📶📶📶📶📶","📶📶📶📶📶")]
    wifi =SelectField(label='Wifi', validators=[DataRequired(message="请输入正确的内容！")],choices=choic_wifi)
    
    choic_coffee = [("",""),("❌️","❌️"),("☕","☕"),("☕☕","☕☕"),("☕☕☕","☕☕☕"),("☕☕☕☕","☕☕☕☕"),("☕☕☕☕☕","☕☕☕☕☕")]
    coffee = SelectField(label='Coffee', validators=[DataRequired(message="请输入正确的内容！")],choices=choic_coffee)
    choic_power = [("",""),("❌️","❌️"),("🔌","🔌"),("🔌🔌","🔌🔌"),("🔌🔌🔌","🔌🔌🔌"),("🔌🔌🔌🔌","🔌🔌🔌🔌"),("🔌🔌🔌🔌🔌","🔌🔌🔌🔌🔌")]
    power = SelectField(label='Power', validators=[DataRequired(message="请输入正确的内容！")],choices=choic_power)
    
    submit = SubmitField(label='Submit')    
    
    def __init__(self,*args, **kwargs):
        super(CafeForm, self).__init__(*args, **kwargs)
        self.csv_data = self.read_csv()
        
        
    def read_csv(self):
        csv_data = pd.read_csv(r'1-100天作业\62dayflask\作业\cafe-data.csv',header=None)
        list_of_rows = csv_data.values.tolist()
        return list_of_rows
    def write_csv(self,csv_list):
        csv_df = pd.DataFrame(csv_list)
        csv_df.to_csv(r'1-100天作业\62dayflask\作业\cafe-data.csv',index=False, header=None)
    def save_changes(self, csv_list):
        self.write_csv(csv_list)

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


@app.route('/add',methods=["GET","POST"])
def add_cafe():
    form = CafeForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        form_list = [form.cafeme.data,form.location.data,form.cafe_open.data,form.cafe_closs.data,form.coffee.data,form.wifi.data,form.power.data]
        print("新内容是",form_list,type(form_list))
        list_of_row = form.csv_data
        print("旧内容是",list_of_row,type(list_of_row))
        list_of_row.append(form_list)
        print("合并内容",list_of_row)
        form.save_changes(csv_list=list_of_row)
        return render_template('cafes.html', cafes=list_of_row)
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    form = CafeForm()
    list_of_rows = form.csv_data
    
    print("行",list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
