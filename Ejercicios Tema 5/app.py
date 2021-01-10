from flask import Flask, jsonify
import json
app = Flask(__name__)

@app.route('/')
def home():
	cuidador = json.dumps({"name": "Alan"})
	animal = json.dumps({"name": "Okapi"})
	report = json.dumps({"name": "Report_1", "reporter": "Alan", "animal": "Okapi", "report": "Okapis are fine! They have eaten everything!"})

	return jsonify([cuidador, animal, report]), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
