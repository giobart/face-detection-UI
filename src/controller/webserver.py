from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from src.tools.image_upload import direct_image_upload

webserver = Blueprint('webserver', __name__)


@webserver.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')


@webserver.route('/add', methods=['GET'])
def add_page():
    return render_template('add.html')


@webserver.route('/add', methods=['POST'])
def add_face():
    if 'file' not in request.files:
        return "invalid file", 200
    file = request.files['file']
    try:
        direct_image_upload(
            file,
            request.form['name'].strip(),
            request.form['surname'].strip(),
            request.form['id'].strip()
        )
    except Exception as e:
        print(e)
        return "upload failed, is the upload service available?", 200

    return redirect(url_for('webserver.index_page'))


@webserver.route('/login', methods=['POST'])
def login():
    """
        Mock method for login. Does not generate any token, only for demonstrative purpose.
    """
    if request.form['id'] == "admin" and request.form['password'] == "admin":
        return redirect(url_for('webserver.add_page'))
    else:
        return "Invalid credentials", 200
