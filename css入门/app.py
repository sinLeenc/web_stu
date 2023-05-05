from flask import Flask,render_template,request


app = Flask(__name__)



@app.route('/index')
def index():
    return render_template("index.html")

# 登录界面
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login_css.html")

# 注册界面
@app.route('/register')
def register():
    return render_template("register_css.html")


@app.route('/css/style')
def css_style():
    return render_template('css_style.html')

@app.route('/example/xiaomi')
def example_xiaomi():
    return render_template('example_xiaomi.html')


if __name__ == '__main__':
    app.run(debug=True)