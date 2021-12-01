from flask import Flask, request, jsonify, render_template, make_response
import mysql.connector
from mysql.connector import errorcode
import jwt
import datetime

from functools import wraps
from res.auth import Auth
from res.controllers.recipes import Recipes
from res.controllers.ingredients import Ingredients
from res.controllers.beers import Beers

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['SECRET_KEY'] = '21savageinjapan'

#config = {
#'host':'qkrecipes.mysql.database.azure.com',
#'user':'sorte@qkrecipes',
#'password':'wegotFlow21',
#'database':'quickrecipes',
#}

config = {
'host':'localhost',
'user':'root',
'password':'',
'database':'quickrecipes',
}


# Construct connection string
def db_connection():
	try:
		db = mysql.connector.connect(**config)	
		print('Connection status: {}'.format(db.is_connected()))

	except mysql.connector.Error as err:
  		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
   			print("Something is wrong with the user name or password")
  		elif err.errno == errorcode.ER_BAD_DB_ERROR:
    			print("Database does not exist")
  		else:
    			print(err)
	return db


"""
	With this app.route we go to the Home page
"""
@app.route('/', methods=['GET'])
def index():
	return render_template("api-doc.html")





# ****************************
# *          AUTH            *
# ****************************
"""
	With this app.route we check and create a new user if doesn't exist
"""

# CREATE USER
@app.route('/api/v1/auth/', methods=['POST'])
def auth():
	db = db_connection()
	"""

	:param name: user name
	:param email: user email

	:return: a key
	"""
	data = request.get_json()
	obj = Auth(db, data['email'], data['password'], data['name'], 0 /* covid */ ) if 'user_type' not in data else Auth(db, data['email'], data['password'], data['name'], data['user_type'], 0 /* covid */)  # instance obj
	response = obj.cUser()  # create record in DB

	return jsonify(response)


# LOGIN 
@app.route('/api/v1/login/')
def login():	
	db = db_connection()
	
	auth = request.authorization
	if not auth or not auth.username or not auth.password:
		return make_response('could not verify', 401, {'wwww-Authenticate':'Basic realm="Login required!"'})

	user_obj = Auth(db, auth.username, auth.password)
	user = user_obj.get_user()	
	
	if not user:		
		return make_response('could not verify', 401, {'wwww-Authenticate':'Basic realm="Login required!"'})
	
	if user_obj.check_password(user['password']):
		token = jwt.encode({'public_id': user['public_id'], 'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=30) }, app.config['SECRET_KEY'], algorithm="HS256")
		return jsonify({'token': token, 'user_type': user['user_type']})
	
	return make_response('could not verify', 401, {'wwww-Authenticate':'Basic realm="Login required!"'})


# SESSION VERIFICATION
def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		db = db_connection()
		token = None
		
		if 'x-access-token' in request.headers:
			token = request.headers['x-access-token']

		if not token:
			return jsonify({'message': 'Token is missing!'}), 401
				
		try:
			data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
			current_user = Auth(db).get_by_pi(data['public_id'])
		except:
			return jsonify({'message': 'Token is invalid'}), 401

		return f(current_user, db, *args, **kwargs)
	
	return decorated





# ****************
# * GET REQUESTS *
# ****************

"""
	With this app.route we can get all recipes with or without filters
"""
@app.route('/api/v1/Users/', methods=['GET'])
@token_required
def recipes(current_user, db):

	obj = Users(db, current_user['user_id'], request.args)
	response = obj.getAll()

	return jsonify(response)





@app.route('/api/v1/User_details/<int:user_id>', methods=['GET'])
@token_required
def g_recipe_details(current_user, db, user_id):

	obj = Users(db, current_user['user_id'], request.args)
	response = obj.getOne(user_id)
	
	return jsonify(response)



# *****************
# * POST REQUESTS *
# *****************

"""
- IMPORT XML / JSON

@app.route('/api/v1/create_recipe/', methods=['POST'])
@token_required
def create_recipe(current_user, db):
	
	data = request.get_json()
	
	obj = Recipes(db, current_user['user_id'], data)
	response = obj.cRecipe()	
	
	return jsonify(response) */

"""


# ****************
# * PUT REQUESTS *
# ****************

@app.route('/api/v1/userCovidStatus/<int:user_id>', methods=['PUT'])
@token_required
def update_recipe(current_user, db, user_id):
	
	data = request.get_json()
	
	obj = Covid(db, current_user['user_id'], data)
	response = obj.update(user_id)	
	
	return jsonify(response)




# *******************
# * DELETE REQUESTS *
# *******************




if __name__ == "__main__":
	app.run(debug=True, port=5000)
