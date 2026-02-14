💼 Job Intelligence System

An end-to-end AI-powered job analytics platform that predicts salaries, enables resume-based insights, provides a Retrieval-Augmented Generation (RAG) chatbot, and visualizes the highest-paying jobs globally — all through an interactive Streamlit web application.

🚀 Features
🔮 Salary Prediction

Predicts annual salary (USD) using a trained machine-learning model

Inputs include:

Resume (PDF upload)

Job title & experience level (auto-extracted)

Employment type

Company size & location

Industry

Remote ratio

Resume parsing is powered by Google Gemini

📄 Resume Intelligence (LLM-Powered)

Automatically extracts structured data from resumes:

Job title

Experience level (EN / MI / SE / EX)

Education level

Years of experience

Number of skills

Uses Gemini 2.5 Flash for fast and accurate document understanding

🤖 RAG AI Chatbot

Ask natural-language questions about:

Job roles

Salaries

Experience trends

Uses:

ChromaDB for vector storage

HuggingFace embeddings

Google Gemini as the LLM

Answers are generated only from retrieved context (no hallucinations)

🌍 Global Highest-Paying Jobs Explorer

Interactive world map visualization

Filter by:

Country

Job title

Displays:

Top-N highest paying jobs

Salary-based geospatial scatter plot

Ranked salary table
