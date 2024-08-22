from flask import Flask, jsonify, render_template, request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
# from random import choice
import random
'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\Administrator\Desktop\py\1-100天作业\66day\作业1\instance\cafes.db'
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dict_data = {}
        for column in self.__table__.columns:
            dict_data[column.name] = getattr(self,column.name)
        return dict_data
    
    

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return redirect('https://documenter.getpostman.com/view/37835189/2sAXjDduwB')

@app.route("/add",methods=["GET",'POST'])
def add():
    new_cafe = Cafe(
    name = str(request.form.get('name')),
    map_url = str(request.form.get('map_url')),
    img_url = str(request.form.get('img_url')),
    location = str(request.form.get('location')),
    seats = str(request.form.get('seats')),
    has_toilet = bool(request.form.get('has_toilet')),
    has_wifi = bool(request.form.get('has_wifi')),
    has_sockets = bool(request.form.get('has_sockets')),
    can_take_calls = bool(request.form.get('can_take_calls')),
    coffee_price = str(request.form.get('coffee_price'))
    )
    print(new_cafe)
    db.session.add(new_cafe)
    db.session.commit()
    return render_template("index.html")

@app.route("/random",methods=["GET"])
def randoms():
    # result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    # all_cafe_data = result.scalars().all()
    all_cafe_data = Cafe.query.all()
    cafes = random.choice(all_cafe_data)
    
    return jsonify(cafe = cafes.to_dict())
@app.route("/all",methods=["GET"])
def all_cafe():
    # result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    # all_cafes = result.scalar()
    all_cafes = Cafe.query.all()
    cafes_list = [ cafes.to_dict() for cafes in all_cafes ]
    return jsonify({"cafes":cafes_list})

@app.route("/search",methods=["GET"])
def search():
    loc=request.args.get('loc')
    all_cafes = db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalars().all()
    cafes_list = [ cafes.to_dict() for cafes in all_cafes ]
    if cafes_list:
        return jsonify({"cafes":cafes_list})
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}),404
    
@app.route("/update-price/<int:cafe_id>",methods=["PATCH"])
def pach(cafe_id):
    data = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    # data.price = request.args.get('nwe_price')
    # data = db.get_or_404(Cafe,cafe_id)
    if data:
        data.coffee_price = request.args.get('nwe_price')
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else: 
        return jsonify({"error":{"Not Found":"Sorry a cafe with that id was not found in the database."} })
    
    # print(request.args.get('nwe_price'))

    

# http://127.0.0.1:5000/search?loc=Peckham
# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
