from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/projects/<path:filename>')
def download_file(filename):
    return send_from_directory('projects', filename)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

@app.route("/file_organizer")
def file_organizer():
    return render_template("file_organizer.html")

if __name__ == "__main__":
    app.run(debug=True)