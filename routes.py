from __main__ import app

from Controller.IndexController import IndexController

class Routes:

	@app.route('/')
	def index():
		return IndexController.index()
	
	@app.route('/get/temperature', methods = ['GET'])
	def get_temperature():
		return IndexController.getTemperature()

	@app.route('/save/temperature', methods = ['POST'])
	def save_temperature():
		return IndexController.saveTemperature()
