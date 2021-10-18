from flaskr import app
from flask import jsonify
from markupsafe import escape
@app.route('/echo/<text>', methods=['GET', 'POST'])
def show_user_profile(text):
    # show the user profile for that user
    return jsonify(f'{escape(text)}')