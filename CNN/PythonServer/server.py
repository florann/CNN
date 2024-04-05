#import the Flask micro framework
from flask import Flask, request, render_template, make_response, jsonify 
from flask_cors import CORS, cross_origin
import subprocess

app = Flask(__name__)

CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-script', methods=['GET'])
def run_script():
    print("Run script")
    if request.method == 'GET':
        result = subprocess.run(['python', '../Pathfinding.py'], capture_output=True, text=True)
        resultOutput = result.stdout.replace('\\n', '<br>')
        response = make_response(jsonify(resultOutput))

        return response
    else:
        return 'Method Not Allowed', 405

