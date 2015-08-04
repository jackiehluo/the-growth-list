from flask import Flask, render_template
import config
import json

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index():
    with open('data/startups.json', 'r') as file:
            data = json.loads(file.read())
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=config.DEBUG, host=config.HOST)