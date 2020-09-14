import requests

'''
Http请求工具封装
'''

class RequestUtil:

    def __init__(self):
        pass


    def request(self,url,method,headers=None,param=None,content_type=None):
        try:
            if method=='get':
                result = requests.get(url=url,params=param,headers=headers).json()
                return result
            elif method=='post':
                if content_type == 'application/json':
                    result = requests.post(url=url,json=param,headers=headers).json()
                    return result
                else:
                    result = requests.post(url=url,data=param,headers=headers).json()
                    return result
            else:
                print("Http method {0} 未添加".format(method))

        except Exception as e:

            print('Http请求报错：{0}'.format(e))

if __name__ == '__main__':

    r = RequestUtil()

    # #get 方法验证
    # url = 'https://api.xdclass.net/pub/api/v1/web/all_category'
    # res = r.request(url=url,method='get')
    # print(res)

    # post 方法验证
    url = 'https://api.xdclass.net/pub/api/v1/web/web_login'
    data = {'phone':'13113777555',
            'pwd':'1234567890'}
    headers = {'Content_Type':'application/x-www-form-urlencoded'}
    res = r.request(url=url,method='post',param=data,headers=headers)
    print(res)