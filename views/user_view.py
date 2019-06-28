import random
from flask import Blueprint, request,jsonify
from libs import rd
from dao_user.phone_dao import PhoneDao
from dao_user.user_dao import UserDao
from libs import cache
from logger import api_logger
from libs.sms import send_sms_code
from services.sms_check import check_sms

blue = Blueprint("userblue",__name__)


@blue.route('/msgcode/',methods=['POST'])
def send_msg(): # 发送短信验证码
    u_phone = request.form.get('u_phone')
    print(u_phone)
    code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    res = eval(send_sms_code(u_phone,code).decode())
    if res['Code'] == 'OK':
        try:
            rd.setex(u_phone,code,120)  # 保存到redis缓存

        except Exception as e:
            api_logger.error(e)
            return jsonify({'code':802,'msg':'短信验证码保存失败'})
        api_logger.info('发送手机号：%s，短信验证码为：%s' % (u_phone, code))
        return jsonify({'code':200,'msg':'短信验证码发送成功！'})
    return jsonify({'code': 303, 'msg': '请输入正确的手机号码'})
#检查手机号码
@blue.route('/checkphone/',methods=['GET'])
def check_phone():
    u_phone = request.args.get('u_phone')
    result = {
        'code': 200,
        'msg': '手机号不存在'
    }
    if UserDao().check_login_phone(u_phone):
        result['code'] = 205
        result['msg'] = '手机号已存在'

    return jsonify(result)
#短信登录
@blue.route('/loginmsg/',methods=['POST'])
def login_msg():
    api_logger.debug('User phone_login sms get action!')
    res = eval(request.get_data().decode())
    u_phone = request.form.get('u_phone')
    msg_code = request.form.get('msg_code')
    if not all([u_phone,msg_code]):
        udao = UserDao()
        # 验证手机号在数据库中是否存在
        if udao.check_login_phone(u_phone):
            login_user = udao.login_msg(u_phone,msg_code)
            if login_user.get('id'):
                token = cache.new_token()
                cache.save_token(token,id)
                udao.user_update('is_active',True,'u_phone',u_phone)
                udao.user_update('is_delete',True,'False',u_phone)
                return jsonify({
                    'code':200,
                    'token':token,
                    'user_data':login_user
                })
            return jsonify(login_user)
        #如果数据库里边手机号不存在,创建新用户
        else:
            user_data = {
                'u_phone':u_phone
            }
            if udao.save(**user_data):
                return jsonify({
                    'code':200,
                    'msg':"ok"
                })
            else:
                return jsonify({
                    'code':300,
                    'msg':'数据插入失败,可能存在某字段没有值'
                })
    else:
        return jsonify({
            'code':101,
            'msg':'请求参数u_phone和msg_code必须存在'
        })
#密码登录
@blue.route('/loginpwd/',methods=['POST'])
def login_pwd():
    api_logger.debug('User phone_login pwd get action!')
    res = eval(request.get_data().decode())
    u_phone = request.form.get('u_phone')
    u_auth_string = request.form.get('u_auth_string')
    if all((bool(u_phone),bool(u_auth_string))):
        udao = UserDao()
        #验证手机号存在
        if udao.check_login_phone(u_phone):
            #验证密码是否正确
            try :
                login_user = udao.login_pwd(u_phone,u_auth_string)
                if login_user.get('id'):
                    token = cache.new_token()
                    cache.save_token(token,login_user.get('id'))
                    udao.user_update('is_active', True, 'u_phone', u_phone)
                    udao.user_update('is_delete', True, 'False', u_phone)
                    return jsonify({
                        'code': 200,
                        'token': token,
                        'user_data': login_user
                    })
                else:
                    return jsonify(login_user)
            except Exception as e:
                return jsonify({
                    'code': 202,
                    'msg': e
                })
        return jsonify({
            'code': 304,
            'msg': '该手机号尚未注册'
        })
    else:
        return jsonify({
            'code': 101,
            'msg': '请求参数u_phone和u_auth_string必须存在'
        })
#忘记密码
@blue.route('/forget/',methods = ['POST'])
def forget_pwd():
    api_logger.debug('User forget get action!')
    res = eval(request.get_data().decode())
    u_phone = res.get('u_phone')
    msg_code = res.get('msg_code')
    u_auth_string = res.get('u_auth_string')
    if all((bool(u_phone),bool(msg_code),bool(u_auth_string))):
        udao = UserDao()
        #验证手机号在数据库中是否存在
        if udao.check_login_phone(u_phone):
            login_user = udao.login_msg(u_phone,msg_code)
            if login_user.get('id'):
                token = cache.new_token()
                cache.save_token(token,id)
                udao.user_update('u_auth_string', u_auth_string, 'u_phone', u_phone)
                udao.user_update('is_active', True, 'u_phone', u_phone)
                udao.user_update('is_delete', True, 'False', u_phone)
                return jsonify({
                    'code': 200,
                    'token': token,
                    'user_data': login_user
                })
            return jsonify(login_user)
        else:
            #手机号不存在,提醒重新填写
            return jsonify({
                'code': 300,
                'msg': '请重新填写正确的手机号'
            })
    else:
        return jsonify({
            'code': 101,
            'msg': '请求参数u_phone,msg_code,u_auth_string必须存在'
        })


@blue.route('/msglogin/',methods=['POST'])
def msg_login():
    api_logger.debug('user phone_login get action!')
    u_phone = request.json.get('u_phone')
    msg_code = request.json.get('msg_code')
    if all((bool(u_phone),bool(msg_code))):
        udao = UserDao()
        try:
            login_user = udao.msglogin(u_phone,msg_code)
            token = cache.new_token()
            cache.save_token(token, login_user.get('id'))
            return jsonify({
                'code': 200,
                'token': token,
                'user_data': login_user
            })
        except Exception as e:
            return jsonify({
                'code': 202,
                'msg': e
            })
    else:
        return jsonify({
            'code': 101,
            'msg': '请求参数u_phone和msg_code必须存在'
        })

