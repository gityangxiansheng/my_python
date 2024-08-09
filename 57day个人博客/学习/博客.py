from flask import Flask,render_template
import time
import random


app = Flask(__name__)


@app.route('/')
def method_name():
    cc = time.strftime("%Y")
    #提交-模板render-template
    return render_template('网页.html',times=cc)

if __name__ == '__main__':
    app.run(debug=True)