import requests
import json
from flask import Flask,render_template

app = Flask(__name__)


# @app.route('/')
# def wed():
#     return render_template('网页.html')

@app.route('/')
def wed2():
    josns = requests.get(f'https://api.npoint.io/94e3ce2297d5624c4f90')
    dictsc = josns.json()
    return render_template('网页.html',xx=dictsc)

if __name__ == '__main__':
    app.run(debug=True)
    



