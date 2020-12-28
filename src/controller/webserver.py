from flask import Blueprint, request, jsonify, render_template

webserver = Blueprint('webserver', __name__)


@webserver.route('/', methods=['GET'])
def index_page():

    return render_template('index.html')
