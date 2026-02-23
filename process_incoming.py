import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity  
import numpy as np
import joblib
import requests


def format_time(seconds):
    seconds = int(seconds)
    mins= seconds//60
    secs= seconds % 60
    return f"{mins:02d}:{secs:02d}"

def create_embedding(text_list):
    r= requests.post("http://localhost:11434/api/embed",json={
        "model": "bge-m3",
        "input":text_list
    })

    return r.json()['embeddings']

def inference(prompt):
    r= requests.post("http://localhost:11434/api/generate",json={
        "model": "llama3.2:1b",
        "prompt":prompt,
        "stream":False  
    })

    return r.json()["response"]

df=joblib.load('embeddings.joblib')

def ask_question(incoming_query):
    question_embedding= create_embedding([incoming_query])[0]
    similarities= cosine_similarity(np.vstack(df['embedding']),[question_embedding]).flatten()
    top_results=5
    max_index= similarities.argsort()[::-1][0:top_results]
    new_df=df.loc[max_index]
    #TimeStamp
    new_df["start"] = new_df["start"].apply(format_time)
    new_df["end"] = new_df["end"].apply(format_time)

    prompt = f'''
I am teaching Machine Learning from my ML course.
 Here are subtitle chunks with timestamps in mm:ss:
{new_df[["title","start","end","text"]].to_json(orient="records")}

Answer the question using ONLY these chunks.
Mention video title and timestamp.

Question: {incoming_query}
'''

    response = inference(prompt)

    with open("response.txt", "w", encoding="utf-8") as f:
        f.write(response)

    return response

# for index ,item in new_df.iterrows():
#     print(index,item["title"],item["text"],item["start"],item["end"])
#find similarities of question embedding with other embeddings 
# print(np.vstack(df['embedding'].values))
# print(np.vstack(df['embedding']).shape)

# print(similarities)

# print(max_index)cls
# print(new_df[["title","text"]])