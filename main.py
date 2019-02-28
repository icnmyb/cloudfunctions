# -*- coding: utf-8 -*-
from flask import jsonify, make_response

def run(request):
    '''[GCFで呼ばれるメイン関数]

    Arguments:
        request {[dic]} -- [POSTされるjson]
    '''

    try:
        request_json = request.get_json()
        message = request_json['message']
        result_dic = {'message': message}
        return make_response(jsonify(result_dic))
    except (OSError, TypeError) as e:
        return make_response(jsonify({"error":e.args}))
