# coding = utf-8
import datetime
from utils.db_util import DB_Util

class Xdcalss_api_test:

    def load_all_case_by_app(self,app):
        '''
        根据 app 加载所有测试用例
        :param app:
        :return:
        '''
        db = DB_Util()
        sql = "select * from `case` where app='{0}'".format(app)
        data = db.query(sql)
        return data

    def load_case_by_id(self,id):
        '''
        根据 id 加载单个测试用例
        :param id:
        :return:
        '''
        db = DB_Util()
        sql = "select * from `case` where id='{0}'".format(id)
        data = db.query(sql,state="one")
        return data

    def load_config_by_app_key(self,app,key):
        '''
        根据 app 和 key 加载配置信息
        :param app:
        :param key:
        :return:
        '''
        db = DB_Util()
        sql = "select * from `config` where app='{0}' and dict_key='{1}'".format(app,key)
        data = db.query(sql,state="one")
        return data


    def update_result_by_case_id(self,id,response,is_pass,msg):
        '''
        根据测试用例 id 更新测试用例结果
        :param response:
        :param id:
        :return:
        '''
        db = DB_Util()
        current_time = datetime.datetime.now().strftime("%y-%m-%d %h:%m:%s")
        print(current_time)
        if is_pass:
            sql = "update `case` set pass='{0}',response='{1}',msg='{2}',update_time='{3}' where id={4}".format(is_pass,'',msg,current_time,id)

        else:
            sql = "update `case` set pass='{0}',response=\'{1}\',msg='{2}',update_time='{3}' where id={4}".format(is_pass,
                                                                                                                str(response),
                                                                                                                msg,
                                                                                                                current_time,
                                                                                                                id)
        rows = db.execute(sql)
        return rows


    def run_all_case(self,app):
        '''
        执行所有测试用例
        :param app:
        :return:
        '''

    def run_case(self,id,host):
        '''
        执行单个测试用例
        :param id:
        :param host:
        :return:
        '''

    def assert_response(self,case,response):
        '''
        断言
        :param case:
        :param response:
        :return:
        '''

    def sent_test_report_to_email(self,app):
        '''
        发送测试报告到指定邮件
        :param app:
        :return:
        '''

if __name__=="__main__":
    test = Xdcalss_api_test()
    #r = test.load_all_case_by_app('小滴课堂')
    r = test.load_config_by_app_key('小滴课堂','host')
    print(r)
