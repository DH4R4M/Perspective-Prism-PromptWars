import os
import json
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# We will initialize the Gemini client inside the route to prevent 
# the server from crashing on startup if the API key isn't set yet.
client = None
try:
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        client = genai.Client(api_key=api_key)
except Exception as e:
    print(f"Warning: Gemini client failed to initialize: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_status():
    global client
    data = request.json
    venue_status = data.get('status', '')

    if not venue_status:
        return jsonify({"error": "No status provided."}), 400

    try:
        # Re-initialize client if it was not created on startup
        if client is None:
            load_dotenv(override=True)
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                return jsonify({"error": "Missing or invalid GEMINI_API_KEY. Please add your key to the .env file and verify it is correct."}), 500
            try:
                client = genai.Client(api_key=api_key)
            except Exception:
                return jsonify({"error": "Missing or invalid GEMINI_API_KEY. Please add your key to the .env file and verify it is correct."}), 500

        # Prompt for the Prism multi-persona logic
        prompt = (f"You are the 'Stadium Sentry', an AI system that analyzes physical "
                  f"event experiences from multiple perspectives (Prism logic). "
                  f"Analyze the following venue status: '{venue_status}'\n\n"
                  f"Provide a JSON response with exactly four keys: 'Security', 'Fan', 'Manager', and 'Severity'. "
                  f"For the three perspective keys, provide a concise perspective (2-3 sentences) on what this status means "
                  f"for that specific persona, and what actions might be needed or how they feel. "
                  f"For 'Severity', provide an integer from 1 to 10 evaluating the overall urgency of the situation (1=Minor Info, 10=Life-Threatening Emergency). "
                  f"Output ONLY valid JSON, nothing else.")

        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json"
            )
        )

        # Parse the JSON response
        result = json.loads(response.text)
        return jsonify(result)

    except Exception as e:
        print(f"Error during GenAI call: {e}")
        return jsonify({"error": f"Error communicating with Gemini: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
