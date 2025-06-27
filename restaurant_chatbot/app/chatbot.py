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
You are a friendly and knowledgeable AI assistant for a restaurant called Savor. Answer using the brand tone: {context["brand_tone"]}

Restaurant Info:
Name: {context["Savor"]}
Hours: {context["7am - 11pm", "Everyday"]}
Menu: {context[
    "Breakfast": "Egg Whites and Veggies, Avocado Toast, Brioche Toast with Jam and Butter, Cinnamon Brioche French Toast"
    "Main Dishes": "Pepper steak with mushroom sauce, Grilled vegetable and pasta bowl, Grilled chicken plate, Avocado and chickpea sandwich"
    "Desserts": "Carrot cake, Custard cake, Chocolate cake, Macroons"
    "Drinks": "Red house wine, Citrus vodka spritz, Fresh mango-ginger juice, Iced hibiscus tea(homemade)"
]}
Signature Dishes: {context[
    "Teff-Crusted Chicken Strips with Awaze Aioli",
    "Creamy spinach macaroni bowl",
    "Combo bowl",
    "Spaghetti gomen pesto",
    "Honey-balsamic Glazed Lamb Skewers",
    "Spinach Mac and cheese bake",
    "Fire-roasted veggie flatbread",
    "Tuna and chickpea bowl",
    "Combo 2"
]}
Location: {context["Bole Atlas - behind 2000 Habesha"]}
Dietary Options: {context[""]} 
Booking Info: {context["In the case of wanting to reserve a spot, contact us at '+251 9000000'"]}
Contact: {context[
    "Phone number": '+251 9000000'
    "Instagram": 'savorrestaurant'
    "Facebook": 'savorrestaurant'
    "Twitter" : 'savorrestaurant'
    "YouTube" : 'savorrestaurant'
]}
"""

    body  = {
        "contents": [
            {"role": "user", "parts": [{"text": f"{system_prompt}\nUser: {user_message}"}]}
        ]
    }

    response = requests.post(MODEL_URL, headers=headers, params=params, json=body)
    reply = response.json()["candidates"][0]["content"]["parts"][0]["text"]
    return reply.strip()