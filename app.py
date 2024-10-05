from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Langsmith Imports
from langchain_openai import ChatOpenAI

# GroqCloud Imports
from groq import Groq

# Initialize Flask app
app = Flask(__name__)

# Langsmith API initialization
llm = ChatOpenAI(api_key=os.getenv("LANGCHAIN_API_KEY"))

# GroqCloud API initialization
groq_client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

@app.route('/chat/langsmith', methods=['POST'])
def langsmith_chat():
    user_message = request.json.get('message')

    try:
        response = llm.invoke(user_message)
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

    return jsonify({"response": response})

@app.route('/chat/groqcloud', methods=['POST'])
def groqcloud_chat():
    user_message = request.json.get('message')

    try:
        chat_completion = groq_client.chat.completions.create(
            messages=[{"role": "user", "content": user_message}],
            model="llama3-8b-8192",
        )
        response = chat_completion.choices[0].message.content
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
