from flask import Flask, request, session
import json
import mysql

app = Flask(__name__)

@app.route("/")
def pong():
    return "pong"
# 登录
@app.route("/login",methods=['POST'])
def login():
    data = request.get_json()
    id=data['id']
    # name = data['name']
    passwd=data['passwd']
    psd=mysql.queryPasswd('%s' %(id))
    if psd == passwd:
        return{
            "status_code":1,
            "msg":"yes"
        }
    else:
        return{
            "status_code":0,
            "msg":"error"
        }

# 注册
@app.route("/register",methods=['post'])
def register():

    return

# 获取历史消息
@app.route("/msg",methods=['GET'])
def getmsg():

    return