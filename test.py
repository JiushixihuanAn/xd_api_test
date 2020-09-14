import pymysql


class db_util:

    def __init__(self):
        #连接数据库
        self.connection = pymysql.connect(host='123.57.7.179',
                                 user='yang',
                                 password='yxf063520.',
                                 db='xd_api_test_demo')
        #使用 cursor 方法获取操作游标，得到一个可以执行的 sql 语句，并且操作结果作为字典返回的游标
        self.cursor = self.connection.cursor(cursor=pymysql.cursors.DictCursor)


    def __del__(self):

        self.cursor.close()
        self.connection.close()


    def query(self,sql,state="all"):
        '''
        查询方法
        :param sql:
        :param state:默认按照全部查询
        :return:
        '''
        try:
            #使用 execute 方法执行sql语句
            # ``
            self.cursor.execute(sql)

            #查询全部
            if state == "all":
                data = self.cursor.fetchall()
            #查询单条
            else:
                data = self.cursor.fetchone()
            return data

        except Exception as e:
            print(e)

    def execute(self,sql):

        try:
            #执行 sql 操作
            rows = self.cursor.execute(sql)
            #提交事件
            self.connection.commit()
            return rows

        except Exception as e:
            print("数据库操作异常 {0}".format(e))
            #回滚
            self.connection.rollback()

if __name__=="__main__":

    db = db_util()
    result = db.query("select * from `case`")
    result1 = db.execute("insert into `case`(`app`) values('hello')")

    print(result)
