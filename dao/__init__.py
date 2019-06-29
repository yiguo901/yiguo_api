import pymysql
from pymysql.cursors import DictCursor
from logger import api_logger


DB_CONFIG = {


    "host":"localhost",
    "port":3306,
    # "user":"ygadmin",
    # "password":"yg1176",
    # "db":"yg_api_db",
    # "charset":"utf8"
    "user":"root",
    "password":"123456",
    "db":"yiguo",
    "charset":"utf8"

}


class DB:
    def __init__(self):
        self.conn = pymysql.Connect(**DB_CONFIG)

    def __enter__(self):
        if self.conn is None:
            self.conn = pymysql.Connect(**DB_CONFIG)

        return self.conn.cursor(cursor=DictCursor)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        else:
            api_logger.error(exc_val)
            self.conn.rollback()

        return True # 异常不会继续向外抛出


class BaseDao():
    def __init__(self):
        self.db = DB()

    def save(self,table_name,**values):
        sql = 'replace into %s(%s) values(%s)' % \
              (table_name,
               ','.join(values.keys()),
               ','.join(['%%(%s)s' % key for key in values.keys()])
               )
        success = False
        with self.db as c:
            c.execute(sql,args=values)
            api_logger.info('replace %s ok!' % sql)
            success = True
        return success

    def delete(self,table_name,by_id):
        pass

    def list(self,table_name,*fileds,
             where=None,args=None,page=1,page_size=20):
        sql = "select {} from {} where {}={} limit {},{}".format\
            (','.join(*fileds),table_name,where,args,(page-1)*page_size,page_size)
        with self.db as c:
            c.execute(sql)
            result = c.fetchall()
            api_logger.info('select %s ok!' % sql)
            return result

    def count(self,table_name):
        pass

    
    # def query(self, table, *fields, page=1):
    #     if not len(fields):
    #         sql = 'select * from %s limit %s' % (table, page)
    #     else:
    #         sql = 'select %s from %s limit %s' % (','.join(fields), table,page)
    #
    #     print(sql)
    #     with self.db as c:
    #         c.execute(sql)
    #         data = c.fetchall()
    #     return data
    
    def query(self, sql, *args):
        with self.db as c:
            c.execute(sql, args=args)
            data = c.fetchall()
            if data:
                data = list(data)

        return data
