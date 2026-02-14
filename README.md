<div align="center">

# 💼 Job Intelligence System

### AI-Powered Salary Prediction, Resume Intelligence & Global Job Analytics

An end-to-end AI-powered job analytics platform that predicts salaries, enables resume-based insights, provides a Retrieval-Augmented Generation (RAG) chatbot, and visualizes the highest-paying jobs globally — all through an interactive Streamlit web application.

🚀 Predict salaries • Analyze resumes • RAG chatbot • Explore high-paying jobs worldwide

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![LangChain](https://img.shields.io/badge/LangChain-RAG-orange)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-green)
![License](https://img.shields.io/badge/License-MIT-purple)

</div>

---

## ✨ Overview

**Job Intelligence System** is an end-to-end **AI-driven job analytics platform** that combines:

- 📄 **Resume understanding using LLMs**
- 🔮 **Machine learning salary prediction**
- 🤖 **Retrieval-Augmented Generation (RAG) chatbot**
- 🌍 **Interactive global salary visualization**

All delivered through a modern **Streamlit web application**.

---

## 🚀 Key Features

### 🔮 Salary Prediction Engine
- ✔ ML-based annual salary prediction (USD)
- ✔ Resume-driven feature extraction
- ✔ Supports **remote, hybrid & onsite** roles

**Inputs**
- Employment type  
- Company size & location  
- Industry  
- Remote ratio  
- Resume (PDF)

---

### 📄 Resume Intelligence (LLM-Powered)
Automatically extracts structured insights from resumes:
- Job title  
- Experience level (EN / MI / SE / EX)  
- Education level  
- Years of experience  
- Number of skills  

Powered by **Google Gemini 2.5 Flash**.

---

### 🤖 RAG AI Chatbot
Ask natural-language questions such as:
- *“Which jobs pay the most globally?”*
- *“How does experience impact salary?”*

**Tech Stack**
- ChromaDB (Vector Store)
- LangChain
- HuggingFace Embeddings
- Google Gemini LLM

> Responses are generated **only from retrieved context** (no hallucinations).

---

### 🌍 Global Highest-Paying Jobs Explorer
- 🌐 Interactive world map
- 📊 Salary-based bubble visualization
- 🔎 Filter by country & job title
- 📋 Ranked salary table

---

## 🧠 System Architecture

├── ui.py # Streamlit UI & application logic
├── knowledge_builder.py # Vector database builder (RAG)
├── sal_model.ipynb # Salary model training notebook
├── salary_model.pkl # Trained ML model
├── chroma/ # Persistent vector store
└── README.md

## ⚙️ Tech Stack

### 🖥 Frontend
- Streamlit
- Plotly

### 🤖 AI & LLMs
- Google Gemini (Chat & Embeddings)
- LangChain
- ChromaDB
- HuggingFace Sentence Transformers

### 📊 Machine Learning
- Scikit-learn
- Pandas
- NumPy

---
