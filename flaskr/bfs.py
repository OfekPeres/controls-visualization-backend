from flask import jsonify, request, make_response
from flaskr import app
import json
import numpy as np
from .submodules.MappingAlgorithms.src.discrete.bfs import BFS
from .utils.numpy_encoder import NumpyEncoder


# http://localhost:5000/random?start=5&end=20
@app.route('/bfs', methods=["GET", "POST"])
def get_bfs():
    
    if request.method == "GET":
        payload = {}
        payload['obstacles'] = [{"shape":"rectangle", "definition":[20,10,40,20]},{"shape":"circle", "definition":[10,10,3]}, {"shape":"circle", "definition":[50,50,20]}]
        payload['start'] = [0,0]
        payload['goal'] = [90,25]
        payload['goalRadius'] = 10
        payload['step_size'] = 1
        payload['width'] = 400
        payload['height'] = 400
        
        bfs = BFS(payload)

        response = make_response(json.dumps(bfs.points_list, cls=NumpyEncoder))
        response.content_type = 'application/json'
        return response
    if request.method == "POST":


        payload = request.get_json()

        
        # print("Type of goalRadius: {}".format(type(payload['goalRadius'])))
        # payload['goalRadius'] = float(payload['goalRadius'])
        # print("Type of goalRadius: {}".format(type(payload['goalRadius'])))
        
        bfs = BFS(payload)
        
        respose_data = {}
        respose_data['goal'] = payload['goal']
        respose_data['goalRadius'] = payload['goalRadius']
        respose_data['obstacles'] = payload['obstacles']
        respose_data['points'] = bfs.points_list
        respose_data['targetNodeIndex'] = len(bfs.points_list)-1
        response = make_response(json.dumps(respose_data, cls=NumpyEncoder))
        response.content_type = 'application/json'
        return response

