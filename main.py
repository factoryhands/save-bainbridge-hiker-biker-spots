from flask import Flask, render_template, jsonify, request, redirect, url_for
import openai
import os

openai.api_key = os.environ['OPEN_AI_KEY']

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/generate', methods=['GET', 'POST'])
def generate_text():
  response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=
    "Write two paragraphs compelling a park's employee to bring back the hiker biker spots at Fay Bainbridge Park that were made non-reservable sites open to motorists. Do not start with a greeting. Do not end with a closing.",
    max_tokens=350)
  generated_text = response.choices[0].text.strip()

  return jsonify({'text': generated_text})


app.run(host='0.0.0.0', port=81)
