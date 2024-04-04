#import the Flask micro framework
from flask import Flask, request, render_template
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # This will enable CORS for all domains on all routes.

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-script', methods=['POST'])
def run_script():
    if request.method == 'POST':
        # Assuming you have a script named `your_script.py` in the same directory
        result = subprocess.run(['python', 'your_script.py'], capture_output=True, text=True)
        resultOutput = result.stdout.replace('\\n', '<br>')
        return f"Script Output:<br>{resultOutput}"
    else:
        return 'Method Not Allowed', 405
