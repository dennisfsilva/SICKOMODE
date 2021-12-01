# waiting signature
from res.controllers.api_standard_service import Api_standard_service

import datetime
import numpy
import random

class Users(Api_standard_service):

	
	def getAll(self):
		"""
		Method that search for recipes
		:param self: object with all information for the search
		:type param: object
		:return: return a array of recipe

		"""


		# run sql var
		sql = "SELECT * FROM Users WHERE user_type = 'common'"
		try:
			self.cursor.execute(sql)
			results = self.cursor.fetchall()

			data = {'results': [], 'nr_results': len(results)}
			for x in results:
				data['results'].append({'id': x[1],'Name': x[2], 'Email': x[3], 'Tele': x[4], 'COVID-Status': x[5],'User_Type': x[6]})


		except:
			data = {'status': 'Error: unable to fecth data'}

		return data



	def getOne(self, user_id):
		
		if self.db_ver('Users', 'id', user_id) == 0:
			return {'status': 404, 'Message': 'User id not found!'}		

		
		if not recipe_id:
			data = {'status': 300, 'Message': 'parameter required [id_recipe]'}
		else:

			data = {}
			sql = "SELECT * FROM Users WHERE id = {}".format(user_id)
			
			try:
				self.cursor.execute(sql)
				recipes = self.cursor.fetchone()

				data = {'User': { 'id': user_id, 'Name': x[2], 'Email': x[3], 'Tele': x[4], 'COVID-Status': x[5],'User_Type': x[6]}}


			except:
				self.db.rollback()

		return data


	def __del__(self):
		"""
		Destroy the class Users

		"""
		print("destroy class Users")
