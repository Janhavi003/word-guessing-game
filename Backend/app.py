from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

WORDS = ["python", "flask", "javascript", "backend", "frontend"]
SECRET_WORD = random.choice(WORDS)

@app.route("/guess", methods=["POST"])
def guess_word():
    data = request.get_json()
    guess = data.get("guess", "").strip().lower()


    if not guess:
        return jsonify({"message": "Please enter a guess."})

    if guess == SECRET_WORD:
        return jsonify({"message": "🎉 Correct! You guessed the word!"})
    else:
        return jsonify({"message": "❌ Wrong guess. Try again!"})

if __name__ == "__main__":
    app.run(debug=True)
