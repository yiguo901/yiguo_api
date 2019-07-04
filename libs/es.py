"""
封装ElasticSearch搜索引擎的SDK(library库)
"""
import requests
import pymysql
from pymysql.cursors import DictCursor


class ESearch():
    def __init__(self, index):
        self.host = '121.199.63.71'
        self.port = '9203'
        self.index = index

    def create_index(self):
        url = f'http://{self.host}:{self.port}/{self.index}'
        resp = requests.put(url, json={
            "settings": {
                "number_of_shards": 5,
                "number_of_replicas": 1
            }
        })
        resp_data = resp.json()
        print(resp_data)
        if resp_data.get('acknowledged'):
            print('create index %s ok!' % self.index)

    def remove_index(self):
        url = f'http://{self.host}:{self.port}/{self.index}'
        requests.delete(url)
        print('删除成功!')

    def add_doc(self, doc_type, id=None, **values):
        url = f'http://{self.host}:{self.port}/{self.index}/{doc_type}/'
        if id:
            url += f"{id}"
        resp = requests.post(url, json=values)
        resp_data = resp.json()
        print(resp_data)
        if resp_data.get('result') == "created":
            print('add doc %s ok!' % values)
        else:
            print('add doc %s error!' % values)

    def query(self, keyword):
        url = f'http://{self.host}:{self.port}/{self.index}/_search?q={keyword}'
        resp = requests.get(url)
        resp_data = resp.json()
        if resp_data.get('hits').get('total') > 0:
            return {
                'code': 200,
                'total': resp_data.get('hits').get('total'),
                'datas': [data.get('_source')
                          for data in resp_data.get('hits').get('hits')
                          ]
            }
        else:
            return {'code': 201, 'msg': '无'}


def init_index():

    # 连接数据库，将doctors表数据添加到索引库中
    db = pymysql.Connect(host="localhost",
                         port=3306,
                         user='root',
                         password='123456',
                         db='yiguo',charset='utf8')
    with db.cursor(cursor=DictCursor) as c:
        c.execute('select category_id, category_name, child_id,child_name from goods')

        es_ = ESearch('ygindex')
        # es_.remove_index()
        es_.create_index()
        for row_data in c.fetchall():
            print(row_data)
            es_.add_doc('goods', **row_data)

        print('--init add goods doc_type all ok--')

# def init_index():
#     db = DB()
#     with db.conn.cursor(cursor=DictCursor) as c:
#         c.execute('select id,child_name from goods')
#         es_ = ESearch('ygindex')
#         for row_data in c.fetchall():
#             es_.add_doc('goods', **row_data)
#         print('___init add goods doc_type all ok!')


if __name__ == '__main__':

    # search = ESearch('ygindex')
    # print(search.query('苹果'))
    # init_index()
    # search.remove_index()
    # serarch = ESearch('ygindex')
    # print(serarch.query('苹果'))
    # search.remove_index()
    init_index()