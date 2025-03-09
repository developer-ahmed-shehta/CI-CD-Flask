from flask import Flask, render_template, request, jsonify
import importlib
import replaceme
import os
app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

# Path to the file to overwrite
UPLOAD_FOLDER = os.getcwd()

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

MODULE_NAME = 'replaceme'
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/goodbye')
def goodbye_world():
    return 'Hi, Ali'

@app.route('/print')
def practice_world():
    return replaceme.printer()

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if file:
        # Save the file to overwrite the existing module file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], MODULE_NAME + '.py')
        file.save(file_path)
        print(file_path)
        # Reload the module to apply changes
        try:
            #import replaceme
            importlib.reload(replaceme)
            return jsonify({"message": "File uploaded and module reloaded successfully."}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "Unknown error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
