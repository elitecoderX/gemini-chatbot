# 🤖 Streamlit Gemini Chatbot

This is a **Chatbot** built using **Streamlit** and **Google Gemini API**. It provides AI-powered responses based on user queries.

## 🌟 Features
- ✅ **Authentication:** Users must enter a secret code to access the chatbot.
- 🤖 **Google Gemini API Integration:** Uses **Gemini** to generate responses.
- 🎨 **Clean & Modern UI:** Uses Streamlit’s built-in chat interface.

---

## 🚀 Installation & Setup
### **1️⃣ Clone the Repository**
```sh
    git clone https://github.com/yourusername/gemini-chatbot.git
    cd gemini-chatbot
```

### **2️⃣ Install Dependencies Using Pipenv**
```sh
    pipenv install  # Install dependencies
    pipenv shell  # Activate virtual environment
```

### **3️⃣ Add Your API Key and Secret Code**
#### **Create `.streamlit/secrets.toml` and add:**
```toml
    API_KEY = "your_gemini_api_key_here"
    SECRET_CODE = "your_secret_password"
```
#### **Get Your Gemini API Key Here:**
[Google AI Studio](https://aistudio.google.com/) → Generate API Key

### **4️⃣ Run the Chatbot**
```sh
    streamlit run app.py
```

---

## 🔧 How It Works
1️⃣ **Authentication** → Users enter a secret code before accessing the chatbot.  
2️⃣ **User Query** → The chatbot sends the query to Gemini API.  
3️⃣ **Gemini API Response** → Provides AI-generated responses based on the query.  

---

## 📌 To-Do & Future Improvements
- 🔹 Implement **Retrieval-Augmented Generation (RAG)** with PDF processing.
- 🔹 Add **Vector Database (FAISS)** for better document retrieval.
- 🔹 Enhance **UI/UX** with custom styling.
- 🔹 Add **multi-user authentication** with Streamlit login.

---

## ❤️ Contribute
Want to improve this chatbot? Feel free to fork and submit a PR! 🚀
