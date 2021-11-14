from werkzeug.wrappers import request
from flaskr import app
from flask import jsonify, request, make_response
from markupsafe import escape
@app.route('/echo/<text>', methods=['GET', 'POST'])
def show_user_profile(text):
    # show the user profile for that user

    if request.method == "GET":
        return jsonify(f'{escape(text)}')
    
    elif request.method == "POST":
        print("In post request")
        payload = request.get_json()
        return jsonify(payload)