from dao import BaseDao


class cart_dao(BaseDao):

    def query(self, table):
        sql = 'select * from %s' % (table)
        # sql = 'select %s from %s limit %s' % (','.join(fields), table,page)

        print(sql)
        with self.db as c:
            c.execute(sql)
            data = c.fetchall()
        return data

    def add_cart(self):
        pass

    def cart_list(self):
        pass

