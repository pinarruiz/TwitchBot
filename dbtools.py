from sqlite3 import connect, OperationalError

class Database:
	def __init__(self, nombre):
		self.dbName = nombre
		self.conexion = connect(str(nombre) + ".db")
		self.cursor = self.conexion.cursor()

	def createTable(self, tableName, campos):
		campos = ", ".join(campos)
		query = "CREATE TABLE " + str(tableName) + " (" + campos + ")"
		if not self.tableExists(tableName):
			self.cursor.execute(query)
			return True
		else:
			return False

	def deleteTable(self, tableName):
		if self.tableExists(tableName):
			query = "DROP TABLE " + str(tableName)
			try:
				self.cursor.execute(query)
				return True
			except:
				return False
		else:
			return False
		
	def tableExists(self, tableName):
		try:
			query = "SELECT * FROM " + str(tableName)
			self.cursor.execute(query)
			return True
		except OperationalError:
			return False

	def insertar(self, tableName, values):
		if self.tableExists(tableName):
			query = "INSERT INTO " + str(tableName) + " VALUES(" + ', '.join(map(str, values)) + ")"
			self.cursor.execute(query)
			self.conexion.commit()
			return True
		else:
			return False

	def modificar(self, tableName, where, value):
		if self.tableExists(tableName):
			query = "UPDATE " + str(tableName) + " SET "
			for data in value:
				query += str(data) + " = " + str(value[str(data)]) + ", "
			query = query[:-2] + " WHERE "
			for key in where:
				query += str(key) + " = " + str(where[key]) + " AND "
			query = query[:-4]
			self.cursor.execute(query)
			self.conexion.commit()
			return True
		else:
			return False

	def executeSQL(self, sqlSentence, fetch = True):
		try:
			self.cursor.execute(sqlSentence)
			self.conexion.commit()
			if fetch:
				fetched = self.cursor.fetchall()
				for i in range(len(fetched)):
					fetched[i] = list(fetched[i])
				return fetched
			else:
				return True
		except Exception as e:
			print(e)
			return False