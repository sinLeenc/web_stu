
from flask import Flask,render_template,request

app = Flask(__name__)

# 创建了网址 /show/info 和函数 index 的对应关系
# 用户在浏览器访问 /show/info, 网站自动执行index
@app.route("/show/info")
def index():
    # 自动取templates中找到  index.html
    return render_template("index.html")

# article页面
@app.route("/article/info")
def article():
    return render_template("article_index.html")

# 表格页面
@app.route("/form/data")
def fromdata():
    return render_template("form_data.html")

# 用户登录界面
@app.route("/user/login")
def userLogin():
    return render_template("user_login.html")

# 用户注册界面
@app.route("/user/register", methods=['GET','POST'])
def userRegister():
    if request.method == "GET":
        return render_template("user_register.html")
    else:
        # 1. 接受用户通过POST形式发送过来的数据
        print(request.form)
        user = request.form.get('user')
        password = request.form.get('pwd')
        # 获取多个
        hobby = request.form.getlist('hobby')
        # ...
        print(user, password, hobby)
        # 将用户信息写入文件中实现注册, 写入到excel中实现注册, 写入数据库中实现注册

        # 2. 给用户再返回结果
        return "注册成功"


# # 注册提交表单地址
@app.route("/get/register", methods=['GET','POST'])
def get_register():
    # 1. 接受到数据
    print(request.args)
    # 2. 给用户再返回结果
    return "注册成功"

# # 注册提交表单地址post
# @app.route("/post/register", methods=['POST'])
# def post_register():
#     # 1. 接受用户通过POST形式发送过来的数据
#     print(request.form)
#     user = request.form.get('user')
#     password = request.form.get('pwd')
#     # 获取多个
#     hobby = request.form.getlist('hobby')
#     #...
#     print(user, password, hobby)
#     # 将用户信息写入文件中实现注册, 写入到excel中实现注册, 写入数据库中实现注册
#
#     # 2. 给用户再返回结果
#     return "注册成功"

if __name__ == '__main__':
    app.run(debug=True)