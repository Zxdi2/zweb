
from flask import Flask, request, render_template,send_from_directory,make_response

app = Flask(__name__)


@app.route("/")
def flask_main():

    return "<center><h1>hi 🥰 </h1></center>"


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)