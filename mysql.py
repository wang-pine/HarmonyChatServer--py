import json
import pymysql
# 查询密码
def queryPasswd(id):
    db = pymysql.connect(host="localhost",
                         user="root",
                         password="ws030114",
                         database="harmonychat" )
    cursor = db.cursor()
    sql="SELECT passwd FROM usr WHERE id="+id+";"
    cursor.execute(sql)
    results=cursor.fetchall()
    for row in results:
        passwd=row[0]
        print("passwd=%s" %(passwd))
    db.close()
    return passwd

# 查询头像
def queryHead(id):
    db = pymysql.connect(host="localhost",
                         user="root",
                         password="ws030114",
                         database="harmonychat" )
    cursor = db.cursor()
    sql="SELECT head FROM usr WHERE id="+str(id)+";"
    cursor.execute(sql)
    results=cursor.fetchall()
    for row in results:
        head=row[0]
        print("head=%s" %(head))
    db.close()
    return head

# 查询消息
class msg:
    def __init__(self,msgId,fromUsr,toUsr,msg,date):
        self.msgId = msgId
        self.toUsr=toUsr
        self.fromUsr=fromUsr
        self.msg=msg
        self.date=date
def queryMsg(usrId,toUsrId,date):
    db = pymysql.connect(host="localhost",
                         user="root",
                         password="ws030114",
                         database="harmonychat" )
    cursor = db.cursor()
    strDate='"'+date+'"'
    # sql='SELECT * FROM msg WHERE fromusr='+str(usrId)+' AND tousr='+str(toUsrId)+' WHERE time >='+strDate+';'
    sql = "SELECT *FROM msg WHERE fromusr= %s AND tousr= %s AND time >= '%s' " %(usrId,toUsrId,date)
    cursor.execute(sql)
    results=cursor.fetchall()
    allmsg=[]
    for row in results:
        msgTemp=msg(row[0],row[1],row[2],row[3],row[4])
        print("%s %s %s %s %s" %(row[0],row[1],row[2],row[3],row[4]))
        allmsg.append(msgTemp)
    db.close()
    return allmsg

# 全部信息转json能解析的格式
def msgToJson(msg):
    list=[]
    for element in msg:
        temp={}
        temp['id']=element.msgId
        temp['to_usr']=element.toUsr
        temp['from_usr']=element.fromUsr
        temp['msg']=element.msg
        temp['date']=str(element.date)
        list.append(temp)
    return list

# 注册新用户
def register(name,head,passwd):
    db = pymysql.connect(host="localhost",user="root",password="ws030114",database="harmonychat")
    cursor = db.cursor()
    sql=("INSERT INTO usr(name,head,passwd) VALUES('%s','%s','%s')" %(name,head,passwd))
    cursor.execute(sql)
    id=cursor.lastrowid
    db.commit()
    db.close()
    return id

# 添加新的信息
def insertMsg(fromUsr,toUsr,msg,time):
    db = pymysql.connect(host="localhost",
                         user="root",
                         password="ws030114",
                         database="harmonychat" )
    cursor = db.cursor()
    sql=("INSERT INTO msg(tousr,fromusr,msg,time) VALUES(%s,%s,'%s','%s')" %(toUsr,fromUsr,msg,time))

    cursor.execute(sql) 
    db.commit() # 切记，还需要commit到数据库执行
    db.close()
    # return cursor.lastrowid()

# 查询所有的好友id
def queryFriends(id):
    db = pymysql.connect(host="localhost",
                         user="root",
                         password="ws030114",
                         database="harmonychat" )
    cursor = db.cursor()
    sql="SELECT friendid FROM friend WHERE usrid="+str(id)+";"
    cursor.execute(sql)
    results=cursor.fetchall()
    list = []
    for row in results:
        list.append(row[0])
    return list

# 插入好友信息
def insertFriend(usrId,friendId):
    db = pymysql.connect(host="localhost",
                         user="root",
                         password="ws030114",
                         database="harmonychat" )
    cursor = db.cursor()
    sql="INSERT INTO friend(usrid,friendid) VALUES("+str(usrId)+","+str(friendId)+");"
    cursor.execute(sql) 
    db.commit() # 切记，还需要commit到数据库执行
    db.close()

# 获取个人信息
def getUsrInfo(usrId):
    res={}
    db = pymysql.connect(host="localhost",
                         user="root",
                         password="ws030114",
                         database="harmonychat" )
    cursor = db.cursor()
    sql="SELECT * FROM usr WHERE id="+str(usrId)+";"
    cursor.execute(sql)
    results=cursor.fetchall()
    for row in results:
        id=row[0]
        name=row[1]
        head=row[2]
        res['id']=id
        res['name']=name
        res['head']=head
        print("id=%s,name=%s,head=%s" %(id,name,head))
    db.close()
    return res

if __name__ == "__main__":
   #queryPasswd("100001")
   # queryHead("100002")
# test get msg
     allmsg=queryMsg(100001,100002,'2023-11-12 23:00:00')
     print("all msg is")
     for element in allmsg:
        print('%s %s %s %s %s' %(element.msgId,element.fromUsr,element.toUsr,element.msg,element.date))
    # list=[]
#     for element in allmsg:
#         temp={}
#         temp['id']=element.msgId
#         temp['to_usr']=element.toUsr
#         temp['from_usr']=element.fromUsr
#         temp['msg']=element.msg
#         temp['date']=str(element.date)
#         list.append(temp)
#     # json.dump(list)
#     print(list)
    # insertMsg(100003,100005,"你好","2023-11-20 13:20:20")
    # res = queryFriends(100001)
    # print(res)
    # insertFriend(100004,100005)
    # res = getUsrInfo(100001)
    # print(res)
    # allmag=queryMsg(100001,100003,'2023-11-20 20:47:20')
    # jsonmsg=msgToJson(allmag)
    # print(jsonmsg)
    # id=register("wang-ss","nulll","dddiwndiwdnwd")
    # print("id=%s" %(id))