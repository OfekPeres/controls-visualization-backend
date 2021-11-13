from flask import jsonify, request, make_response
from flaskr import app
import json
import numpy as np
from .submodules.RRT.src.RRT import RRT

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
@app.route('/rrt', methods=["GET", "POST"])
def get_rrt():
    if request.method == "GET":
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
    if request.method == "POST":
        payload = request.get_json()
        # print("----------------------------")
        # print("Printing Post method output")
        # print("Start: {}".format(payload['start']))
        # print("Goal: {}".format(payload['goal']))
        # print("Goal Radius: {}".format(payload['goalRadius']))
        # print("Goal Radius type: {}".format(type(payload['goalRadius'])))
        # print("d_max: {}".format(payload['d_max']))
        # print("Width: {}".format(payload['width']))
        # print("Height: {}".format(payload['height']))
        # print("Obstacles: {}".format(payload['obstacles']))
        # print("----------------------------")

        
        # print("Type of goalRadius: {}".format(type(payload['goalRadius'])))
        # payload['goalRadius'] = float(payload['goalRadius'])
        # print("Type of goalRadius: {}".format(type(payload['goalRadius'])))
        
        rrt = RRT(payload)
        
        response = make_response(json.dumps(rrt.GetRRTPayload(), cls=NumpyEncoder))
        response.content_type = 'application/json'
        return response

