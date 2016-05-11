from workflow.web import post
from workflow.notify import notify
from urllib2 import URLError

LOGIN_URL = 'http://net.tsinghua.edu.cn/do_login.php'

def login(username, md5pwd):
    data = {
        'action': 'login',
        'username': username,
        'password': u'{MD5_HEX}' + md5pwd,
        'ac_id': 1
    }

    try:
        res = post(LOGIN_URL, data=data, timeout=1)
        notify(title=str(res.status_code), text=res.text)
    except URLError as e:
        notify(title=str(e.errno), text=str(e.reason))

def logout():
    data = { 'action': 'logout' }
    try:
        res = post(LOGIN_URL, data=data, timeout=1)
        notify(title=str(res.status_code), text=res.text)
    except URLError as e:
        notify(title=str(e.errno), text=str(e.reason))
