from flask import Flask
import subprocess
from datetime import datetime
import os
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system information
    name = "Atharva Narkhede"  # Replace with your full name
    username = os.getenv("USER", "atharva-narkhede")  # Fetch the system username

    # Convert current UTC time to IST
    utc_time = datetime.utcnow()
    ist_timezone = pytz.timezone('Asia/Kolkata')
    server_time = utc_time.replace(tzinfo=pytz.utc).astimezone(ist_timezone).strftime("%Y-%m-%d %H:%M:%S IST")

    # Execute `top` command and capture output
    top_output = subprocess.check_output("top -bn1", shell=True).decode("utf-8")

    # Format the output for the webpage
    return f"""
    <html>
        <head><title>HTop Output</title></head>
        <body>
            <h1>Name: {name}</h1>
            <h2>User: {username}</h2>
            <h3>Server Time (IST): {server_time}</h3>
            <pre>{top_output}</pre>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
