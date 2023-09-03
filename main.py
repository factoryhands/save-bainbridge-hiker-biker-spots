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
    engine="text-davinci-003",
    prompt=
    "Write a kind but firm one paragraph statement requesting that the spots designated for hikers, bikers, and kayakers be restored at Fay Bainbridge Park. Do not include a greeting or begin the paragraph like a letter.",
    max_tokens=350)
  generated_text = response.choices[0].text.strip()

  return jsonify({'text': generated_text})


app.run(host='0.0.0.0', port=8080)
