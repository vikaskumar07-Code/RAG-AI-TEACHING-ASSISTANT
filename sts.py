import whisper
import json

model=whisper.load_model("base")
result= model.transcribe(audio="audios/Mean Sqaured Error, Mean Absolute Error And RMSE In Hindi- Linear Regression ｜ Krish Naik Hindi.mp3",
                         task="translate",
                         word_timestamps=False,
                          fp16=False)

print(result["segments"])

chunks = []
for segment in result["segments"]:
    chunks.append({
        "start": segment["start"],
        "end": segment["end"],
        "text": segment["text"]
    })

with open("output.json","w",encoding="utf-8") as f:
    json.dump(chunks,f,indent=2)