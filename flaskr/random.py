from flask import jsonify, request
from flaskr import app
import random
@app.route('/random')
def get_random_number():
    params = request.args.to_dict()
    print(params)
    if not params:
        return jsonify(random.random())
    else:
        start, end = int(params['start']),int(params['end'])
        return jsonify(random.randint(start, end))

