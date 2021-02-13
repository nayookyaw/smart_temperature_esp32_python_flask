from flask import render_template

class IndexController:
	def index():
		data = {
			'page' : 'index'
		}
		return render_template('/views/index.html', data = data)
