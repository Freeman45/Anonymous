from flask import Flask, request, render_template_string, session, redirect, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey123"  # needed for session

file_path = "M2m.txt"

# HTML templates
LOGIN_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Login</title>
<style>
body {
    font-family: Arial, sans-serif;
    background: url('https://effective-gold-2f6nrnwang.edgeone.app/20251231_212639.png') no-repeat center center fixed;
    background-size: cover;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}
.container {
    background: rgba(255,255,255,0.9);
    padding: 25px 30px;
    border-radius: 12px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.25);
    width: 100%;
    max-width: 400px;
    text-align: center;
}
h2 { margin-bottom: 15px; }
.warning { color: red; font-weight: bold; margin-bottom: 20px; }
input { width: 100%; padding: 12px; margin: 10px 0; border-radius: 8px; border: 1px solid #ccc; font-size: 14px; }
button { width: 100%; padding: 12px; border: none; border-radius: 8px; background: #2575fc; color: white; font-size: 16px; cursor: pointer; transition: 0.3s; }
button:hover { background: #6a11cb; }
</style>
</head>
<body>
<div class="container">
<h2>Welcome</h2>
<div class="warning">Sa'eed won't know your name!</div>
<form method="POST">
    <input type="text" name="name" placeholder="Enter your name to proceed" required>
    <button type="submit">Login</button>
</form>
</div>
</body>
</html>
"""

MESSAGE_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Send a Message</title>
<style>
body {
    font-family: Arial, sans-serif;
    background: url('https://effective-gold-2f6nrnwang.edgeone.app/20251231_212639.png') no-repeat center center fixed;
    background-size: cover;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}
.container {
    background: rgba(255,255,255,0.9);
    padding: 25px 30px;
    border-radius: 12px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.25);
    width: 100%;
    max-width: 400px;
    text-align: center;
}
h2 { margin-bottom: 15px; }
.success { color: green; font-weight: bold; margin-bottom: 20px; }
input, textarea { width: 100%; padding: 12px; margin: 10px 0; border-radius: 8px; border: 1px solid #ccc; font-size: 14px; resize: vertical; }
textarea { min-height: 120px; }
button { width: 100%; padding: 12px; border: none; border-radius: 8px; background: #2575fc; color: white; font-size: 16px; cursor: pointer; transition: 0.3s; }
button:hover { background: #6a11cb; }
</style>
</head>
<body>
<div class="container">
<h2>Send an Anonymous Message</h2>
{% if success %}
<div class="success">Message sent successfully!</div>
{% endif %}
<form method="POST">
    <textarea name="message" placeholder="Type your message..." required></textarea>
    <button type="submit">Send</button>
</form>
</div>
</body>
</html>
"""

# Routes
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session['name'] = request.form['name'].strip()
        return redirect(url_for("message"))
    return render_template_string(LOGIN_PAGE)

@app.route("/message", methods=["GET", "POST"])
def message():
    if 'name' not in session:
        return redirect(url_for("login"))

    success = False
    if request.method == "POST":
        message_text = request.form['message'].strip()
        name = session['name']
        time = datetime.now().isoformat()
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(f"Name: {name}\nMessage: {message_text}\nTime: {time}\n{'-'*30}\n")
        success = True

    return render_template_string(MESSAGE_PAGE, success=success)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
