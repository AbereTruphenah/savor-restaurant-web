
# 🍽️ Savor Chatbot Backend

A FastAPI-powered AI chatbot for **Savor**, a modern restaurant. This chatbot responds to user questions about our opening hours, menu, booking process, dietary needs, and more — in a warm and charming brand voice — using **Gemini AI**.

---

## 🔗 Live Demo

- **Chatbot API**: https://savor-chatbot-backend.onrender.com/chat  
- **Frontend Site**:   
- **Docs (Swagger UI)**: https://savor-chatbot-backend.onrender.com/docs

---

## 🎯 Features

- ✅ FastAPI backend with `/chat` POST endpoint
- ✅ Integrated with Gemini AI (Gemini Pro)
- ✅ Context-rich prompt using detailed restaurant info
- ✅ Input validation, error handling, and fallback messaging
- ✅ Secure `.env`-based credential management
- ✅ CORS enabled for frontend communication
- ✅ Docker containerized backend
- ✅ Deployed publicly via Render

---

## 📁 Project Structure

```
restaurant_chatbot/
├── app/
│   ├── main.py           # FastAPI app
│   └── context.json      # Restaurant context data
├── requirements.txt
├── Dockerfile
├── .env (not tracked)
└── README.md
```

---

## 📩 How to Use the API

### Endpoint

```
POST /chat
```

### Request Body (JSON)

```json
{
  "question": "What time do you open?"
}
```

### Response (JSON)

```json
{
  "response": "Savor is open daily from 7 AM to 11 PM. We’d love to welcome you!"
}
```

---

## 🧪 Postman Testing

Here are 3 example Postman requests used to test the `/chat` endpoint:

### ✅ Test 1: Opening Hours

**Request**
```json
POST /chat
{ "question": "What are your opening hours?" }
```

**Response**
```json
{ "response": "We're open from 7 AM to 11 PM every day!" }
```

---

### ✅ Test 2: Signature Dishes

```json
POST /chat
{ "question": "What's your most recommended dish?" }
```

**Response**
```json
{ "response": "You have to try our Teff-Crusted Chicken Strips with Awaze Aioli!" }
```

---

### ⚠️ Test 3: Empty Input

```json
POST /chat
{ "question": "" }
```

**Response**
```json
{ "response": "Sorry, I couldn't generate a response at the moment." }
```

---

## 🔐 Environment Variables

**.env**
```
GEMINI_API_KEY=your_actual_gemini_key
```

Make sure `.env` is listed in your `.gitignore` and **never pushed to GitHub**.

---

## 🐳 Docker Setup

### Build the container

```bash
docker build -t savor-chatbot-backend .
```

### Run the container

```bash
docker run -p 8000:8000 --env-file .env savor-chatbot-backend
```

The app will be live at: `http://localhost:8000`

---

## 🌍 Deployment

- Render was used to deploy the backend from the `restaurant_chatbot/` subfolder.
- Dockerfile path: `restaurant_chatbot/Dockerfile`
- Build context: `restaurant_chatbot`
- Secrets are managed via Render’s Environment tab.

---

## 🔧 Tech Stack

- FastAPI
- Gemini AI (Google)
- Python 3.11+
- Docker
- Postman
- Vercel (frontend)
- Render (backend)

---

## 💬 Chatbot Context Sources

Restaurant data was loaded from a structured JSON file:

- `context.json` includes:
  - Opening hours
  - Full menu
  - Signature dishes
  - Dietary accommodations
  - Location and booking info
  - Contact details
  - Brand tone

---

## 📌 Submission Checklist

✅ All 6 required questions supported  
✅ Brand-specific Gemini responses  
✅ Docker container builds & runs  
✅ Backend deployed on Render  
✅ Live site connected via fetch()  
✅ Postman tests documented  
✅ API key hidden using `.env`  
✅ GitHub repo with clear commits

---

## 🧠 Author

**Raymond Odhiambo**  
Savor Restaurant Chatbot – Built with care and flavor 🌿✨
