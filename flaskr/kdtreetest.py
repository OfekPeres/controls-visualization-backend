from KDTree4RRT.KDTree import KDTree
from flaskr import app
from flask import jsonify
from markupsafe import escape
@app.route('/kdtree', methods=['GET', 'POST'])
def kdtree():
    # show the user profile for that user
    return jsonify(f'{escape(KDTree())}')