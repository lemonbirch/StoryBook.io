import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify, url_for 
from storyprompt import buildPrompt
from dotenv import load_dotenv
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

load_dotenv()

story_list = []


GEMINI_KEY = os.getenv('api_key')
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')




@app.route('/')
def index():
    return render_template('index.html')



@app.route('/storychoicebuilder', methods=['GET'])
def storychoicebuilder():
    return render_template('storychoicebuilder.html')


@app.route('/story')
def story():
    global story_list, promptBuilder, user_input, name, theme 
    # prompt_name = []
    user_input = None
    promptBuilder = buildPrompt()
    theme = promptBuilder.generateTheme()
    name = promptBuilder.generateName()
    contentPrompt = promptBuilder.contentPrompt(user_input, name, theme)
    print("this test isnt for zakiquaky")
    story_list = (contentPrompt)
    #reset story list
    # story_list = [] 
    if request.method == 'GET':
        character_name = request.args.get('character_name')
        story_theme = request.args.get('story_theme')
        user_input = f"{character_name} and {story_theme}"
        print(f"get {user_input}")
    elif request.method == 'POST':
        ucharacter_name = request.args.get('character_name')
        story_theme = request.args.get('story_theme')
        user_input = f"{character_name} and {story_theme}"
        print(f"Post {user_input}")
    else:
        user_input = None
    promptBuilder = buildPrompt()
    theme = promptBuilder.generateTheme()
    name = promptBuilder.generateName()
    contentPrompt = promptBuilder.contentPrompt(user_input, name, theme)
    response = model.generate_content(contentPrompt)
    story_response = response.text
    story_list.append(story_response)
    #story_response = reformat_story(story_list)
    #story_response = reformat_story(story_list)
    return render_template('story.html', story=story_response)


   

@app.route('/continue_story', methods=['POST'])
def continue_story():
    global story_list, promptBuilder
    print("this test is for zackiqacky taki")
    print(story_list)

    data = request.json
    chosen_option = data['choice']
    new_prompt = f"The user chose option {chosen_option} in {story_list[-1]}. Continue the story based on the option chosen. For reference, here is the entire story so far, along with the original prompt: {story_list}"
    new_response = model.generate_content(new_prompt)
    new_story_response = new_response.text
    story_list.append(new_story_response)
    #new_story_response = reformat_story(story_list)
    return jsonify({'new_story': new_story_response})

@app.route('/reset_story', methods=['POST'])
def reset_story():
    global promptBuilder, story_list, user_input, name, theme
    # name = promptBuilder.generateName()
    # theme = promptBuilder.generateTheme()
    contentPrompt = promptBuilder.contentPrompt(user_input, name, theme)
    story_list = [contentPrompt]
    response = model.generate_content(contentPrompt)
    story_response = response.text
    story_list.append(story_response)
    #story_response = reformat_story(story_list)
    return jsonify({'new_story': story_response})

def reformat_story(story_list):
    # add catches so the code doesnt break the website
    story_list_splice = str(story_list[len(story_list) -1])
    page_number = len(story_list)
    story_list_splice = story_list_splice.split("**")
    print(f"this is the splices list {story_list_splice}")
    story_list_story = story_list_splice[2]
    story_list_choices = story_list_splice[4]
    reformated_story = f"Page: {page_number}\n{story_list_story}\n\n\nChoices:\n{story_list_choices}"
    return reformated_story
if __name__ == '__main__':
    socketio.run(app, debug=True)