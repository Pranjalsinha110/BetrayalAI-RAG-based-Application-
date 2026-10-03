# 🤖 BetrayalAI

### 🎥 Chat With Any YouTube Video Using RAG + AI

<p align="center">

<img src="https://img.shields.io/badge/AI-RAG%20Powered-8A2BE2?style=for-the-badge&logo=openai&logoColor=white"/>
<img src="https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react&logoColor=black"/>
<img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/Python-Backend-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/LangChain-RAG-1C3C3C?style=for-the-badge"/>
<img src="https://img.shields.io/badge/FAISS-Vector%20Search-FF6F00?style=for-the-badge"/>
<img src="https://img.shields.io/badge/HuggingFace-Embeddings-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black"/>

</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=25&duration=3000&pause=1000&color=8A2BE2&center=true&vCenter=true&width=800&lines=Chat+with+YouTube+Videos+%F0%9F%8E%A5;Powered+by+Retrieval+Augmented+Generation+%F0%9F%A7%A0;Ask+Questions.+Get+Context-Aware+Answers.+%E2%9C%A8;Turn+Passive+Watching+into+Interactive+Learning+%F0%9F%9A%80" alt="Typing Animation"/>
</p>

<p align="center">
  <b>Transform any YouTube video into an intelligent conversational knowledge base.</b>
</p>

<p align="center">
  <i>Watch less. Understand more. Ask anything.</i> 🧠✨
</p>

---

# 🌟 What is BetrayalAI?

**BetrayalAI** is an AI-powered **Retrieval-Augmented Generation (RAG)** application that allows users to have a natural conversation with YouTube videos.

Instead of watching an entire video to find one specific piece of information, users can simply provide the **YouTube URL**, ask a question, and receive an intelligent answer based on the video's transcript.

### 💡 The Core Idea

```text
YouTube Video
      ↓
Transcript Extraction
      ↓
Text Processing
      ↓
Chunking
      ↓
Embedding Generation
      ↓
FAISS Vector Database
      ↓
Semantic Retrieval
      ↓
Relevant Context
      ↓
LLM
      ↓
AI Generated Answer
```

> 🚀 BetrayalAI converts a passive video-watching experience into an interactive AI-powered knowledge retrieval system.

---

# 🎯 Why BetrayalAI?

Imagine you're watching a **2-hour programming lecture** and you only want to know:

> 💬 "What is the difference between JWT authentication and session authentication?"

Instead of manually searching through the entire video:

```text
❌ Watch 2 Hours
❌ Search Manually
❌ Skip Through Video
❌ Find the Exact Timestamp
```

BetrayalAI lets you simply ask:

```text
👤 User:
"What is the difference between JWT and session authentication?"

🤖 BetrayalAI:
"According to the video, JWT authentication stores the
authentication information inside a signed token, while
session authentication keeps session information on the server..."
```

⚡ **Relevant information. Immediately.**

---

# ✨ Key Features

<table>
<tr>
<td width="50%">

### 🎥 YouTube Intelligence

Ask questions directly from YouTube videos.

</td>
<td width="50%">

### 🧠 RAG Architecture

Uses Retrieval-Augmented Generation for contextual answers.

</td>
</tr>

<tr>
<td>

### 🔎 Semantic Search

Finds relevant content based on meaning rather than exact keywords.

</td>
<td>

### 🗃️ FAISS Vector Database

Efficient similarity search over generated embeddings.

</td>
</tr>

<tr>
<td>

### 🤖 LLM Powered

Generates natural-language answers from retrieved context.

</td>
<td>

### 💬 Conversational UI

Interact with video content through a chat interface.

</td>
</tr>

<tr>
<td>

### 📚 Learning Assistant

Useful for lectures, tutorials, courses and educational videos.

</td>
<td>

### ⚡ Automated Pipeline

Transcript → Chunks → Embeddings → Retrieval → Answer.

</td>
</tr>
</table>

---

# 🧠 RAG Architecture

BetrayalAI follows a standard **Retrieval-Augmented Generation pipeline**.

```mermaid
flowchart LR

A[🎥 YouTube URL] --> B[📜 Transcript Extraction]

B --> C[✂️ Text Chunking]

C --> D[🧠 Embedding Model]

D --> E[(🗃️ FAISS Vector Database)]

F[❓ User Question] --> G[🔎 Semantic Search]

G --> E

E --> H[📚 Relevant Context]

H --> I[🤖 LLM]

I --> J[💬 Context-Aware Answer]

style A fill:#ff0000,color:#fff
style E fill:#ff9800,color:#fff
style I fill:#8a2be2,color:#fff
style J fill:#00a86b,color:#fff
```

---

# 🔄 Complete Working Pipeline

## 1️⃣ User Provides YouTube URL

```text
https://youtube.com/watch?v=VIDEO_ID
```

The application identifies the requested video and begins the processing pipeline.

⬇️

## 2️⃣ Transcript Extraction

The system retrieves the available transcript using the **YouTube Transcript API**.

```text
YouTube Video
      ↓
Transcript
      ↓
Raw Text
```

⬇️

## 3️⃣ Text Chunking

Long transcripts are divided into smaller meaningful chunks.

```text
Large Transcript
       ↓
 ┌───────────────┐
 │ Chunk 1       │
 ├───────────────┤
 │ Chunk 2       │
 ├───────────────┤
 │ Chunk 3       │
 ├───────────────┤
 │ Chunk 4       │
 └───────────────┘
```

Chunking improves retrieval efficiency and helps the model focus on relevant information.

⬇️

## 4️⃣ Embedding Generation

Each chunk is converted into a numerical vector representation.

```text
Text Chunk
   ↓
Embedding Model
   ↓
Vector Representation
```

These vectors represent the **semantic meaning** of the text.

⬇️

## 5️⃣ FAISS Vector Storage

The generated vectors are stored in a **FAISS vector index**.

```text
Chunk 1 → Vector 1
Chunk 2 → Vector 2
Chunk 3 → Vector 3
Chunk 4 → Vector 4

             ↓

       FAISS Index
```

⬇️

## 6️⃣ User Asks a Question

```text
👤 "What does the speaker say about authentication?"
```

⬇️

## 7️⃣ Semantic Retrieval

The question is converted into an embedding and compared against stored vectors.

```text
Question Vector
      ↓
Similarity Search
      ↓
Top Relevant Chunks
```

⬇️

## 8️⃣ Context Injection

The retrieved chunks are provided to the LLM as contextual information.

```text
Question
   +
Retrieved Context
   ↓
LLM
```

⬇️

## 9️⃣ AI Response

The LLM generates a natural-language answer grounded in the retrieved video content.

```text
🤖 Final Answer
       ↓
💬 Chat Interface
```

---

# 📊 Data Flow Diagram

<p align="center">
  <img src="diagram BetrayalAI/Dfd.jpg" width="850" alt="BetrayalAI Data Flow Diagram"/>
</p>

### 🔍 DFD Explanation

The DFD demonstrates how information flows through the application:

```text
User
 ↓
YouTube URL
 ↓
Transcript Extraction
 ↓
Text Processing
 ↓
Embeddings
 ↓
FAISS
 ↓
Semantic Retrieval
 ↓
Relevant Context
 ↓
LLM
 ↓
Generated Answer
 ↓
User
```

---

# 🔀 Flowchart

<p align="center">
  <img src="diagram BetrayalAI/Flowchart.jpg" width="850" alt="BetrayalAI Flowchart"/>
</p>

---

# 🧩 System Components

| Component                 | Responsibility             |
| ------------------------- | -------------------------- |
| 🎨 React                  | Frontend user interface    |
| ⚡ FastAPI                | Backend API layer          |
| 📜 YouTube Transcript API | Transcript extraction      |
| 🦜 LangChain              | RAG pipeline orchestration |
| 🤗 HuggingFace            | Text embeddings            |
| 🗃️ FAISS                  | Vector similarity search   |
| 🤖 LLM                    | Answer generation          |
| 💬 Chat UI                | User interaction           |

---

# 🛠️ Technology Stack

## 🎨 Frontend

<p>
<img src="https://img.shields.io/badge/React.js-61DAFB?style=flat-square&logo=react&logoColor=black"/>
<img src="https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=bootstrap&logoColor=white"/>
</p>

### Used For

* User interface
* YouTube URL input
* Chat interface
* Message rendering
* Loading states
* API communication
* Responsive design

---

## ⚙️ Backend

<p>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white"/>
</p>

### Used For

* API endpoints
* Transcript processing
* RAG pipeline
* Vector search
* LLM communication
* Request/response handling

---

## 🧠 AI & RAG

<p>
<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square"/>
<img src="https://img.shields.io/badge/FAISS-FF6F00?style=flat-square"/>
<img src="https://img.shields.io/badge/HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=black"/>
</p>

### Technologies

* 🦜 LangChain
* 🗃️ FAISS
* 🤗 HuggingFace Embeddings
* 📺 YouTube Transcript API
* 🤖 Large Language Model

---

# 📂 Project Structure

```text
BetrayalAI/
│
├── 📁 betrayalai/
│   ├── 📁 src/
│   ├── 📄 package.json
│   └── ...
│
├── 📁 python backend/
│   ├── 📄 api.py
│   ├── 📄 requirements.txt
│   └── ...
│
├── 📁 diagram BetrayalAI/
│   ├── 🖼️ Dfd.jpg
│   └── 🖼️ Flowchart.jpg
│
├── 📄 README.md
├── 📄 .gitignore
└── ...
```

---

# 💬 Example Interaction

### 👤 User

```text
What are the main concepts explained in this video?
```

### 🤖 BetrayalAI

```text
The video mainly explains:

1. Retrieval-Augmented Generation
2. Vector embeddings
3. Semantic search
4. FAISS vector databases
5. Context retrieval
6. LLM-based answer generation
```

---

# 🔎 Semantic Search vs Traditional Search

| Traditional Search         | BetrayalAI                    |
| -------------------------- | ----------------------------- |
| 🔤 Keyword based           | 🧠 Meaning based              |
| Exact words matter         | Semantic similarity matters   |
| Manual searching           | Automatic retrieval           |
| Hard to search long videos | Designed for long transcripts |
| Limited context            | Context-aware answers         |

---

# 🧠 Why RAG?

A traditional LLM may not know the specific information contained inside a particular YouTube video.

RAG solves this by providing the model with **relevant external context at query time**.

```text
                 ┌─────────────────┐
                 │   User Query    │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ Semantic Search │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ Relevant Chunks │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │      LLM        │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │  Final Answer   │
                 └─────────────────┘
```

This architecture helps the application generate answers using information retrieved from the specific video.

---
# 🚀 Getting Started

## 📋 Prerequisites

Before running BetrayalAI, make sure you have:

```text
✅ Python 3.x
✅ Node.js
✅ npm
✅ Git
✅ Internet Connection
```

---

# 📥 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Pranjalsinha110/BetrayalAI-RAG-based-Application-.git

cd BetrayalAI
```

---

# 🐍 Backend Setup

Move into the backend directory:

```bash
cd "python backend"
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🎨 Frontend Setup

Open a new terminal:

```bash
cd betrayalai
```

Install dependencies:

```bash
npm install
```

Start the frontend:

```bash
npm start
```

---

# ⚡ Start Backend

Inside the backend directory:

```bash
uvicorn api:app --reload
```

The backend will start in development mode.

---

# 🔐 Environment Variables

If your implementation uses API keys or external LLM providers, create a `.env` file inside the backend directory.

Example:

```env
LLM_API_KEY=your_api_key_here
```

> ⚠️ Never commit secret API keys to GitHub.

Add environment files to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
node_modules/
```

---

# 🔗 Application Flow

```text
┌──────────────────────┐
│      👤 USER         │
└──────────┬───────────┘
           │
           │ YouTube URL
           ↓
┌──────────────────────┐
│   🎨 React Frontend  │
└──────────┬───────────┘
           │
           │ API Request
           ↓
┌──────────────────────┐
│    ⚡ FastAPI        │
└──────────┬───────────┘
           │
           ↓
┌──────────────────────┐
│ 📜 Transcript API    │
└──────────┬───────────┘
           │
           ↓
┌──────────────────────┐
│ ✂️ Text Chunking     │
└──────────┬───────────┘
           │
           ↓
┌──────────────────────┐
│ 🧠 Embeddings        │
└──────────┬───────────┘
           │
           ↓
┌──────────────────────┐
│ 🗃️ FAISS             │
└──────────┬───────────┘
           │
           │ User Question
           ↓
┌──────────────────────┐
│ 🔎 Similarity Search │
└──────────┬───────────┘
           │
           ↓
┌──────────────────────┐
│ 🤖 LLM               │
└──────────┬───────────┘
           │
           ↓
┌──────────────────────┐
│ 💬 Final Answer      │
└──────────────────────┘
```

---

# 📡 API Concept

The backend acts as the bridge between the frontend and AI pipeline.

Typical request flow:

```text
Frontend
   ↓
POST Request
   ↓
FastAPI
   ↓
RAG Pipeline
   ↓
LLM
   ↓
JSON Response
   ↓
Frontend
```

Example conceptual request:

```json
{
  "youtube_url": "https://youtube.com/watch?v=example",
  "question": "What is discussed in this video?"
}
```

Example conceptual response:

```json
{
  "answer": "The video discusses..."
}
```

---

# 📈 Advantages

### ⚡ Faster Information Retrieval

Users can directly ask questions instead of manually searching through long videos.

### 🧠 Context-Aware Answers

Relevant transcript chunks are retrieved before generating the response.

### 🔎 Semantic Understanding

The system searches based on meaning rather than only matching exact words.

### 📚 Educational Use

Useful for:

* Programming tutorials
* Online lectures
* Technical presentations
* Interview preparation
* Educational content
* Research videos
* Conference talks

### 💬 Conversational Experience

Users interact with video content naturally through a chat interface.

---

# ⚠️ Limitations

BetrayalAI currently has several limitations:

* Transcript availability depends on the YouTube video.
* Poor-quality transcripts can reduce answer quality.
* Very long videos may require more processing time.
* Answer quality depends on the embedding model and LLM.
* Ambiguous questions may produce incomplete results.
* Internet connectivity may be required for external services.
* Current architecture is designed around single-video interaction.

---

# 🔮 Future Scope

The project can be expanded significantly.

```text
                    🚀 FUTURE
                       │
       ┌───────────────┼────────────────┐
       ↓               ↓                ↓
   🎥 Multi-Video   🎙️ Voice         🌍 Multi-
      RAG           Interaction       Language
       │               │                │
       ↓               ↓                ↓
   📄 PDF RAG      ⚡ Streaming      👤 User
       │             Responses       Accounts
       ↓               │                ↓
   🌐 Web RAG          ↓             💾 History
                       │
                       ↓
                 📱 Mobile App
```

### Planned Improvements

* 🎥 Multiple YouTube videos
* 📄 PDF document support
* 🌐 Website/document ingestion
* 🎙️ Voice-based interaction
* ⚡ Streaming responses
* 🌍 Multilingual support
* 👤 User authentication
* 💾 Chat history
* 📝 Automatic notes
* 📚 AI-generated summaries
* 🧠 Advanced retrieval strategies
* 📱 Mobile application
* ☁️ Cloud deployment
* 📊 Analytics and usage dashboard

---

# 🧪 Potential Use Cases

| Use Case            | Example                        |
| ------------------- | ------------------------------ |
| 🎓 Education        | Ask questions from lectures    |
| 💻 Programming      | Query coding tutorials         |
| 📚 Research         | Extract information from talks |
| 🧑‍💼 Business         | Analyze presentations          |
| 📝 Revision         | Generate answers from lectures |
| 🎤 Conferences      | Search technical talks         |
| 🎬 Content Analysis | Understand long-form videos    |

---

# 🏗️ RAG Concepts Demonstrated

This project demonstrates several important modern AI engineering concepts:

```text
🧠 Natural Language Processing
        ↓
✂️ Text Chunking
        ↓
🔢 Vector Embeddings
        ↓
🗃️ Vector Databases
        ↓
🔎 Semantic Retrieval
        ↓
📚 Context Injection
        ↓
🤖 Large Language Models
        ↓
✨ Retrieval-Augmented Generation
```

---

# 🎓 What This Project Demonstrates

BetrayalAI is more than a simple chatbot.

It demonstrates practical implementation of:

* ✅ RAG architecture
* ✅ Semantic search
* ✅ Vector embeddings
* ✅ FAISS similarity search
* ✅ LLM integration
* ✅ LangChain workflows
* ✅ API development with FastAPI
* ✅ React frontend development
* ✅ AI-powered information retrieval
* ✅ End-to-end AI application architecture

---

# 🛡️ Error Handling Considerations

A production-ready implementation should handle cases such as:

```text
❌ Invalid YouTube URL
❌ Video does not exist
❌ Transcript unavailable
❌ Transcript extraction failure
❌ Empty user query
❌ API failure
❌ LLM timeout
❌ Vector database failure
❌ Network failure
```

The frontend should provide meaningful feedback rather than exposing raw backend errors.

---

# ⚡ Performance Pipeline

```text
                    USER
                      │
                      ↓
                ┌──────────┐
                │   URL    │
                └────┬─────┘
                     ↓
             Transcript Fetch
                     ↓
               Text Chunking
                     ↓
              Embeddings
                     ↓
              FAISS Index
                     │
                     │
        ┌────────────┘
        │
        ↓
    User Query
        │
        ↓
  Query Embedding
        │
        ↓
 Similarity Search
        │
        ↓
 Relevant Context
        │
        ↓
      LLM
        │
        ↓
   AI Response
```

---

# 🧑‍💻 Development Philosophy

BetrayalAI is built around a simple principle:

> ### "Don't make users search through information. Let them ask the information."

The project combines modern frontend development, backend APIs and generative AI into a single practical application.

---

# 🌟 Project Highlights

```text
╔══════════════════════════════════════════════╗
║                                              ║
║             🤖 BETRAYALAI                    ║
║                                               ║
║       🎥 Talk to YouTube Videos              ║
║                                              ║
║       🧠 Powered by RAG                     ║
║       🔎 Semantic Search                    ║
║       🗃️ FAISS                              ║
║       🤗 HuggingFace                        ║
║       ⚡ FastAPI                            ║
║       ⚛️ React                              ║
║                                              ║
║       Ask → Retrieve → Understand → Answer   ║
║                                              ║
╚══════════════════════════════════════════════╝
```

---

# 🚀 Roadmap

* [x] 🎥 YouTube transcript extraction
* [x] ✂️ Text chunking
* [x] 🧠 Embeddings
* [x] 🗃️ FAISS vector search
* [x] 🤖 LLM integration
* [x] 💬 Chat interface
* [ ] 🎙️ Voice interaction
* [ ] 🌍 Multilingual support
* [ ] 🎥 Multi-video RAG
* [ ] 📄 PDF RAG
* [ ] 🌐 Website RAG
* [ ] 👤 Authentication
* [ ] 💾 Chat history
* [ ] ⚡ Streaming responses
* [ ] 📱 Mobile application
* [ ] ☁️ Production deployment

---

# 🤝 Contributing

Contributions are welcome! 🎉

If you want to improve BetrayalAI:

```bash
# Fork the repository

# Create a feature branch
git checkout -b feature/amazing-feature

# Commit your changes
git commit -m "Add amazing feature"

# Push the branch
git push origin feature/amazing-feature

# Open a Pull Request 🚀
```

---

# 🐛 Bug Reports & Feature Requests

Found a bug?

Have an idea?

Feel free to open an issue and describe:

```text
🐛 Problem
💡 Expected Behaviour
🔎 Actual Behaviour
📸 Screenshots
📝 Additional Information
```

---

# 📜 License

This project is intended for educational and development purposes.

Add your preferred open-source license here if the repository is distributed under one.

Example:

```text
MIT License
```

---

# ⭐ Support the Project

If you find **BetrayalAI** interesting or useful:

<p align="center">

### ⭐ Star the repository

### 🍴 Fork the project

### 🐛 Report bugs

### 💡 Suggest features

### 🤝 Contribute

</p>

Every contribution helps improve the project. 🚀

---

# 🔗 Repository

<p align="center">

<a href="https://github.com/Pranjalsinha110/BetrayalAI-RAG-based-Application-">
  <img src="https://img.shields.io/badge/GitHub-BetrayalAI-181717?style=for-the-badge&logo=github"/>
</a>

</p>

---

# 👨‍💻 Author

<p align="center">

### **Pranjal Sinha**

🤖 AI / RAG Enthusiast
💻 Full-Stack Developer
🧠 Exploring Generative AI & Intelligent Applications

</p>

---

<p align="center">

## 💜 Built with Python, React, RAG & AI

### 🎥 Watch Less. Ask More. Understand Everything.

**BetrayalAI — Turning YouTube Videos into Conversational Knowledge. 🚀**

</p>

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=8A2BE2&height=120&section=footer"/>
</p>
