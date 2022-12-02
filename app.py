from flask import Flask, request
from class_query import Query
from utils.utils import open_file
import os
app = Flask(__name__)


@app.route('/perform_query', methods=['GET', 'POST'])
def post():
    req = request.json
    path = os.path.abspath(f'data/{req["file_name"]}')

    method = getattr(Query, req['cmd1'], "Такого метода нет")
    method = method(req['value1'], open_file(path))
    if req.get('cmd2', None):
        method2 = getattr(Query, req['cmd2'], "Такого метода нет")
        method2 = method2(req['value2'], list(method))
        return list(method2)
    return list(method)




if __name__ == '__main__':
    app.run()
