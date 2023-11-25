from flask import Flask, jsonify, request, session
import json
import mysql
import pyRedis
import random
app = Flask(__name__,static_folder="./static")

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

# 注册，注册成功之后系统自动分配头像
@app.route("/register",methods=['post'])
def register():
    data =request.get_json()
    name=data['name']
    passwd=data['passwd']
    head="http://47.123.7.97:8080/static/head-%s.jpg"%(str(random.randint(1,3)))
    id=mysql.register(name,head,passwd)
    # return"你的id是%s"%(id)
    if id != 0:
        return {
        "status_code":1,
        "msg":"注册成功",
        "id":str(id),
        "head":str(head)
        }
    else:
        return{
            "status_code":0,
            "msg":"注册失败"
        }




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
        allMsg=mysql.queryMsg(usrId,toUsrId,lastTime)
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
    data=request.get_json()
    usrId=data["from_id"]
    toUsrId=data["to_id"]
    msg=data['msg']
    token=data["token"]
    time=data['time']
    ok=pyRedis.isTokenEqual(usrId,token)
    if ok:
        mysql.insertMsg(usrId,toUsrId,msg,time)
        return{
            "status_code":1,
            "msg":"insert success"
        }
    else:
        return {
            "status_code":0,
            "msg":"token error"
        }

# 获取好友列表
@app.route("/friends",methods=['GET'])
def friendList():
    data=request.get_json()
    id=data['id']
    token=data['token']
    ok=pyRedis.isTokenEqual(id,token)
    if ok:
        friends=mysql.queryFriends(id)
        res={}
        res['status_code']=1
        res['msg']="query success"
        res['res']=friends
        return jsonify(res)
    else:
        return{
            "status_code":0,
            "msg":"token error"
        }
    
# 添加好友
@app.route("/addfriend",methods=['POST'])
def addFriend():
    data=request.get_json()
    id=data['id']
    token=data['token']
    friendId=data['friend_id']
    ok=pyRedis.isTokenEqual(id,token)
    if ok:
        mysql.insertFriend(id,friendId)
        mysql.insertFriend(friendId,id)
        return{
            "status_code":1,
            "msg":"add success"
        }
    else:
        return {
            "status_code":0,
            "msg":"token error"
        }
    
# 获取用户头像
@app.route("/head",methods=['GET'])
def getHead():
    data=request.get_json()
    id=data['id']
    head=mysql.queryHead(id)
    if head!="":
        res={}
        res['status_code']=1
        res['msg']="query success"
        res['head']=head
        return jsonify(res)
    else:
        return{
            "status_code":0,
            "msg":"head is empty"
        }

# 回传个人信息
@app.route("/info",methods=['GET'])
def getInfo():
    data=request.get_json()
    id=data['id']
    token=data['token']
    ok=pyRedis.isTokenEqual(id,token)
    if ok:
        info=mysql.getUsrInfo(id)
        res={}
        res["status_code"]=1
        res["msg"]="get success"
        res['res']=info
        return jsonify(res)
    else:
        return{
            "status_code":0,
            "msg":"get failed"
        }