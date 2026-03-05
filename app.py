
import google.generativeai as genai
import os

# ==============================
# 🔑 SET YOUR API KEY HERE
# ==============================

API_KEY = "Replace your api key"

genai.configure(api_key=API_KEY)

# Choose model
model = genai.GenerativeModel(
    "gemini-2.5-flash",
    system_instruction="""
You are SiddhaGPT – a Siddha medical study assistant.

Strict Rules:
- Answer ONLY based on Siddha medicine principles.
- Use traditional Siddha terminology (Vatha, Pitha, Kabam, Mukkutram).
- Provide structured format:
    1. Definition
    2. Key Concepts
    3. Classification (if applicable)
    4. Symptoms (if disease-related)
    5. Short Notes for Exams
- Do NOT provide modern allopathic treatments.
- Educational purpose only.
- If question is unrelated to Siddha medicine, politely refuse.
"""
)

# ==============================
# 🧠 Start Chat Session (Memory)
# ==============================

chat = model.start_chat(history=[])

# ==============================
# 🪔 Siddha Assistant Function
# ==============================

def ask_siddha(question):
    response = chat.send_message(question)
    return response.text


# ==============================
# 💬 Interactive Console Chat
# ==============================

def main():
    print("\n🪔 SiddhaGPT – Siddha Medical Study Assistant")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("Ask Siddha Question: ")

        if user_input.lower() == "exit":
            print("Good luck with your studies! 📚")
            break

        answer = ask_siddha(user_input)

        print("\n📘 Siddha Answer:\n")
        print(answer)
        print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    main()
