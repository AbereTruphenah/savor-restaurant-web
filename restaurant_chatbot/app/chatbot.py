# Remember to finish the dietary options context

import os 
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

# LOad restaurant content
with open("app/context.json", "r") as f:
    context = json.load(f)

def ask_gemini(user_message: str) -> str:
    headers = {"Content-Type": "application/json"}
    params = {"key": API_KEY}

    system_prompt = f"""
You are a friendly and knowledgeable AI assistant for a restaurant called Savor. Answer using the brand tone: {context['brand_tone']}

Restaurant Info:
Name: {context['name']}
Hours: {context['hours']}
Menu: {context['menu']}
Signature Dishes: {context['signature_dishes']}
Location: {context['location']}
Dietary Options: {context['dietary_options']} 
Booking Info: {context['booking_info']}
Contact: {context['contact']}
"""

    body  = {
        "contents": [
            {"role": "user", "parts": [{"text": f"{system_prompt}\nUser: {user_message}"}]}
        ]
    }

    response = requests.post(MODEL_URL, headers=headers, params=params, json=body)
    reply = response.json()["candidates"][0]["content"]["parts"][0]["text"]
    return reply.strip()