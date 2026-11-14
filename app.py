from flask import Flask
import time

app = Flask(__name__)
@app.route("/")
def home():
	return "Hello from my auto-scaling app!"

@app.route("/health")
def health():
	return {"status": "ok"}

@app.route("/load")
def load():
	end = time.time() + 5
	while time.time() < end:
	  pass
	return "Work hard for 5 seconds"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
