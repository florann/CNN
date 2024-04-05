#import the Flask micro framework
from flask import Flask, request, render_template
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # This will enable CORS for all domains on all routes.
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}) 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-script', methods=['GET'])
def run_script():
    print("Run script")
    if request.method == 'GET':
        result = subprocess.run(['python', '../Pathfinding.py'], capture_output=True, text=True)
        resultOutput = result.stdout.replace('\\n', '<br>')
        return f"Script Output:<br>{resultOutput}"
    else:
        return 'Method Not Allowed', 405
