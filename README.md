# Chatbots Using LLM

A collection of terminal-based chatbots built using modern Large Language Model (LLM) APIs.
This project explores how conversational AI systems work under the hood by implementing chatbot logic, memory management, and streaming responses using Python.

The goal of this project was to understand **LLM interaction patterns**, **API usage**, and **conversation state handling** without relying on heavy frameworks.

---

## 🚀 Features

* Terminal-based conversational chatbot
* Integration with multiple LLM providers
* Persistent conversation memory
* Streaming responses for real-time output
* Command handling for chatbot control
* Modular architecture for easy extension

---

## 🧠 Concepts Explored

This project focuses on core LLM engineering concepts such as:

* Large Language Model APIs
* Prompt Engineering
* Conversation State Management
* Streaming Responses
* Persistent Memory Storage
* Error Handling with API responses
* Environment Variable Security

---

## 🛠 Tech Stack

* **Python**
* **Groq API**
* **Google Gemini API**
* **dotenv**
* **JSON for memory storage**

---

## 📂 Project Structure

```
ChatbotsUsingLLM/
│
├── gemini_chatbot/
│   ├── main.py
│   ├── file.py
│   ├── config.json
│   └── memory.json
│
├── groq_chatbot/
│   ├── main.py
│   ├── file.py
│   ├── config.json
│   └── memory.json
│
├── .env
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/palakgupta5412/ChatbotsUsingLLM.git
cd ChatbotsUsingLLM
```

### 2️⃣ Install dependencies

```
pip install groq python-dotenv
```

### 3️⃣ Configure environment variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key
GEMINI_API_KEY=your_api_key
```

---

## ▶️ Running the Chatbot

```
python main.py
```

---

## 💬 Supported Commands

```
/clear  → clear conversation memory
/help   → show available commands
/exit   → exit chatbot
```

---

## 🧩 How It Works

1. User enters input in the terminal.
2. Conversation history is stored in a JSON file.
3. The LLM API receives the conversation context.
4. The model generates a response.
5. Response is streamed back to the user in real time.
6. The conversation is saved for future interactions.

---

## 📌 Key Learning Outcomes

* Understanding LLM API integration
* Managing conversation state
* Implementing persistent memory
* Streaming responses from LLMs
* Secure handling of API keys

---

## 🔮 Future Improvements

* Web interface using React
* Voice-enabled chatbot
* Integration with databases
* Tool-calling capabilities

---

## 👩‍💻 Author

**Palak Gupta**
B.Tech IT | AI and MERN Enthusiast
