from dao import BaseDao

class AddressDao(BaseDao):
    # 数据库查询地址信息
    def address_query(self,user_id):
        try:
            # 地址
            address = self.list('address', ('id', 'name', 'phone_num', 'address_details', 'addr_type'),
                                where='user_id_id', args=user_id, page=1, page_size=5)
        except Exception as e:
            raise Exception({'code': 201, 'msg': e})
        return {
            "address": address,
        }

    def saves(self, **values):
            return super(AddressDao, self).save('address', **values)


    def address_edit_query(self,user_id):
        try:
            # 编辑地址
            edit = self.list('address', ('id', 'name', 'phone_num', 'address_details', 'addr_type'),
                             where='id', args=user_id)

        except Exception as e:
            raise Exception({'code': 201, 'msg': e})

        return {
            "edit": edit
        }

    def delete_address(self, id, user_id):
        sql = "delete from address where id=%s and user_id=%s"
        del_address = self.query(sql, id, user_id)
        return del_address
