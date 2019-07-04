from flask import Blueprint
from flask import request, jsonify
from dao.address_dao import AddressDao
from libs import cache
from libs.cache import get_token_user_id

blue_addr = Blueprint('addr_api', __name__)


@blue_addr.route("/address/query/", methods=("POST",))
def address_query():
    resp = request.get_json()
    if resp:
        token = resp.get('token')
        user_id = cache.get_token_user_id(token)
        dao = AddressDao()
        data = dao.address_query(user_id)
        if data:
            return jsonify({
                'code': 200,
                'msg': 'ok',
                'data': data
            })
    return jsonify({
        'code': 201,
        'msg': '请求数据失败',
    })

@blue_addr.route('/address/add/', methods=('POST',))
def address_view():
    # 新增收货地址
    # [{'name:'tom'},{'phone_num':'18333332222'},{'address_details':'陕西省西安市雁塔区玫瑰公馆'},
    # {'addr_type':'0'}]
    data = request.get_json().get('data', None)
    addr_data = { key:value for d in data for key, value in d.items()}
    token = request.args.get("token", None)
    if token is None:
        return jsonify({"code": 201, "msg": "token查询参数必须提供"})
    u_id = get_token_user_id(token)
    addr_data['user_id_id'] = u_id
    if u_id:
        # resp 为一个列表
        if not addr_data:
            return jsonify({
                'code': '202',
                'msg': '参数error'
            })
        else:
            # tom,123456789,西安市#高新区#高新6路,0,1
            # 插入数据address表
            dao = AddressDao()
            dao.saves(**addr_data)
            return jsonify({
                'code': '200',
                'msg': '更新地址成功！',
                'data': addr_data
            })
    else:
        return jsonify({
            'code': '202',
            'msg': 'token不正确'
        })

@blue_addr.route("/address/edit/", methods=('POST',))
def edit():
    resp = request.get_json()
    if resp:
        id = resp.get('id')
        dao = AddressDao()
        data = dao.address_edit_query(id)
        if id :
            return jsonify({
                'code': 200,
                'msg': 'ok',
                'data': data
            })
        return jsonify({
            'code': 201,
            'msg': '请求数据失败',
        })
    return jsonify({
            'code': 202,
            'msg': '需要一个地址id',
        })

@blue_addr.route('/address/delete/', methods=('POST',))
def address_delete():
    data_id = request.get_json()
    print(data_id)
    token = request.args.get("token", None)
    if token is None:
        return jsonify({"code": 201, "msg": "token查询参数必须提供"})
    u_id = get_token_user_id(token)
    if u_id:
        # resp 为一个列表
        if not data_id:
            return jsonify({
                'code': '202',
                'msg': '参数error'
            })
        else:
            # tom,123456789,西安市#高新区#高新6路,0,1
            # 插入数据address表
            dao = AddressDao()
            dao.delete_address(data_id, u_id)








