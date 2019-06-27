from dao import BaseDao
from logger import api_logger

from libs.crypt import make_password, check_password


class UserDao(BaseDao):

    def save(self, **values):
        api_logger.info('db insert Yguser: <%s>' % values['user_phone'])
        values['user_password'] = make_password(values['user_password'])
        return super(UserDao, self).save('user_phone', **values)

    def check_login_name(self, user_phone):
        # 检查用户名是否已存在
        result = self.query('select id as cnt from Yguser where user_phone=%s', user_phone)
        return not bool(result)

    def login(self, user_phone, user_password):
        sql = 'select id, user_password from Yguser ' \
              'where user_phone=%s and activated=%s'
        user_data = self.query(sql, user_phone, 1)

        if user_data:
            user_id, auth_str = (user_data[0].get('id'),
                                 user_data[0].get('user_password'))

            if check_password(user_password, auth_str):
                # 验证成功
                user_profile = self.get_profile(user_id)
                if user_profile is None:
                    return {
                        'user_id': user_id,
                        'nick_name': user_phone
                    }

                return user_profile
            api_logger.warn('用户 %s 的口令不正确' % user_phone)
            raise Exception('用户 %s 的口令不正确' % user_phone)
        else:
            api_logger.warn('查无此用户 %s' % user_phone)
            raise Exception('查无此用户 %s' % user_phone)

    def get_profile(self, user_id):
        # 获取用户的详细信息
        sql = "select user_id, nick_name, phone, photo from Yguser " \
              "where user_id=%s"
        user_profile = self.query(sql, user_id)
        if user_profile:
            return user_profile[0]


if __name__ == '__main__':
    dao = UserDao()
    # dao.login('disen', 'disen666')  # 登录成功之后的数据
    print(dao.check_login_name('disen'))