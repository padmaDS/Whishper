import whisper
import urllib.request

def vid2text(url):
    urllib.request.urlretrieve(url, 'video30.mp4') 
    print("Download complete")
    model = whisper.load_model("small.en")
    result = model.transcribe('video30.mp4')
    output = result["text"]
    # file_name = str(url) + '.txt'

    with open('output.txt', 'w') as f:
        f.write(output)
    return output

if __name__ == "__main__":
    # Example URL, replace it with the actual URL you want to process
    example_url = 'https://quadz.blob.core.windows.net/newpoc/harvard.wav'
    
    # Call vid2text with the desired URL
    output_text = vid2text(example_url)
    
    print("Output Text:", output_text)
