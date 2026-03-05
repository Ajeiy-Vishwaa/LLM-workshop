import streamlit as st
import google.generativeai as genai
import os

# ==============================
# API KEY
# ==============================

API_KEY = os.getenv("GEMINI_API_KEY")   # safer than hardcoding
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# ==============================
# Streamlit Page Setup
# ==============================

st.set_page_config(page_title="SiddhaGPT", page_icon="🪔")

st.title("🪔 SiddhaGPT – Siddha Medical Study Assistant")
st.write("Ask questions related to Siddha medicine.")

# ==============================
# Conversation Memory
# ==============================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ==============================
# Ask Siddha Function
# ==============================

def ask_siddha(question):

    history_text = ""
    for q, a in st.session_state.chat_history:
        history_text += f"User: {q}\nAssistant: {a}\n"

    prompt = f"""
Strict Rules:
- Answer ONLY based on Siddha medicine principles.
- Use traditional Siddha terminology (Vatha, Pitha, Kabam, Mukkutram).
- Provide structured format:
    1. Definition
    2. Key Concepts
    3. Classification
    4. Symptoms
    5. Short Notes for Exams
- Do NOT provide modern allopathic treatments.
- Educational purpose only.
- If question is unrelated to Siddha medicine, politely refuse.

Conversation History:
{history_text}

Question:
{question}
"""

    response = model.generate_content(prompt)
    return response.text


# ==============================
# User Input
# ==============================

user_question = st.text_input("Ask your Siddha question")

if st.button("Ask"):

    if user_question:

        answer = ask_siddha(user_question)

        st.session_state.chat_history.append((user_question, answer))

        st.subheader("📘 Siddha Answer")
        st.write(answer)

# ==============================
# Show Chat History
# ==============================

if st.session_state.chat_history:
    st.subheader("💬 Conversation History")

    for q, a in reversed(st.session_state.chat_history):
        st.write("**You:**", q)
        st.write("**SiddhaGPT:**", a)
        st.write("---")
