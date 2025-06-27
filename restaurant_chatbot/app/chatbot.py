import os 
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
print("Loaded API Key:", "✔️" if API_KEY else "❌ MISSING!")

MODEL_URL = "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent"


# LOad restaurant content
with open("app/context.json", "r") as f:
    context = json.load(f)

def ask_gemini(user_message: str) -> str:
    headers = {"Content-Type": "application/json"}
    params = {"key": API_KEY}

    menu = "\n".join(f"- {item}" for item in context["menu"])
    signature_dishes = "\n".join(f"- {item}" for item in context["signature_dishes"])

    system_prompt = f"""
You are a friendly and knowledgeable AI assistant for a restaurant called Savor.Use emojis to make the response friendly. Answer using the brand tone: {context['brand_tone']}

Restaurant Info:
Name: {context['name']}
Hours: {context['hours']}
Menu: \n{menu}
Signature Dishes: \n{signature_dishes}
Location: {context['location']}
Dietary Options: {context['dietary_options']} 
Booking Info: {context['booking_info']}
Contact: {context['contact']}
"""

    body  = {
        "contents": [
            {
                "role": "user",
                 "parts": [{"text": f"{system_prompt}\nUser: {user_message}"}]
            }
        ]
    }

    try:
        response = requests.post(MODEL_URL, headers=headers, params=params, json=body)
        response.raise_for_status()
        return response.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
    except Exception as e:
        print("Gemini API Error:", e)
        print("Response text:", response.text)
        return "Sorry, I couldn't generate a response at the moment."