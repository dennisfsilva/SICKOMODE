

class Api_standard_service:
	
	def __init__(self, db, user_id = 0, args = []):
                """
                Contructor for this object

                :param db: variable object of database
                :param userId: user id
                :param args: arguments of condition in the search
                :type db: string
                :type userId: string
                :type args: string

                """

                self.db = db
                self.cursor = db.cursor(buffered=True)

                self.user_id = int(user_id)
                self.args = args



	def db_ver(self, table, field, value):
		try:
			sql = "SELECT * FROM {} WHERE {} = '{}' ".format(table, field, value)
			self.cursor.execute(sql)
			
			return self.cursor.rowcount

		except:
			self.db.rollback()

		return -1

	def checkParam(self, param):
		if type(param) is str:
			if param in self.args: return True
			else: return False	
		else:	
			for x in param:
				if x not in self.args:
					return False

			return True

		return 'varibale type {} not supported'.format(type(param))	
