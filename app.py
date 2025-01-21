from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Function to detect a fruit based on a description
def detect_fruit(description):
    prompt = f"Identify the fruit based on this description: {description}. Provide the most likely fruit name."
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an assistant that specializes in identifying fruits."},
            {"role": "user", "content": prompt}
        ]
    )
    
    fruit_name = response['choices'][0]['message']['content'].strip()
    return fruit_name

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect():
    data = request.json
    description = data.get("description", "")
    fruit_name = detect_fruit(description)
    return jsonify({"fruit": fruit_name})

if __name__ == "__main__":
    app.run(debug=True)
