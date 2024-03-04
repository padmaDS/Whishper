
## This code is for 2 inputs (1 is for url and 1 is for model_name)


import whisper
from flask import Flask, request, jsonify
import urllib.request

app = Flask(__name__)

def vid2text(url, model_name):
    urllib.request.urlretrieve(url, r'C:\Users\PadmavathiMadisetty\Downloads\0703.mp3') 
    print("Download complete")
    model = whisper.load_model(model_name)
    result = model.transcribe(r'C:\Users\PadmavathiMadisetty\Downloads\0703.mp3')
    output = result["text"]
    file_name = model_name + '.txt'

    with open(file_name, 'w') as f:
        f.write(output)
    
    return output

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/gmr2', methods=['POST'])
def gmrapi():
    data = request.json

    if 'text' not in data or 'model_name' not in data:
        return jsonify({'error': "text or model_name field is missing"}), 400

    input_text = data['text']
    model_name = data['model_name']

    out = vid2text(input_text, model_name)
    response_dict = {'output': out}
    
    return jsonify(response_dict)

if __name__ == "__main__":
    app.run(debug=True, host='localhost')
    # app.run(debug=True, host='0.0.0.0')
    # vid2text(url)
