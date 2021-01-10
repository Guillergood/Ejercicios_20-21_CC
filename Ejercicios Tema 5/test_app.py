from flask import Flask
import json
import pytest

from app1 import define_routes

# Comprueba que existe el report_1
def test_one_report():
    app = Flask(__name__)
    define_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    
    # Asegurar el código recibido es OK
    assert response.status_code == 200
    
    data = response.get_data()
    all_entries = json.loads(data)
    reports = json.loads(all_entries[2]);
    # Asegurar que Report_1 existe
    assert 'Report_1' in [reports['name']]
    
# Comprueba que inserta un nuevo cuidador
def test_new_cuidador():
	app = Flask(__name__)
	define_routes(app)
	client = app.test_client()
	url = '/insert/cuidador'
	
	new_cuidador = {
		'name': 'David'
	}
	
	response = client.post(url, data = json.dumps(new_cuidador))
	assert response.status_code == 200
