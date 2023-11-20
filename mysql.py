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
    sql="SELECT head FROM usr WHERE id="+id+";"
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
def queryMsg(usrId,toUsrId):
    db = pymysql.connect(host="localhost",
                         user="root",
                         password="ws030114",
                         database="harmonychat" )
    cursor = db.cursor()
    sql="SELECT * FROM msg WHERE fromusr="+str(usrId)+" AND tousr="+str(toUsrId)+";"
    cursor.execute(sql)
    results=cursor.fetchall()
    allmsg=[]
    for row in results:
        msgTemp=msg(row[0],row[1],row[2],row[3],row[4])
        print("%s %s %s %s %s" %(row[0],row[1],row[2],row[3],row[4]))
        allmsg.append(msgTemp)
    db.close()
    return allmsg


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
def register(name,head):
    return id
if __name__ == "__main__":
   #queryPasswd("100001")
   # queryHead("100002")
# test get msg
    allmsg=queryMsg(100001,100002)
#    print("all msg is")
#    for element in allmsg:
#        print('%s %s %s %s %s' %(element.msgId,element.fromUsr,element.toUsr,element.msg,element.date))
    list=[]
    for element in allmsg:
        temp={}
        temp['id']=element.msgId
        temp['to_usr']=element.toUsr
        temp['from_usr']=element.fromUsr
        temp['msg']=element.msg
        temp['date']=str(element.date)
        list.append(temp)
    # json.dump(list)
    print(list)