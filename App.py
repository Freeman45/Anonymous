from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)

# File to store messages
file_path = "M2m.txt"

# Modern mobile-friendly HTML form
HTML_FORM = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Send a Message</title>
<style>
    body {
        font-family: Arial, sans-serif;
        background: linear-gradient(to right, #6a11cb, #2575fc);
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
    }
    .container {
        background: white;
        padding: 25px 30px;
        border-radius: 12px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.25);
        width: 100%;
        max-width: 400px;
    }
    h2 {
        text-align: center;
        color: #333;
        margin-bottom: 20px;
    }
    input, textarea {
        width: 100%;
        padding: 12px;
        margin: 10px 0;
        border-radius: 8px;
        border: 1px solid #ccc;
        font-size: 14px;
        resize: vertical;
    }
    button {
        width: 100%;
        padding: 12px;
        border: none;
        border-radius: 8px;
        background: #2575fc;
        color: white;
        font-size: 16px;
        cursor: pointer;
        transition: 0.3s;
    }
    button:hover {
        background: #6a11cb;
    }
    .success {
        text-align: center;
        color: green;
        font-weight: bold;
        margin-bottom: 15px;
    }
</style>
</head>
<body>
<div class="container">
    <h2>Send a Message</h2>
    {% if success %}
    <div class="success">Message sent successfully!</div>
    {% endif %}
    <form method="POST" action="/">
        <input type="text" name="name" placeholder="Your name (optional)">
        <textarea name="message" placeholder="Type your message..." required></textarea>
        <button type="submit">Send</button>
    </form>
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    success = False
    if request.method == "POST":
        name = request.form.get("name", "Anonymous")
        message = request.form.get("message", "")
        time = datetime.now().isoformat()

        # Append message to file
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(f"Name: {name}\nMessage: {message}\nTime: {time}\n{'-'*30}\n")

        success = True

    return render_template_string(HTML_FORM, success=success)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
