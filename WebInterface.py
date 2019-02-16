from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from socket import gethostbyname, gethostname
from os import urandom
from hashlib import md5
from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

from dbtools import Database
from ChatBot import ChatBot

app = Flask(__name__)
botObj = None

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

@app.route("/controlpanel", methods=['POST'])
def controlPanel():
	global botObj
	if request.form['botctrl'] == "btnonoff" and botObj != None:
		if botObj.isRunning():
			botObj.stopBot()
			botObj = None
		else:
			botObj.start()
	return redirect("/")

@app.route("/")
def webRoot():
	global botObj
	confDb = Database("BotConf")
	if session.get('login') is None:
		if confDb.tableExists("userdata"):
			return render_template("/login.html")
		else:
			return render_template("/noconf.html")
	else:
		if confDb.tableExists("config"):
			if botObj == None:
				userChannel, oauthtw = confDb.executeSQL("SELECT * FROM config")[0]
				botObj = ChatBot(decrypt(session['mddd1'], userChannel), decrypt(session['mddd1'], oauthtw))
			if botObj.isRunning():
				btnColor = "#4CAF50"
				btnValue = "Bot activado"
			else:
				btnColor = "#BD2031"
				btnValue = "Bot desactivado"
			return render_template("/dashboard.html", btnColor = btnColor, btnValue = btnValue)
		else:
			return render_template("/botfirstconfig.html")

def startServer(ipAddr = gethostbyname(gethostname()), port = 80):
	serverPort = 80
	app.secret_key = urandom(16)
	app.run(ipAddr, serverPort)

if __name__ == '__main__':
	startServer()