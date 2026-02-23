# RAG AI TEACHING ASSISTANT -PROJECT

# ML Teaching Assistant (RAG-Based)

An intelligent **Machine Learning Teaching Assistant** built using **Retrieval Augmented Generation (RAG)** that answers ML questions from a curated playlist of machine learning playlist videos by KRISH NAIK.

The system converts lecture videos into structured knowledge and allows users to interact with that knowledge through a conversational Streamlit interface.

---

## Project Overview

This project transforms Machine Learning lecture videos into a searchable knowledge base and enables students to ask conceptual and implementation-related questions.

Instead of relying on generic LLM knowledge, the assistant retrieves relevant lecture content and generates context-aware answers grounded in the playlist material.

The goal is to simulate a **personal ML tutor** that explains topics exactly as taught in the lectures.

---

## How It Works

The pipeline follows a Retrieval Augmented Generation workflow:

1. **Video Processing**
   - Lecture videos are converted to audio
   - Audio is transcribed into structured JSON format

2. **Text Chunking & Cleaning**
   - Transcripts are cleaned and split into semantic chunks
   - Chunks are merged and preprocessed for retrieval

3. **Embedding Generation**
   - Each chunk is converted into vector embeddings
   - Embeddings are stored locally for fast similarity search

4. **Question Answering**
   - User question → converted to embedding
   - Relevant transcript chunks retrieved
   - LLM generates answer grounded in retrieved context

5. **Interactive UI**
   - Streamlit chat interface
   - Persistent conversation history
   - Teaching-assistant style responses

---

## Key Features

Playlist-aware ML question answering  
Concept explanation from lecture context  
Retrieval-based grounded responses  
Chat-style teaching assistant interface  
Modular preprocessing pipeline  
Lightweight local vector retrieval  
Streamlit-based interactive UI  

---

## Project Structure
app.py # Streamlit chat interface
process_incoming.py # Question processing + retrieval pipeline
video_to_mp3.py # Video → audio conversion
mp3_to_json.py # Audio transcription to JSON
preprocess_json.py # Transcript cleaning
merge_chunks.py # Chunk merging
prompt.txt # Teaching assistant prompt
response.txt # Generated response storage
embeddings.joblib # Vector embedding store

---

## Example Use Cases

* Understanding regression algorithms
* Clarifying lecture intuition
* Revising ML interview concepts
* Learning implementation details from playlist
* Rapid doubt solving while studying

---

## Running the App

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Future Improvements

Multi-playlist support
Lecture timestamp navigation
Replace the LLAMA3.2 MODEL TO  OPEN AI API MODEL -LATEST MODEL FOR BETTER ACCURACY

VIKAS KUMAR