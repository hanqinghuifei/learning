import js2py
import requests
import json
def login():
    session = requests.session()
    session.headers ={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}

    # 获取get响应数据
    response = session.get('http://activity.renren.com/livecell/rKey')

    # 构建n
    n = json.loads(response.content)['data']
    # 构建t
    t = {'password': 'jietouanhao2468'}
    # 构建js执行环境
    context = js2py.EvalJs()

    context.n = n
    context.t = t
    # 获取js
    bigint_js = session.get('http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/BigInt.js').content.decode()
    context.execute(bigint_js)
    rsa_js = session.get('http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/RSA.js').content.decode()
    context.execute(rsa_js)
    bar_js = session.get('http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/Barrett.js').content.decode()
    context.execute(bar_js)


    pwd_js = '''
            t.password = t.password.split("").reverse().join(""),
            setMaxDigits(130);
            var o = new RSAKeyPair(n.e,"",n.n)
            , r = encryptedString(o, t.password);
    '''
    context.execute(pwd_js)
    # 检查密码加密
    print(context.r)
    # 构建post数据
    pwd = context.r
    post_data = {
        'phoneNum': 15922073040,
        'password': pwd,
        'c1': -100,
        'rKey': n['rkey']
    }
    response = session.post('http://activity.renren.com/livecell/ajax/clog', data=post_data)
    print(response.content.decode())

    print('1')
if __name__ == '__main__':
    login()



