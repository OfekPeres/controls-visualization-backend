from flask import jsonify, request, make_response
from flaskr import app
from .submodules.RRT.src.RRT import RRT
import json
import numpy as np

class NumpyEncoder(json.JSONEncoder):
    """ Special json encoder for numpy types """
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


# http://localhost:5000/random?start=5&end=20
@app.route('/rrt')
def get_rrt():
    payload = {}
    payload['obstacles'] = [{"shape":"rectangle", "definition":[20,10,40,20]},{"shape":"circle", "definition":[10,10,3]}, {"shape":"circle", "definition":[50,50,20]}]
    payload['start'] = [0,0]
    payload['goal'] = [90,25]
    payload['goalRadius'] = 10
    payload['d_max'] = 28
    payload['width'] = 400
    payload['height'] = 400
    rrt = RRT(payload)
    
    response = make_response(json.dumps(rrt.GetRRTPayload(), cls=NumpyEncoder))
    response.content_type = 'application/json'
    return response

