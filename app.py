from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import random
import os

# Set template folder to current directory
app = Flask(__name__, template_folder=os.path.dirname(os.path.abspath(__file__)))

# Route to serve CSS from main folder
@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), filename)

quotes = [
    {"author": "Linus Torvalds", "quote": "Talk is cheap. Show me the code."},
    {"author": "Steve Jobs", "quote": "The only way to do great work is to love what you do."},
    {"author": "Sam Levenson", "quote": "Don’t watch the clock; do what it does. Keep going."},
    {"author": "Theodore Roosevelt", "quote": "Believe you can and you’re halfway there."},
    {"author": "Steve Jobs", "quote": "Your time is limited, so don’t waste it living someone else’s life."},
    {"author": "Confucius", "quote": "It does not matter how slowly you go as long as you do not stop."},
    {"author": "Walt Disney", "quote": "The way to get started is to quit talking and begin doing."},
    {"author": "Nelson Mandela", "quote": "It always seems impossible until it’s done."}
]

@app.route("/")
def home():
    quote = random.choice(quotes)
    return render_template("index.html", quote=quote, quotes=quotes)

@app.route("/add", methods=["POST"])
def add_quote():
    author = request.form.get("author")
    quote_text = request.form.get("quote")
    if author and quote_text:
        quotes.append({"author": author, "quote": quote_text})
    return redirect(url_for("home"))

@app.route("/delete/<int:index>", methods=["POST"])
def delete_quote(index):
    if 0 <= index < len(quotes):
        quotes.pop(index)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
