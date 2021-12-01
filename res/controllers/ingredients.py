from res.controllers.api_standard_service import Api_standard_service
import datetime

class Ingredients(Api_standard_service):


	def gIngredients(self):
		sql = "SELECT * FROM Ingredients "

		sql += "WHERE nome_ingredient LIKE '{}%' ".format(self.args.get('name')) if self.args.get('name') != None else ""
		sql += "LIMIT {}".self.args.get('results') if self.args.get('results') != None else ""

		try:
			self.cursor.execute(sql)
			content = self.cursor.fetchall()
	
			data = {'content': [], 'nr_results': len(content)}
			for x in content:
				data['content'].append({'id': x[0], 'name': x[2], 'type': x[5]})

		except:
			data = {'status': 'Error: unable to fetch data'}	

		return data		




	def gIngredientDetails(self, ing_id):
		if not ing_id:
			return {'status': 300, 'Message':'parameter required [ingredient_id]'}
		
		data = {'content':[], 'total_results': 0}
		for x in ing_id.split(','):
			x = int(x)			
	
			ingredient = "SELECT * FROM Ingredients WHERE id_ingredient = {}".format(x)
			recipes = "SELECT Recipe.id_recipe, title, description, image_link FROM Recipe, Ingredientes_Receita WHERE Ingredientes_Receita.id_ingredient = {} and Ingredientes_Receita.id_recipe = Recipe.id_recipe and (Recipe.visible = 1 or (Recipe.visible = 0 and Recipe.id_user = {}))".format(x, self.user_id)

			try:	
				self.cursor.execute(ingredient)
				ing = self.cursor.fetchone()			
				
				if self.cursor.rowcount > 0:
					data['content'].append({'ingredient':{'id': ing[0], 'name': ing[2], 'calories': ing[3], 'type': ing[5], 'created_at': ing[4] }, 'recipes': [] })
					
					self.cursor.execute(recipes)
					recipesContent = self.cursor.fetchall()
						
					if len(recipesContent) > 0:
						for i in recipesContent:
							data['content'][len(data['content'])-1]['recipes'].append({'recipe_id': i[0], 'title': i[1], 'description': i[2], 'image_link': i[3]})			
				
					data['total_results'] += 1
			except:	
				data = {'Status': 301, 'Message': 'unable to fetch data'}
		
		if data['total_results'] == 0:
			return {'status': 'ERROR', 'Message': 'no data found for this request!'}
			
		return data






	def cIngredient(self):
		
		if self.checkParam(['name', 'type']) is False:
			return {'Status': 'ERROR', 'Message': 'Params required [name, type]'}
		
		# verifys if ingredient exists by checking his name
		if self.db_ver('Ingredients', 'nome_ingredient', self.args['name']) > 0:
			return {'status': 'ERROR', 'Message': 'Ingredient name already exists'}		
		
		
		try: calories = self.args['calories']
		except: calories  = 0

		sql = "INSERT INTO Ingredients(id_user, nome_ingredient, calories, created_at, type)VALUES(%s, %s, %s , %s, %s)"

		try:
			self.cursor.execute(sql, [self.user_id, self.args['name'], calories, datetime.date.today(), self.args['type']])
			self.db.commit()

			return {'Status': 200, 'Message': 'Ingredient Created'}
				
		except:
			return {'Status': 'ERROR', 'Message': 'Something went wrong!'}





	def uIngredient(self, ing_id):
		try: name = self.args['nome_ingredient']
		except: name = ""		

		param = ['nome_ingredient', 'calories', 'type']

		# verify if id and name exists
		if (self.db_ver('Ingredients', 'id_ingredient', ing_id) == 1) and ( self.db_ver('Ingredients', 'nome_ingredient', name) == 0 ): 	
			try:
				for x in param:
					if x in self.args and self.args[x] != None:
						sql = "UPDATE Ingredients SET {} = '{}' WHERE id_ingredient = {} and id_user = {}".format(x, self.args[x], ing_id, self.user_id)
						self.cursor.execute(sql)	
						
				self.db.commit()
				
			except:
				self.db.rollback()
		
		else:
			return {'status': 'ERROR', 'Message': 'Ingredient id not found or ingredient name already exists in DB'}		
	

		return {'status': 200, 'Message': 'successful updated!'}		





	def dIngredient(self, ing_id):
		
		if self.db_ver('Ingredients', 'id_ingredient', ing_id) == 0:
			return {'status': 'ERROR', 'Message': 'Ingredient id not found!'}

		delIng = "DELETE FROM Ingredients WHERE id_ingredient = {}".format(ing_id)
		delIngRec = "DELETE FROM Ingredientes_Receita WHERE id_ingredient = {}".format(ing_id)			
		
		try:
			self.cursor.execute(delIngRec)
			self.cursor.execute(delIng)
	
			self.db.commit()

		except:
			self.db.rollback()	
	
		return {'status': 204, 'Message': 'Ingredient deleted!'}



	def __del__(self):
		print("destroy class Ingredients")
