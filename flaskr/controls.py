from flask import jsonify, request, make_response
from flaskr import app
import json
import numpy as np
from .submodules.controls_algorithms.src.dynamics.dubins_car import DubinsCar
from .submodules.controls_algorithms.src.controls.bang_bang import BangBang
from .utils.numpy_encoder import NumpyEncoder


@app.route('/bangbang', methods=["GET", "POST"])
def bangbang():
    if request.method == "GET":
        # Mock Data
        payloadFromFrontEnd = [{'x':100, 'y':100}, {'x':150, 'y':250}, {'x':200, 'y':360}, {'x':250, 'y':120}, {'x':220, 'y':180} ]
        points = []
        for point in payloadFromFrontEnd:
            points.append(np.array([point['x'], point['y']]))

        
        car = DubinsCar(20, 0, 0, 0*np.pi/4, 0, 20)

        controller = BangBang(points, car)
        print("About to calculate trajectory")
        traj = controller.GetControlTrajectory()
        
        data = {'points':points, 'finalPos':car.pos, 'controls':traj}
        response = make_response(json.dumps(data, cls=NumpyEncoder))
        response.content_type = 'application/json'
        return response
    if request.method == "POST":
        payload = request.get_json()
        
        response = make_response("Placedholder")
        response.content_type = 'application/json'
        return response






    

    # print("# of control inputs: {}".format(len(traj)))
    # print(traj)
    # print("0 control input: {}".format(np.where(traj == 0)))
    # print(np.where(traj <0))
    # # np.where(traj >0)
    # print("Final car position: {}".format(car.pos))