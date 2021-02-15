from __main__ import app

from Controller.IndexController import IndexController

class Routes:

	@app.route('/')
	def index():
		return IndexController.index()
	
	@app.route('/upload')
	def upload_page():
		return IndexController.upload_page()
	
	@app.route('/upload/image', methods= ['POST'])
	def upload_image():
		return IndexController.upload_image()