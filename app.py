#We need to import some flask package features
from flask import Flask, render_template, request, redirect, url_for
#Create a Flask app 
app = Flask(__name__)

#Create an empty array to store mood history, it will be reseted if app restarts
mood_history = []

#This is a decorator, it changes behavior of function that is defined just below this.
#In this case, we tell python that the function who follows the decoratore needs to be executed when user open '/' path (home page)
@app.route('/')
def index():
    #render_tempalte will generate a page using html specified html file
    #it is also passing mood_history as 'history' variable in html, so we can show mood history
    return render_template('index.html', history=mood_history)

@app.route('/submit', methods=['POST'])
def submit():
    #when we define a form with the POST method in HTML, the submited data is inside a reques.form
    #.get('mood') tells that we wand to get the value of 'mood' which is the 'name' of our selection in HTML
    mood = request.form.get('mood')
    comment = request.form.get('comment')
    #simply checks if mood and comment variable is not null
    from datetime import datetime
    timestamp = datetime.now().strftime('%Y-%m-%D %H:%M:%S')
    if mood is not None and comment is not None:
        mood_history.append(f"{mood} - {timestamp} - {comment}")
    elif mood:
        mood_history.append(f"{mood} - {timestamp}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
    ##app.run(host='0.0.0.0', port=5000, debug=True) -> for running on all addresses

