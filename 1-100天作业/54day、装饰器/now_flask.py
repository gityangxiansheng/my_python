from flask import Flask
app = Flask(__name__)

@app.route('/')
def ons():
    return '<h1 style="color: red;text-align: center;">主页</h1>' \
        '<img  src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbTBtajNjejVxOHBrcjdwanY1M2J4NmNkM3VpcDc1Nno0bHdnMDhrbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5jCTUWzwtqG2s/giphy.gif" alt="猫啊" width="800" style="display: block; margin: 0 auto;">'

@app.route('/usrename/<name>/<int:number>')
def hello_world(name,number): 
    return  f"<h1 style='text-align: center;'>您好亲爱的 {name}先生,恭喜您今年{number}岁了!</h1>" \
        '<img  src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGNhczNtYWwyNnQzb21odGZzbTd3YjZtemxrbzludGgwZHlrM21tdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MCeIiRETfwBK2rtGRi/giphy.gif" alt="蛋糕" width="800" style="display: block; margin: 0 auto;">'


def make_bold(bay):
    def bold_in():
        bayc = "<b>"+bay()+"</b>"
        return bayc
    return bold_in

def make_emphasis(bay):
    def emphasis_in():
        bayc = "<em>"+bay()+"</em>"
        return bayc
    return emphasis_in

def make_underlined(bay):
    def underlined_in():
        bayc = "<u>"+bay()+"</u>"
        return bayc
    return underlined_in

@app.route('/bay')
@make_bold
@make_underlined
@make_emphasis
def bay():
    return "Bay"





if __name__ == '__main__':
    app.run(debug=True)
