from flask import Flask, request, render_template_string
import os
from datetime import datetime

app = Flask(__name__)

# Folder and file setup
folder = "Anon"
file_path = os.path.join(folder, "M2m.txt")
os.makedirs(folder, exist_ok=True)

# Simple HTML form
HTML_FORM = """
<form method="POST" action="/">
  <input type="text" name="name" placeholder="Your name (optional)">
  <textarea name="message" placeholder="Type your message..." required></textarea>
  <button type="submit">Send</button>
</form>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "Anonymous")
        message = request.form.get("message", "")
        time = datetime.now().isoformat()

        # Append message to file
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(f"Name: {name}\nMessage: {message}\nTime: {time}\n{'-'*20}\n")

        return "Message sent successfully! <a href='/'>Send another</a>"

    return render_template_string(HTML_FORM)

if __name__ == "__main__":
    app.run(debug=True)
