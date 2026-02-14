<div align="center">
💼 Job Intelligence System
An end-to-end AI-powered job analytics platform that predicts salaries, enables resume-based insights, provides a Retrieval-Augmented Generation (RAG) chatbot, and visualizes the highest-paying jobs globally — all through an interactive Streamlit web application.
</div>
✨ Overview

The Job Intelligence System is an end-to-end AI-driven analytics platform that combines:

📄 Resume understanding using LLMs

🔮 Machine learning salary prediction

🤖 Retrieval-Augmented Generation (RAG) chatbot

🌍 Interactive global salary visualization

All delivered through a modern Streamlit interface.

🚀 Key Features
🔮 Salary Prediction Engine

✔ ML-based annual salary prediction (USD)
✔ Resume-driven feature extraction
✔ Supports remote, hybrid & onsite roles

Inputs

Employment type

Company size & location

Industry

Remote ratio

Resume (PDF)

📄 Resume Intelligence (LLM-Powered)

⚡ Automatically extracts structured insights:

Job title

Experience level (EN / MI / SE / EX)

Education level

Years of experience

Skill count

🧠 Powered by Google Gemini 2.5 Flash

🤖 RAG AI Chatbot

Ask natural questions like:

“What jobs pay the most in Germany?”
“How does experience affect salary?”

Architecture

🔹 ChromaDB (Vector Store)

🔹 LangChain

🔹 HuggingFace Embeddings

🔹 Gemini LLM

🛡️ Answers are generated only from retrieved context

🌍 Global Highest-Paying Jobs Explorer

📌 Interactive world map
📌 Salary-based bubble visualization
📌 Country & job-title filtering
📌 Ranked salary table

🧠 System Architecture
├── ui.py                   # Streamlit UI + App Logic
├── knowledge_builder.py    # RAG Vector DB Builder
├── sal_model.ipynb         # Salary Model Training
├── salary_model.pkl        # Trained Regression Model
├── chroma/                 # Persistent Vector Store
└── README.md

⚙️ Tech Stack
🖥️ Frontend

Streamlit

Plotly

🤖 AI & LLMs

Google Gemini (Chat + Embeddings)

LangChain

ChromaDB

HuggingFace Sentence Transformers

📊 Machine Learning

Scikit-learn

Pandas

NumPy
