from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)

# File to store messages (in the same folder as app.py)
file_path = "M2m.txt"

# Simple HTML form
HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Send a Message</title>
</head>
<body>
    <h2>Send a Message</h2>
    <form method="POST" action="/">
        <input type="text" name="name" placeholder="Your name (optional)"><br><br>
        <textarea name="message" placeholder="Type your message..." required></textarea><br><br>
        <button type="submit">Send</button>
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "Anonymous")
        message = request.form.get("message", "")
        time = datetime.now().isoformat()

        # Append message to M2m.txt
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(f"Name: {name}\nMessage: {message}\nTime: {time}\n{'-'*30}\n")

        return "<h3>Message sent successfully!</h3><a href='/'>Send another</a>"

    return render_template_string(HTML_FORM)

if __name__ == "__main__":
    app.run(debug=True)
