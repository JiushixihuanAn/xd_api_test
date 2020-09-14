# coding=utf-8

import unittest
from utils.request_util import RequestUtil

class IndexTextCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('滚你妈的开始')
        request = RequestUtil()


    def test_index_category(self):
        request = RequestUtil()
        url = 'https://api.xdclass.net/pub/api/v1/web/all_category'
        response = request.request(url=url,method='get')
        self.assertEqual(response['code'],0,'返回数据存在问题')
        self.assertTrue(len(response['data'])>0,'分类列表为空')

    def test_index_card(self):
        request = RequestUtil()
        url = 'https://api.xdclass.net/pub/api/v1/web/index_card'
        response = request.request(url=url,method='get')
        self.assertEqual(response['code'],0,'返回数据存在问题')
        self.assertTrue(len(response['data'])>0,'视频列表为空')

    def test_index_findListByType(self):
        url = 'https://api.xdclass.net/pub/api/v1/web/product/find_list_by_type'
        data = {'type':'2'}
        request = RequestUtil()
        response = request.request(url=url,method='get',param=data)
        print(response)
        self.assertEqual(response['code'],0,'返回数据错误')
        self.assertTrue( len(response['data']) == True,'返回数据列表为空')

    def test_index_find_ad(self):
        url = 'https://api.xdclass.net/pub/api/v1/web/find_ad_by_id'
        data = {'id':1}
        request = RequestUtil()
        response = request.request(url,'get',param=data)
        self.assertEqual(response['code'],0,'返回数据存在问题')
        self.assertTrue(len(response['data'])>0,'返回数据列表为空')

    def test_index_video(self):
        url = 'https://api.xdclass.net/pub/api/v1/web/video_detail'
        data = {'detail':'52'}
        req = RequestUtil()
        response = req.request(url,'get',data)
        self.assertTrue(response['id'] != 'null',"视频不存在")
        self.assertEqual(response['code'],0,"返回数据存在问题")


if __name__ == '__main__':
    unittest.main(verbosity=2)

