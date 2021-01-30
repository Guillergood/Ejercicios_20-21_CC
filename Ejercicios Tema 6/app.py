from flask import Flask, jsonify, request
import json
app = Flask(__name__)

def define_routes(app):
	@app.route('/')
	def home():
		cuidador = json.dumps({"name": "Alan"})
		animal = json.dumps({"name": "Okapi"})
		report = json.dumps({"name": "Report_1", "reporter": "Alan", "animal": "Okapi", "report": "Okapis are fine! They have eaten everything!"})

		return jsonify([cuidador, animal, report]), 200
		
	@app.route('/insert/cuidador', methods=['POST'])
	def insert_cuidador():
		data_string = request.get_data()
		data = json.loads(data_string)
		
		cuidador_name = data.get('name')


		if cuidador_name:
			return 'Ok', 200
		else:
			return 'Error', 400
		
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
