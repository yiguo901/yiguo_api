from flask import Blueprint, jsonify, request

from libs.es import ESearch

blue_es = Blueprint('es_api', __name__)


@blue_es.route('/search/', methods=("GET",))
def serach_view():

    res = request.args.get('q')
    search = ESearch('ygindex')

    return jsonify({
        'code': 200,
        'msg': 'ok',
        'data': search.query(res)
    })

