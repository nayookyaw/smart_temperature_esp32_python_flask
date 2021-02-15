from flask import render_template, request, jsonify
import boto3, botocore
import random, string, datetime

from __main__ import db
from Models.Images import Images

from aws import AWS

class IndexController:
	s3 = boto3.client(
		"s3",
		aws_access_key_id = AWS.S3_KEY,
		aws_secret_access_key = AWS.S3_SECRET_ACCESS_KEY
	)

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
	
	def upload_image():
		# try:
			imagefile = request.files.get('file', '')

			# generate random string for file name
			letters = string.ascii_lowercase
			letters = ''.join(random.choice(letters) for i in range(30))
			now = datetime.datetime.now()
			now = now.strftime("%Y-%m-%d-%H-%M-%S")

			folder_name = "revolution-images/"
			file_name = now + letters

			# save data into database
			image = Images(
				name = file_name,
				uuid = file_name,
				created_at = now
			)

			db.session.add(image)
			db.session.commit()

			res_data = Images.query.filter_by(name=file_name).first()
			print (imagefile.content_type)

			acl="public-read"
			content_type = "image/jpeg"
			
			indexController = IndexController()
			indexController.s3.upload_fileobj(
				imagefile,
				AWS.S3_BUCKET,
				folder_name + file_name,
				ExtraArgs = {
						"ACL": acl,
						"ContentType": content_type
				}
			)

			return jsonify({ "result" : "warrr success" })
		# except Error as e:
		# 		print (e)
		# 		return jsonify({ "result" : "Error occurs" })

