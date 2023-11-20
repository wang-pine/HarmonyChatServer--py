from flask import Flask, jsonify, request, session
import json
import mysql
import pyRedis
app = Flask(__name__)

@app.route("/")
def pong():
    return "扫我端口，死你的母亲"
# 登录
@app.route("/login",methods=['POST'])
def login():
    data = request.get_json()
    id=data['id']
    # name = data['name']
    passwd=data['passwd']
    psd=mysql.queryPasswd('%s' %(id))
    if psd == passwd:
        pyRedis.generateToken(id)
        token=pyRedis.getToken(id)
        # res=token.encode('utf-8')
        return{
            "status_code":1,
            "msg":"yes",
            "token":token
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

# token使用测试
@app.route("/token",methods=['POST'])
def tokenTest():
    data =request.get_json()
    id=data['id']
    token=data['token']
    if pyRedis.isTokenEqual(id,token):
        return{
            "status_code":1,
            "msg":"success"
        }
    else:
        return{
            "status_code":0,
            "msg":"fail"
        }

# 获取历史消息
@app.route("/msg",methods=['GET'])
def getmsg():
    data=request.get_json()
    usrId=data["from_id"]
    toUsrId=data["to_id"]
    token=data["token"]
    lastTime=data["last_time"]
    ok=pyRedis.isTokenEqual(usrId,token)
    if ok:
        allMsg=mysql.queryMsg(usrId,toUsrId)
        res={}
        res['status_code']=1
        res['msg']="query success"
        msgJson=mysql.msgToJson(allMsg)
        # msg=json.dumps(allMsg)
        res['res']=msgJson
        return jsonify(res)
    else:
        return{
            "status_code":0,
            "msg":"token error"
        }
# 发送消息  
@app.route("/sendmsg",methods=['POST'])
def sendMsg():
    
    return 