import unittest
from utils.request_util import RequestUtil
host = 'https://api.xdclass.net'

global token
class UserTestCase(unittest.TestCase):

    def test_login(self):
        req = RequestUtil()
        url = host + '/pub/api/v1/web/web_login'
        data = {'phone':'13113777555',
                'pwd':'1234567890'}
        response = req.request(url,'post',param=data,content_type='application/x-www-form-urlencoded')

        global token
        token = response['data']['token']
        self.assertEqual(response['code'],0,'登录失败')
        self.assertTrue(response['data'] !=  'null','返回数据为空，登录失败')

    def test_info(self):
        print(token)
        req = RequestUtil()
        url = host + '/pub/api/v1/web/user_info'
        headers = {'token':'{0}'.format(token)}
        response = req.request(url, 'post', headers=headers, content_type='application/json')

        self.assertEqual(response['code'], 0, '查询失败')
        self.assertTrue(response['data'] != 'null', '返回数据为空，查询失败')

if  __name__ == '__main__':
    #  依赖需要解决
    
    unittest.main()
