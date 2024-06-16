import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
from storyprompt import buildPrompt
from dotenv import load_dotenv
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

load_dotenv()

promptBuilder = buildPrompt()
theme = promptBuilder.generateTheme()
name = promptBuilder.generateName()
contentPrompt = promptBuilder.contentPrompt(name, theme)

GEMINI_KEY = os.getenv('api_key')
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

story_list = [contentPrompt]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/story')
def story():
    response = model.generate_content(contentPrompt)
    story_response = response.text
    story_list.append(story_response)
    return render_template('story.html', story=story_response)

@app.route('/continue_story', methods=['POST'])
def continue_story():
    data = request.json
    chosen_option = data['choice']
    new_prompt = f"The user chose option {chosen_option} in {story_list[-1]}. Continue the story based on the option chosen. For reference, here is the entire story so far, along with the original prompt: {story_list}"
    new_response = model.generate_content(new_prompt)
    new_story_response = new_response.text
    story_list.append(new_story_response)
    return jsonify({'new_story': new_story_response})

@app.route('/reset_story', methods=['POST'])
def reset_story():
    global promptBuilder, story_list
    name = promptBuilder.generateName()
    theme = promptBuilder.generateTheme()
    contentPrompt = promptBuilder.contentPrompt(name, theme)
    story_list = [contentPrompt]
    response = model.generate_content(contentPrompt)
    story_response = response.text
    story_list.append(story_response)
    return jsonify({'new_story': story_response})

if __name__ == '__main__':
    socketio.run(app, debug=True)