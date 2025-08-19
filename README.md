

```markdown
# 🔮 AI Astrologer

AI Astrologer is a fun, interactive web application that combines traditional astrology with modern AI.  
It determines your zodiac sign from your birth details, shares fun facts about your sign, and lets you ask **one free question** to an AI-powered astrologer.

---

## ✨ Features
- Collects user details: **Name, Date of Birth, Time of Birth, Place of Birth**.  
- Calculates **Zodiac Sign** using rule-based astrology logic.  
- Generates **fun facts** about your zodiac sign with the help of AI.  
- Allows you to ask **one free astrology-related question** to the AI Astrologer.  
- Built with **Python + Streamlit** and integrated with **OpenRouter API**.

---

## 📂 Project Structure

```

AI-Astrologer/
│── app.py             # Main Streamlit application
│── requirements.txt   # Python dependencies
│── README.md          # Project documentation
│── .env.example       # Environment variable template

````

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/AI-Astrologer.git
cd AI-Astrologer
````

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
```

Activate it:

* **Windows**:

  ```bash
  venv\Scripts\activate
  ```
* **Mac/Linux**:

  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up API Key

1. Copy `.env.example` → `.env`
2. Get your free API key from [OpenRouter](https://openrouter.ai/)
3. Open `.env` and paste your key:

   ```
   OPENROUTER_API_KEY=sk-your-key-here
   ```

### 5. Run the Application

```bash
streamlit run app.py
```

You’ll see a local URL like:

```
http://localhost:8501
```

Open it in your browser to use the app.

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** (for UI)
* **OpenRouter API** (for AI responses)
* **Dotenv** (for environment variable management)

---

## 🎥 Demo Deliverables

* **Codebase (this repo)** with clean structure.
* **Demo Video (2–3 minutes)** showing:

  * Entering birth details
  * Getting zodiac sign
  * Viewing fun facts
  * Asking AI astrologer one question

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License**.

---

✨ *Built with love using Streamlit, Python, and OpenRouter AI.*

```
