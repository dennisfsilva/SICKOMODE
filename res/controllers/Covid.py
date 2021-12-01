from res.controllers.api_standard_service import Api_standard_service

class Covid(Api_standard_service):

	def update(self, user_id, status):
		"""

		status -> covid situation if 1 the user has covid if 0 the user dont

		"""	
		if not user_id:
			return {'status': 300, 'Message': 'parameter required [user_id]'}

		if self.db_ver('Users', 'id', user_id):
			return {'status': 404, 'Message': 'User id not found!'}

		sql = "UPDATE Users SET covid = {} WHERE id = {}".format(status, user_id)

		try:
			self.cursor.execute(sql)
			self.db.commit()

		except:
			self.db.rollback()
			return {'status': 'ERROR', 'Message':'couldnt not satisfy request'}

		return {'status':200, 'Message':'successful updated'}
