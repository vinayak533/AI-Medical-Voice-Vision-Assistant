# 🧠 AI Medical Voice & Vision Assistant

## 📌 Summary
This project is an AI-powered medical assistant that allows users to interact with an AI doctor using voice and medical images. The system converts patient speech into text, analyzes uploaded medical images using a Vision AI model, and generates a doctor-like response which is then converted into speech.

The goal of this project is to simulate a virtual medical consultation experience using AI technologies.

---

## 🛠️ Technologies Used

Python  
Gradio (Web Interface)  
Groq Whisper (Speech-to-Text)  
Vision LLM (LLaMA Vision Model)  
ElevenLabs Text-to-Speech  
dotenv (Environment Variables)  
Object-Oriented Programming (OOP)  
Modular Python Architecture  

---

## ✨ Features

Voice input from patient  
Speech-to-Text conversion using Whisper  
Medical image analysis using Vision AI  
AI-generated doctor responses  
Doctor voice response using Text-to-Speech  
Interactive Gradio web interface  
Real-time AI interaction  
Modular and scalable project structure  

---

## ⚙️ Process

1. User records their medical question using the microphone  
2. User uploads a medical image (for example a skin condition)  
3. Speech is converted into text using Whisper STT  
4. The image and patient query are sent to the Vision AI model  
5. The AI generates a doctor-like response  
6. The response is converted into voice using ElevenLabs  
7. The result is displayed in the interactive interface  

---

## 🏗️ How I Built It

- Designed a modular AI assistant architecture
- Implemented speech-to-text pipeline using Groq Whisper
- Integrated Vision AI for medical image analysis
- Generated natural language responses using an LLM
- Converted AI responses to speech using ElevenLabs
- Built an interactive UI using Gradio
- Structured the project into modular Python components

---

## 📚 What I Learned

- Building AI-powered assistants
- Speech-to-Text system integration
- Vision AI model usage
- Prompt engineering for AI responses
- Text-to-Speech generation
- Designing modular AI systems
- Building interactive AI applications with Gradio

---

## 🚀 How It Could Be Improved

- Add conversation memory
- Support multiple medical image types
- Improve medical reasoning using fine-tuned models
- Add patient chat history
- Integrate real medical datasets
- Deploy as a cloud AI service
- Add authentication and user accounts

---

## ▶️ How to Run the Project


### Create Virtual Environment

python -m venv venv  
venv\Scripts\activate

---

### Install Dependencies

pip install -r requirements.txt

---

### Add Environment Variables (.env)

GROQ_API_KEY=your_api_key_here  
ELEVENLABS_API_KEY=your_api_key_here

---

### Run the Application

python app.py

---

## 📂 Project Structure

AI-Medical-Voice-Vision-Assistant/

app.py                        # Main Gradio application  
brain_of_the_doctor.py       # Vision AI medical analysis  
voice_of_the_patient.py      # Speech-to-text processing  
voice_of_the_doctor.py       # Text-to-speech generation  

requirements.txt  
.env  
README.md  

---

## ⭐ About

An AI-powered medical assistant that analyzes medical images and voice queries to provide health insights using Vision AI, Speech Recognition, and Text-to-Speech.

---

## 👨‍💻 Author

Vinayak K V
