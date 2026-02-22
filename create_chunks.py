import whisper
import json
import os

model=whisper.load_model("base")

audios=os.listdir("audios")

os.makedirs("json", exist_ok=True)
for audio in audios:
    if not audio.endswith((".mp3",".wav",".m4a")):
        continue
    title= os.path.splitext(audio)[0].split("-")[0].strip()
    json_path=f"json/{audio}.json"

    if os.path.exists(json_path):
        print(F"Skipping already processed:{title}")
        continue

    print(f"Processing:{audio}")

    result= model.transcribe(audio=f"audios/{audio}",
                            task="translate",
                            word_timestamps=False,
                            fp16=False)

    chunks = []
    for segment in result["segments"]:
        chunks.append({
            "title":title,
            "start": segment["start"],
            "end": segment["end"],
            "text": segment["text"]
        })

    chunks_with_metadata={"chunks":chunks,"text": result["text"]}

    with open(json_path,"w",encoding="utf-8") as f:
        json.dump(chunks_with_metadata,f,indent=2)