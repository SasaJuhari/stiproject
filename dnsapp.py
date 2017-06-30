#!/usr/bin/python 

from flask import Flask, jsonify
from flask import abort, make_response
from flask.ext.httpauth import HTTPBasicAuth 
import json
from flask import request 
import dns

auth =  HTTPBasicAuth()

app = Flask(__name__)

tasks = [
    {

    } 
]

@auth.get_password
def get_password(username):
        if username == 'sasa':
                return 'Password!'
        return None

@auth.error_handler
def unauthorized():
        return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@app.route('/createdns', methods=['POST'])
@auth.login_required
def createdns():
	function = {
		'name' : request.json['name'],
		'eth' : request.json['eth']
	}
	tasks.append(function)
	dns.createdns(function['name'],function['eth'])
        return jsonify({'dns' : dns.readdns()})

@app.route('/readdns', methods=['GET'])
def readdns():
        return jsonify({'dns' : dns.readdns()})

@app.route('/deldns', methods=['POST'])
@auth.login_required
def deldns():
	function = {
		'name' : request.json['name']
	}
	tasks.append(function)
	dns.deldns(function['name'])
	return jsonify({'dns' : dns.readdns()})

@app.route('/updatedns', methods=['POST'])
@auth.login_required
def updatedns():
        function = {
                'name' : request.json['name'],
		'name1' : request.json['name1']	

        }
        tasks.append(function)
        dns.updatedns(function['name'],function['name1'])
        return jsonify({'dns' : dns.readdns()}) 

if __name__ == '__main__':
        app.run(debug=True)

