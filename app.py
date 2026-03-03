
import google.generativeai as genai
import os

# ==============================
# 🔑 SET YOUR API KEY HERE
# ==============================

API_KEY = "AIzaSyDdKzItbDSh70ELyk54Qm0v3DWg3VzCXWU" 

genai.configure(api_key=API_KEY)

# Choose model
model = genai.GenerativeModel("gemini-2.5-flash")

# ==============================
# 🪔 Siddha Assistant Function
# ==============================

def ask_siddha(question):
    prompt = f"""
You are a Siddha Medical Professor teaching B.S.M.S students.

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

Question:
{question}
"""

    response = model.generate_content(prompt)
    return response.text


# ==============================
# 🧠 Interactive Console Chat
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