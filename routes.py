from __main__ import app

from Controller.IndexController import IndexController
from Controller.UploadController import UploadController

class Routes:

	@app.route('/')
	def index():
		return IndexController.index()
	
	@app.route('/about')
	def about():
		return IndexController.about()
	
	@app.route('/get/total/images/count', methods = ['POST'])
	def total_images_count():
		return IndexController.get_total_images_count()
	
	@app.route('/upload')
	def upload_page():
		return IndexController.upload_page()
	
	@app.route('/upload/image', methods= ['POST'])
	def upload_image():
		return UploadController.upload_image()