from flask import jsonify, request, make_response
from flaskr import app
import json
import numpy as np
from .submodules.controls_algorithms.src.dynamics.dubins_car import DubinsCar
from .submodules.controls_algorithms.src.controls.bang_bang import BangBang
from .utils.numpy_encoder import NumpyEncoder
from .submodules.controls_algorithms.src.controls.dubins_path import DubinsPath
from .submodules.controls_algorithms.src.controls.converter import GetWaypointsFromDubinsPathOuput
from datetime import datetime

@app.route('/bangbang', methods=["GET", "POST"])
def bangbang():
    if request.method == "GET":
        # Mock Data
        payloadFromFrontEnd = [{
            'x': 100,
            'y': 100
        }, {
            'x': 150,
            'y': 250
        }, {
            'x': 200,
            'y': 360
        }, {
            'x': 250,
            'y': 120
        }, {
            'x': 220,
            'y': 180
        }]
        points = []
        for point in payloadFromFrontEnd:
            points.append(np.array([point['x'], point['y']]))

        car = DubinsCar(50, 0, 0, 0 * np.pi / 4, 0, 20)

        controller = BangBang(points, car)
        print("About to calculate trajectory")
        traj = controller.GetControlTrajectory()

        data = {'points': points, 'finalPos': car.pos, 'controls': traj}
        response = make_response(json.dumps(data, cls=NumpyEncoder))
        response.content_type = 'application/json'
        return response
    if request.method == "POST":
        payload = request.get_json()
        points = []
        for point in payload['waypoints']:
            points.append(np.array([point['x'], point['y']]))

        # points = [np.array([point['x'], point['y']]) for point in payload["waypoints"]]
        l = payload['carLength']
        speed = payload['carSpeed']
        x = payload['x']
        y = payload['y']
        theta = payload['theta']

        car = DubinsCar(l, x, y, theta, 0, speed)

        controller = BangBang(points, car)

        traj = controller.GetControlTrajectory()

        data = {'points': points, 'finalPos': car.pos, 'controls': traj}
        response = make_response(json.dumps(data, cls=NumpyEncoder))
        response.content_type = 'application/json'
        return response


@app.route('/dubins_path', methods=["POST"])
def dubins_analytic_path():
    if request.method == "POST":
        payload = request.get_json()
        # for point in payload['targetPoses']:
        #     points.append(np.array([point['x'], point['y']]))

        targetPoses = []
        for pose in payload['targetPoses']:
            p = np.array([pose['x'], pose['y'], pose['theta']])
            targetPoses.append(p)
        l = payload['carLength']
        speed = payload['carSpeed']
        x = payload['x']
        y = payload['y']
        theta = payload['theta']

        car = DubinsCar(l, x, y, theta, 0, speed)

        pathGenerator = DubinsPath(car)
        
        waypoints = []
        paths = []
        for i in range(len(targetPoses)-1):
            startPose = targetPoses[i]
            goalPose = targetPoses[i+1]
            output = pathGenerator.GetDubinsPath(startPose, goalPose)
            paths.extend(output['path'])
            waypoints.extend(GetWaypointsFromDubinsPathOuput(output))
        
        waypoints = [{'x':point[0], 'y':point[1]} for point in waypoints]
        data = {'waypoints': waypoints, 'paths':paths, 'type':output['type']}
        response = make_response(json.dumps(data, cls=NumpyEncoder))
        response.content_type = 'application/json'
        return response