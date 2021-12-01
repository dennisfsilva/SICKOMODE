import datetime

import shortuuid
from werkzeug.security import generate_password_hash, check_password_hash

# Auth Managment
class Auth:
	
	

	def __init__(self, db, email = '', password = '', name = '', tele = '', user_type = 'common', covid = 0 ):
		"""
			Constructor of this object
			:param name: user name
			:param email: user email
			:param db: variable object of database
			:type name: string
			:type email: string
		"""
		self.name = name
		self.email = email
		self.password = password
		self.user_type = user_type
		self.tele = tele
		self.covid = covid

		self.db = db
		self.cursor = db.cursor()


	def cUser(self):
		"""
		Creat and insert a new user in database

		:param self: object with all information about the new user
		:param key: the apikey for this user
		:type self: object
		:type key: string
		:return 200: if was insert with success
		:return 201: if wasn't insert with success
		"""
		
		hashed_password = generate_password_hash(self.password, method='sha256')

		sql = "INSERT INTO Users(name,email,password,tele,covid,created_at,api_key,user_type)VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(self.name, self.email,hashed_password,tele,covid,datetime.date.today(),str(shortuuid.uuid()), self.user_type)
		
		try:
			self.cursor.execute(sql)
			self.db.commit()
			
			return 200
		except:
			self.db.rollback()
			
		return 201
		
	def get_by_pi(self, public_id):
		sql = "SELECT * FROM Users WHERE api_key = '{}'".format(public_id)
		
		try:
			self.cursor.execute(sql)
			r = self.cursor.fetchone()

			return {'user_id': r[0], 'name': [1], 'email': r[2], 'user_type': r[8]}
		
		except:
			self.db.rollback()

		return 201


	def get_user(self):
		sql = "SELECT * FROM Users WHERE email = '{}'".format(self.email)

		try:
			self.cursor.execute(sql)
			r = self.cursor.fetchone()
			
			return {'password':r[3], 'name':r[1], 'public_id': r[5], 'user_type': r[8]}

		except:
			self.db.rollback()
	
		return 201

	def check_password(self, password):
		if check_password_hash(password, self.password): return True
		else: return False

	def __del__(self):
		"""
		destoy this class
		"""
		print("destroy class Auth")	
