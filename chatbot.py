import os
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template

# Initialize the Flask app
app = Flask(__name__)

# Configure the Gemini API key
genai.configure(api_key="AIzaSyDCwNGcwzNFcXZyI9Gl3FEAB4C02uj8sJY")


# Route for the chatbot interface
@app.route("/")
def index():
    return render_template("chat.html")

# Function to generate responses using the Gemini model
def generate_response(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

# Route to handle chat input
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_prompt = data.get("prompt")
    
    if not user_prompt:
        return jsonify({"error": "No prompt provided"}), 400
    
    try:
        # Generate response from the Gemini model
        response_text = generate_response(user_prompt)
        return jsonify({"response": response_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)