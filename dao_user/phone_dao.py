from dao_user import BaseDao
from logger import api_logger


class PhoneDao(BaseDao):

    def save(self,**values):
        # api_logger.info('db replace users:<%s>' % values['phone'])
        super(PhoneDao,self).save('users',**values)