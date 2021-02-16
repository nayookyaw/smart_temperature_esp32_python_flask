from flask import render_template, request, jsonify
import random, string, datetime

from __main__ import db
from Models.Images import Images


class IndexController:

	def index():
		data = {
			'page' : 'index'
		}
		return render_template('/views/index.html', data = data)
	
	def upload_page():
		data = {
			'page' : 'upload_page'
		}
		return render_template('/views/upload.html', data = data)
	
	def get_total_images_count():
		data = request.get_json('data')

		return jsonify({ "success" : 'count' })