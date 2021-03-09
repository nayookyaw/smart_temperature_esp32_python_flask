from __main__ import app

from Controller.IndexController import IndexController

class Routes:

	@app.route('/')
	def index():
		return IndexController.index()
		
	@app.route('/save/temperature', methods = ['POST'])
	def save_temperature():
		return IndexController.save_temperature()
