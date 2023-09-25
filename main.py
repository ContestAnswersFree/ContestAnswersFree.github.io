from flask import Flask, redirect

app = Flask(__name__)


@app.route("/")
def process_redirect():
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ", code=302)


if __name__ == '__main__':
    app.run(debug=True)
