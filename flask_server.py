from flask_cors import CORS
from flask import Flask, render_template

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def main():
	return render_template('index.html')

if __name__ == "__main__":
	app.run()