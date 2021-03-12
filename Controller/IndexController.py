from flask import render_template, request, jsonify
import random, string, datetime, json

# from __main__ import db
# from Models.Images import Images

class IndexController:

	def index():
		data = {
			'page' : 'index'
		}
		return render_template('/views/index.html', data = data)
	
	def getTemperature():
		with open('temperature.json', 'r') as fp:
			data = json.load(fp)

		return jsonify({ "response" : data })
	def saveTemperature():
		data = request.get_json('data')
		print (data)

		with open('temperature.json', 'w') as fp:
			json.dump(data, fp)

		return jsonify({ "success" : 'saved temperature' })