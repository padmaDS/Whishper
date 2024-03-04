import whisper

model = whisper.load_model("base")
result = model.transcribe("video30.mp4", FP32 = False)
print(result)
# print(result["text"])