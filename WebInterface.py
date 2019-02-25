from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from socket import gethostbyname, gethostname
from os import urandom, system, name
from hashlib import md5
from threading import Thread
from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from logging import ERROR, getLogger
from random import randint

from dbtools import Database
from ChatBot import ChatBot, Rules, crawlYoutubeList
import embed

app = Flask(__name__)
log = getLogger('werkzeug')
log.setLevel(ERROR)
botObj = None

class Service:
	def __init__(self, name):
		self.serviceDb = Database("Services")
		self.table = name
		self.confTable = name + "conf"

	def getName(self):
		return self.table

	def toggleService(self):
		if self.serviceDb.executeSQL("SELECT * FROM " + self.confTable)[0][0] == 0:
			self.serviceDb.modificar(self.confTable, {"autostart" : 0}, {"autostart" : 1})
		else:
			self.serviceDb.modificar(self.confTable, {"autostart" : 1}, {"autostart" : 0})

	def getColor(self):
		if self.serviceDb.executeSQL("SELECT * FROM " + self.confTable)[0][0] == 0:
			return "#BD2031"
		else:
			return "#4CAF50"

	def getBtnString(self):
		if self.serviceDb.executeSQL("SELECT * FROM " + self.confTable)[0][0] == 0:
			return "Apagado"
		else:
			return "Encendido"

	def setOption(self, option, seted):
		self.serviceDb.modificar(self.confTable, None, {option : "\"" + seted + "\""})

	def getOption(self, option):
		try:
			optValue = self.serviceDb.executeSQL("SELECT " + str(option) + " FROM " + self.confTable)[0][0]
		except:
			optValue = 0
		if option == "fallback" and (optValue == 0 or optValue == "0"):
			return ""
		else:
			return optValue

def clearConsole():
	if name == 'nt':
		system("cls")
	else:
		system("clear")

def encrypt(key, source, encode=True):
	key = SHA256.new(key.encode()).digest()
	IV = Random.new().read(AES.block_size)
	encryptor = AES.new(key, AES.MODE_CBC, IV)
	padding = AES.block_size - len(source) % AES.block_size
	source += bytes([padding]).decode() * padding
	data = IV + encryptor.encrypt(source.encode())
	return b64encode(data).decode("latin-1") if encode else data

def decrypt(key, source, decode=True):
	if decode:
		source = b64decode(source.encode("latin-1"))
	key = SHA256.new(key.encode()).digest()
	IV = source[:AES.block_size]
	decryptor = AES.new(key, AES.MODE_CBC, IV)
	data = decryptor.decrypt(source[AES.block_size:])
	padding = data[-1]
	if data[-padding:] != bytes([padding]) * padding:
		raise ValueError("Invalid padding...")
	return data[:-padding].decode()

@app.route("/_feedsr", methods = ['GET'])
def feedMe():
	if session.get('login') is not None:
		servicesDatabase = Database("Services")
		if Service("songrequest").getOption("autostart") == 0:
			return ""
		try:
			videoid = servicesDatabase.executeSQL("SELECT * FROM songrequest")[0][0]
			servicesDatabase.executeSQL("DELETE FROM songrequest WHERE youtubeurl = '" + videoid + "'", False)
			return videoid
		except:
			fbList = Service("songrequest").getOption("fallback")
			if fbList != "":
				try:
					idList = crawlYoutubeList(fbList)
					return idList[randint(0, len(idList) - 1)]
				except:
					return ""
			return ""
	else:
		return ""

@app.route("/registerbot", methods=['POST'])
def registerBot():
	if request.form['user'] != None and request.form['pass1'] != None and request.form['pass2'] != None:
		if request.form['pass1'] == request.form['pass2']:
			confDb = Database("BotConf")
			if not confDb.tableExists("userdata"):
				confDb.createTable("userdata", ["usuario varchar(255)", "pass varchar(225)"])
				confDb.insertar("userdata", ["\"" + md5(request.form['user'].encode()).hexdigest() + "\"", "\"" + md5(request.form['pass1'].encode()).hexdigest() + "\""])
	return redirect("/")

@app.route("/loginbot", methods=['POST'])
def loginBot():
	if request.form['user'] != None and request.form['pass'] != None:
		confDb = Database("BotConf")
		dbData = confDb.executeSQL("SELECT * FROM userdata")[0]
		if dbData[0] == md5(request.form['user'].encode()).hexdigest():
			if dbData[1] == md5(request.form['pass'].encode()).hexdigest():
				session['login'] = request.form['user']
				session['mddd1'] = request.form['pass']
	return redirect("/")

@app.route("/oauthreg", methods=['POST'])
def oauthReg():
	if session.get('login') is not None and request.form['userchan'] is not None and request.form['oauthtw'] is not None:
		confDb = Database("BotConf")
		if not confDb.tableExists("config"):
			confDb.createTable("config", ["twitchchan varchar(255)", "oauth varchar(225)"])
			confDb.insertar("config", ["\"" + encrypt(session['mddd1'], request.form['userchan']) + "\"", "\"" + encrypt(session['mddd1'], request.form['oauthtw']) + "\""])
	return redirect("/")

@app.route("/newrule", methods=['POST'])
def newrule():
	if session.get('login') is None:
		return redirect("/")
	if request.form['btnrules'] == "inicio":
		return redirect("/")
	else:
		Rules().addRule(request.form['rule'], request.form['response'])
		return render_template("/rules.html", rulesObj = Rules().getRules())

@app.route("/rulectr", methods=['POST'])
def rulectr():
	if session.get('login') is None:
		return redirect("/")
	if request.form['ruleid'] == "nrule":
		return render_template("/newrule.html")
	if request.form['ruleid'] == "inicio":
		return redirect("/")
	else:
		session['ruleidedit'] = int(request.form['ruleid'])
		return render_template("/ruleedit.html", rule = Rules().getRuleByID(int(request.form['ruleid'])))

@app.route("/ruleeditor", methods=['POST'])
def ruleEditor():
	if session.get('login') is None:
		return redirect("/")
	if request.form['btnrules'] == "apagar":
		Rules().toggleRule(session["ruleidedit"])
	elif request.form['btnrules'] == "eliminar":
		Rules().deleteRule(session["ruleidedit"])
	elif request.form['btnrules'] == "guardar":
		Rules().editRule(session["ruleidedit"], request.form['rule'], request.form['response'])
	return render_template("/rules.html", rulesObj = Rules().getRules())

@app.route("/controlpanel", methods=['POST'])
def controlPanel():
	if session.get('login') is None:
		return redirect("/")
	global botObj
	if request.form['botctrl'] == "btnonoff" and botObj != None:
		if botObj.isRunning():
			botObj.stopBot()
			botObj = None
		else:
			botObj.start()
	elif request.form['botctrl'] == "rules":
		return render_template("/rules.html", rulesObj = Rules().getRules())
	elif request.form['botctrl'] == "servicios":
		servicesDatabase = Database("Services")
		if not servicesDatabase.tableExists("songrequestconf") or not servicesDatabase.tableExists("songrequest"):
			servicesDatabase.createTable("songrequestconf", ["autostart number", "fallback varchar(255)"])
			servicesDatabase.createTable("songrequest", ["youtubeurl varchar(255)"])
			servicesDatabase.insertar("songrequestconf", [0, "\"0\""])
		return render_template("/servicios.html", srColor = Service("songrequest").getColor())
	return redirect("/")

@app.route("/servicectr", methods=['POST'])
def serviceCtr():
	if session.get('login') is None or request.form['service'] == "inicio":
		return redirect("/")
	servicesDatabase = Database("Services")
	if request.form['service'] == "songrequest":
		if not servicesDatabase.tableExists("songrequestconf") or not servicesDatabase.tableExists("songrequest"):
			servicesDatabase.createTable("songrequestconf", ["autostart number"])
			servicesDatabase.createTable("songrequest", ["youtubeurl varchar(255)"])
			servicesDatabase.insertar("songrequestconf", [0, ""])
	return render_template("/servicio.html", service = Service(request.form['service']))

@app.route("/singleservice", methods=['POST'])
def singleService():
	if request.form['service'] == "inicio" or session.get('login') is None:
		return redirect("/")
	elif request.form['service'].split(";")[0] == 'toggle':
		Service(request.form['service'].split(";")[1]).toggleService()
	elif request.form['service'].split(";")[0] == 'save':
		Service(request.form['service'].split(";")[1]).setOption(request.form['service'].split(";")[2], request.form['fallback'])
	return render_template("/servicio.html", service = Service(request.form['service'].split(";")[1]))

@app.route("/")
def webRoot():
	global botObj
	confDb = Database("BotConf")
	if session.get('login') is None:
		session['autostart'] = True
		if confDb.tableExists("userdata"):
			return render_template("/login.html")
		else:
			return render_template("/noconf.html")
	else:
		if confDb.tableExists("config"):
			if botObj == None:
				userChannel, oauthtw = confDb.executeSQL("SELECT * FROM config")[0]
				botObj = ChatBot(decrypt(session['mddd1'], userChannel), decrypt(session['mddd1'], oauthtw))
				if session['autostart']:
					botObj.start()
					session['autostart'] = False
			if botObj.isRunning():
				btnColor = "#4CAF50"
				btnValue = "Bot activado"
			else:
				btnColor = "#BD2031"
				btnValue = "Bot desactivado"
			return render_template("/dashboard.html", btnColor = btnColor, btnValue = btnValue, channel = decrypt(session['mddd1'], confDb.executeSQL("SELECT * FROM config")[0][0]))
		else:
			return render_template("/botfirstconfig.html")

def startServer(ipAddr = gethostbyname(gethostname()), port = 80):
	app.secret_key = urandom(16)
	app.run(ipAddr, port)

def main(ipAddr = gethostbyname(gethostname()), port = 80):
	Thread(target = startServer, args = (ipAddr, port)).start()
	clearConsole()
	print(ipAddr + ":" + str(port))
	system("explorer \"http://" + ipAddr + "\"")

if __name__ == '__main__':
	main()