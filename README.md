# BetrayalAI (RAG Based Application)
## 📌 Description

This project is an AI-powered Question Answering system built using a Retrieval-Augmented Generation (RAG) pipeline that enables users to interact with any YouTube video in a conversational manner.

Users can simply provide a YouTube video URL, and the system automatically extracts the transcript, processes it into meaningful chunks, and stores semantic embeddings in a vector database. When a user asks a question, the system retrieves the most relevant context from the video content and generates accurate, context-aware answers using a Large Language Model (LLM).

The application is designed with a chat-based interface, allowing users to have a natural conversation with video content instead of passively watching it. This makes it highly useful for learning, revision, research, and content summarization.

The project demonstrates the practical implementation of modern AI concepts such as semantic search, embeddings, vector databases (FAISS), and LLM integration, making it a strong real-world example of building intelligent applications using RAG architecture.

# 📊 Architecture / Flowchart
## Data Flow Diagram (DFD)

The Data Flow Diagram (DFD) illustrates how data moves through the system, starting from user input to the final generated response. It shows the process of extracting video transcripts, converting them into embeddings, and storing them in a vector database. When a query is asked, relevant information is retrieved and passed to the LLM for answer generation. This diagram helps in understanding the internal workflow and data processing steps of the RAG-based system.

<p align="center">
  <img src="diagram BetrayalAI/Dfd.jpg" width="600"/>
</p>

## 🔄 Flowchart

The flowchart represents the step-by-step working of the system, starting from user input of a YouTube URL and query. It shows how the transcript is extracted, processed into chunks, and converted into embeddings. These embeddings are stored in a vector database for efficient retrieval. Finally, the system fetches relevant context and generates an accurate response using an LLM.

<p align="center">
  <img src="diagram BetrayalAI/Flowchart.jpg" width="600"/>
</p>

## 🚀Features
1. Ask questions from any YouTube video
2. Uses transcript extraction
3. Vector database for semantic search
4. LLM generates accurate answers
5. Chat-like UI

## 🧠 How It Works :--
```bash
=> The user provides a YouTube video URL.
=> The system extracts the transcript from the video.
=> The transcript is divided into smaller text chunks for efficient processing.
=> Embeddings are generated for each text chunk using an embedding model.
=> The embeddings are stored in a FAISS vector database.
=> When the user asks a question, the system retrieves the most relevant chunks based on semantic similarity.
=> The retrieved context is passed to the Large Language Model (LLM) to generate an accurate and context-aware responsei
```
## 🛠️ Tech Stack

### Frontend

* React.js
* Bootstrap 

### Backend

* Python
*  FastAPI

### AI & RAG Technologies

* LangChain
* FAISS Vector Database
* HuggingFace Embeddings
* YouTube Transcript API

### Other Tools

* Git & GitHub
* VS Code

## 📂 Project Structure
```bash
BetrayalAI/
│── betrayalai/        # Frontend
│── python backend/    # Backend
│── Diagrams           # diagrams
│── README.md
│── .gitignore
```

## ⚙️ Installation

### Clone the Repository

```bash id="18t2sw"
git clone https://github.com/Pranjalsinha110/BetrayalAI-RAG-based-Application-.git
cd BetrayalAI
```

### Backend Setup

```bash id="l9w8eo"
cd "python backend"

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Frontend Setup

```bash id="jlwmrf"
cd betrayalai

# Install dependencies
npm install

# Start the frontend server
npm start
```

### Run the Backend Server

```bash id="0m7j85"
python youtube.py
```


