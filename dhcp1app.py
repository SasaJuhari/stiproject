#!/usr/bin/python 

from flask import Flask, jsonify
from flask import abort, make_response
from flask.ext.httpauth import HTTPBasicAuth 
import json
from flask import request 
import dhcp1

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

@app.route('/createdhcp', methods=['POST'])
@auth.login_required
def createdhcp():
	function = {
		'type' : request.json['type']
	}
	tasks.append(function)
	dhcp1.createdhcp(function['type'])
	return jsonify({'dhcp' : dhcp1.readdhcp()})

@app.route('/readdhcp', methods=['GET'])
def readdhcp():
	return jsonify({'dhcp' : dhcp1.readdhcp()})

@app.route('/deldhcp', methods=['POST'])
@auth.login_required
def deldhcp():
	function = {
		'type' : request.json['type']
	}
	tasks.append(function)
	dhcp1.deldhcp(function['type'])
	return jsonify({'dhcp' : dhcp1.readdhcp()})

@app.route('/updatedhcp', methods=['POST'])
@auth.login_required
def updatedhcp():
	function = {
		'type' : request.json['type'],
		'type1' : request.json['type1']
		}	
	tasks.append(function)
	dhcp1.updatedhcp(function['type'],function['type1'])
	return jsonify({'dhcp' : dhcp1.readdhcp()}) 

if __name__ == '__main__':
	app.run(debug=True)
