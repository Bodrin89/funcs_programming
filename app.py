from flask import Flask, request, jsonify
from class_query import Query
import os
app = Flask(__name__)


@app.route('/perform_query', methods=['GET', 'POST'])
def post():
    req = request.json
    path = os.path.abspath(f'data/{req["file_name"]}')
    with open(path, 'r', encoding='utf-8') as file:
        method = getattr(Query, req['cmd1'], "Такого метода нет")
        method = method(req['value1'], file)
        if req.get('cmd2', None):
            method2 = getattr(Query, req['cmd2'], "Такого метода нет")
            method2 = method2(req['value2'], list(method))
            return jsonify(list(method2))
        return jsonify(list(method))


if __name__ == '__main__':
    app.run()
