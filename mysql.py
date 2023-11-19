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
def queryMsg(id):
    
    return 
if __name__ == "__main__":
   #queryPasswd("100001")
   queryHead("100002")