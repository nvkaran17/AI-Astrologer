import streamlit as st
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

# Load API key
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Function to calculate zodiac sign (rule-based)
def get_zodiac_sign(day, month):
    zodiac_signs = [
        ("Capricorn", (12, 22), (1, 19)),
        ("Aquarius", (1, 20), (2, 18)),
        ("Pisces", (2, 19), (3, 20)),
        ("Aries", (3, 21), (4, 19)),
        ("Taurus", (4, 20), (5, 20)),
        ("Gemini", (5, 21), (6, 20)),
        ("Cancer", (6, 21), (7, 22)),
        ("Leo", (7, 23), (8, 22)),
        ("Virgo", (8, 23), (9, 22)),
        ("Libra", (9, 23), (10, 22)),
        ("Scorpio", (10, 23), (11, 21)),
        ("Sagittarius", (11, 22), (12, 21))
    ]
    for sign, start, end in zodiac_signs:
        if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
            return sign
    return "Unknown"

# Function to call OpenRouter API
def ask_openrouter(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.text}"

# ------------------ UI ------------------
st.title("🔮 AI Astrologer")

st.sidebar.header("Enter Your Birth Details")
name = st.sidebar.text_input("Name")
dob = st.sidebar.date_input("Date of Birth")
time_of_birth = st.sidebar.text_input("Time of Birth (HH:MM)")
place_of_birth = st.sidebar.text_input("Place of Birth")

if name and dob and time_of_birth and place_of_birth:
    zodiac = get_zodiac_sign(dob.day, dob.month)
    st.subheader(f"✨ Hello {name}, your Zodiac Sign is **{zodiac}**")

    # Fun Facts (AI-generated)
    if st.button("Get Fun Facts about your Zodiac"):
        fun_fact_prompt = f"Give me 3 fun and interesting astrology facts about the zodiac sign {zodiac}."
        facts = ask_openrouter(fun_fact_prompt)
        st.success(facts)

    # Ask AI Section (only 1 free question)
    if "asked" not in st.session_state:
        st.session_state.asked = False

    if not st.session_state.asked:
        st.subheader("💡 Ask the AI Astrologer (One Free Question)")
        user_question = st.text_input("Type your question here...")
        if st.button("Ask AI"):
            if user_question.strip() != "":
                ai_prompt = f"The user {name}, born on {dob} at {time_of_birth} in {place_of_birth}, with zodiac sign {zodiac}, asks: {user_question}. Please provide an astrology-based answer."
                answer = ask_openrouter(ai_prompt)
                st.info(answer)
                st.session_state.asked = True
    else:
        st.warning("❌ You have already asked your free question.")
