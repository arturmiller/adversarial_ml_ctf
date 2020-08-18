import base64
from io import BytesIO

from flask import Flask, render_template, request, jsonify
from PIL import Image

from app import app, model


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    image = decode_image(data['image'])
    similarity = model.check_similarity(image)
    response = create_response(similarity)
    return response


def decode_image(data):
    starter = data.find(',')
    image_data = bytes(data[starter+1:], encoding="ascii")
    image = Image.open(BytesIO(base64.b64decode(image_data))).convert('RGB')
    return image


def create_response(similarity):
    if similarity > 80.0:
        data = {'similarity': similarity, 'access': 'granted', 'text': 'You have been successfully authenticated! Hello Mr. Goldfish.'}
    elif similarity > 50.0:
        data = {'similarity': similarity, 'access': 'denied', 'text': 'The AI is unsure...'}
    elif similarity > 10.0:
        data = {'similarity': similarity, 'access': 'denied', 'text': 'The AI is confident, that you have no access rights.'}
    else:
        data = {'similarity': similarity, 'access': 'denied', 'text': 'The AI is very confident, that you have no access rights.'}
    return jsonify(data) 
