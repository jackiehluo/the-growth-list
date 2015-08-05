from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('data/startups.json', 'r') as file:
            data = json.loads(file.read())
    return render_template('index.html', **data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')