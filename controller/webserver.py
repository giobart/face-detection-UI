from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from tools.image_upload import direct_image_upload
from tools.db_operations import *
from tools.face_login import *
import json

webserver = Blueprint('webserver', __name__)


@webserver.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')


@webserver.route('/add', methods=['GET'])
def add_page():
    page = request.args.get('page')
    if page is None:
        page = 1
    elif int(page)<1:
        page = 1
    else:
        page = int(page)
    users = users_list(page)
    for elem in users:
        del elem["img"]
    next_page = True
    if len(users) == 0:
        next_page = False
    return render_template('add.html', registered_users=users, page=page, next_page=next_page)


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

@webserver.route('/face_login', methods=['GET'])
def face_login_page():
    return render_template('facelogin.html')

@webserver.route('/delete/<int:id>', methods=['GET'])
def delete_registered_user(id):
    try:
        delete_user(id)
    except Exception as e:
        return e, 200
    return redirect(url_for('webserver.add_page'))


@webserver.route('/login', methods=['POST'])
def login():
    """
        Mock method for login. Does not generate any token, only for demonstrative purpose.
    """
    if request.form['id'] == "admin" and request.form['password'] == "admin":
        return redirect(url_for('webserver.add_page'))
    else:
        return "Invalid credentials", 200


@webserver.route('/face-login', methods=['POST'])
def face_login():
    """
        Mock method for login. Does not generate any token, only for demonstrative purpose.
    """
    img_uri = request.json['imageString']
    if img_uri is not None:
        header, encoded = img_uri.split(",", 1)
        try:
            result = face_login_request(encoded)
            return result["name"], 200
        except Exception as e:
            print(str(e))
            return str(e), 401
    else:
        return "Invalid image", 401
