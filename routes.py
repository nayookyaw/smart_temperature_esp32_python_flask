from __main__ import app

from Controller.IndexController import IndexController

class Routes:

	@app.route('/')
	def index():
		return IndexController.index()