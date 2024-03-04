
## this code is for single input


import whisper
import flask
from flask import Flask, request, jsonify
import urllib
import urllib.request

app = Flask(__name__)

def vid2text(url):
    urllib.request.urlretrieve(url, 'video30.mp4') 
    print("Download complete")
    model = whisper.load_model("base")
    result = model.transcribe('video30.mp4')
    output=result["text"]
    file_name=str(url)+'.txt'
    
    with open('output.txt','w') as f:
        f.write(output)
    return output



# def kkk():
#     import requests
#     import urllib.request 
#     urllib.request.urlretrieve(url_link, video_name.mp4) 

#     return


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/gmr', methods=['POST'])
def gmrapi():

    data = request.json
    #print("this is gmr function")
    # response_gmr = gmr()
    # return response_gmr

    if 'text' not in data:
        return jsonify({'error': "text field is missing"}), 400

    input_text =  data['text']

    out =vid2text(input_text)
    #print(input_text)
    response_dict = {'output': out}
    return jsonify(response_dict)

if __name__ == "__main__":
    app.run(debug=True,host='localhost')
    # app.run(debug=True,host='0.0.0.0')
    # vid2text(url)

