import hashlib
import redis
def testRedis():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.set('foo', 'bar')
    print(str(r.get('foo'),encoding='utf-8'))

def generateToken(id):
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    token=hashlib.md5(str(id).encode('utf-8')).hexdigest()
    r.set(id,token)
    print("id=%s,token=%s" %(id,token))

def getToken(id):
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    token=r.get(id)
    return str(token,encoding='utf-8')

def isTokenEqual(id,token):
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    oToken=r.get(id)
    # 需要对获取到的token进行重新编码才可以使用
    res=str(oToken,encoding='utf-8')
    if token == res:
        return True
    else:
        return False
    
if __name__=="__main__":
    token=getToken(1)
    print(token)
    bools=isTokenEqual(1,'c4ca4238a0b923820dcc509a6f75849b')
    print(bools)
    bool2=isTokenEqual(1,"b'c4ca4238a0b923820dcc509a6f75849b'")
    print(bool2)
