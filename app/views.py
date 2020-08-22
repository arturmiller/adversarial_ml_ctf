import base64
from io import BytesIO

import flask
from PIL import Image
import numpy as np

from app import app, model


@app.route('/')
def home():
    return flask.render_template('index.html')


random_number = ''.join([str(value) for value in np.random.randint(10, size=30)])
@app.route('/hidden_page_' + random_number)
def hidden_page():
    return flask.render_template('hidden_page.html')


@app.route('/check', methods=['POST'])
def check():
    data = flask.request.get_data()
    image = decode_image(data)
    similarity = model.check_similarity(image)
    response = create_response(similarity)
    return response


def decode_image(data):
    starter = data.find(b',')
    image_data = data[starter+1:]
    image = Image.open(BytesIO(base64.b64decode(image_data))).convert('RGB')
    return image


def create_response(similarity):
    if similarity > 80.0:
        data = flask.redirect(flask.url_for('hidden_page'))
        return data
    elif similarity > 50.0:
        data = {'similarity': similarity, 'access': 'denied', 'text': 'The AI is unsure...'}
    elif similarity > 10.0:
        data = {'similarity': similarity, 'access': 'denied', 'text': 'The AI is confident, that you have no access rights.'}
    else:
        data = {'similarity': similarity, 'access': 'denied', 'text': 'The AI is very confident, that you have no access rights.'}
    return flask.jsonify(data) 
