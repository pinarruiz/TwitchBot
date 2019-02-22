from socket import socket
from dbtools import Database
from threading import Thread

class Chat:
	def __init__(self):
		self.messageList = []

	def addMensaje(self, user, mensaje):
		self.messageList.append([user, mensaje])

class Rule:
	def __init__(self, ruleid, rule, response, active):
		self.ruleid = ruleid
		self.rule = rule
		self.response = response
		self.active = active

	def getRuleID(self):
		return self.ruleid

	def getRule(self):
		return self.rule

	def getResponse(self):
		return self.response

	def getActive(self):
		return bool(int(self.active))

	def getBtn(self):
		if self.active == 1:
			return "Regla activa", "#4CAF50"
		else:
			return "Regla no activa", "#BD2031"

class Rules:
	def __init__(self):
		self.dbHelper = Database("Rules")
		if not self.dbHelper.tableExists("ruledata"):
			self.dbHelper.createTable("ruledata", ["rule varchar(255)", "response varchar(225)", "active number", "ruleid number"])

	def getMaxRuleID(self):
		try:
			return int(self.dbHelper.executeSQL("SELECT MAX(ruleid) FROM ruledata")[0][0])
		except:
			return -1

	def editRule(self, ruleid, rule, response):
		self.dbHelper.modificar("ruledata", {"ruleid":ruleid}, {"rule":"\"" + rule + "\"", "response":"\"" + response + "\""})

	def addRule(self, rule, response):
		self.dbHelper.insertar("ruledata", ["\"" + rule + "\"", "\"" + response + "\"", "1", str(self.getMaxRuleID() + 1)])

	def isRuleActive(self, ruleid):
		return self.dbHelper.executeSQL("SELECT active FROM ruledata WHERE ruleid = " + str(ruleid))[0][0]

	def toggleRule(self, ruleid):
		nVal = self.isRuleActive(ruleid) + pow(-1 ,self.isRuleActive(ruleid))
		self.dbHelper.modificar("ruledata", {"ruleid":ruleid}, {"active":nVal})

	def deleteRule(self, ruleid):
		self.dbHelper.executeSQL("DELETE FROM ruledata WHERE ruleid = " + str(ruleid))

	def getRules(self):
		rules = self.dbHelper.executeSQL("SELECT * FROM ruledata")
		rulesObjs = []
		for rule in rules:
			rulesObjs.append(Rule(rule[3], rule[0], rule[1], rule[2]))
		return rulesObjs

	def getRuleByID(self, ruleid):
		rule = self.dbHelper.executeSQL("SELECT * FROM ruledata WHERE ruleid = " + str(ruleid))[0]
		return Rule(rule[3], rule[0], rule[1], rule[2])

class ChatBot(Thread):
	def __init__(self, nick, password):
		super(ChatBot, self).__init__()
		self.HOST = "irc.twitch.tv"
		self.PORT = 6667
		self.NICK = nick
		self.PASS = password
		self.botRun = False
		self.chatObj = None

	def send_message(self, message, sock):
		sock.send(bytes("PRIVMSG #" + self.NICK + " :" + message + "\r\n", "UTF-8"))

	def isRunning(self):
		return self.botRun

	def stopBot(self):
		self.botRun = False

	def getChat(self):
		return self.chatObj

	def iniSocket(self):
		sock = socket()
		sock.connect((self.HOST, self.PORT))
		sock.send(bytes("PASS " + self.PASS + "\r\n", "UTF-8"))
		sock.send(bytes("NICK " + self.NICK + "\r\n", "UTF-8"))
		sock.send(bytes("JOIN #" + self.NICK + " \r\n", "UTF-8"))

		while True:
			line = str(sock.recv(1024))
			if "End of /NAMES list" in line:
				break
		return sock

	def aplicarRegla(self, mensaje, regla):
		if rule.getActive():
			for msgpart in mensaje.split(" "):
				for ruleap in regla.getRule().split(";"):
					if ruleap == msgpart or msgpart == ruleap + ",":
						return True
		return False

	def run(self):
		self.botRun = True
		self.chatObj = Chat()
		self.sock = self.iniSocket()
		while self.botRun:
			for line in str(self.sock.recv(1024)).split('\\r\\n'):
				parts = line.split(':')
				if len(parts) < 3:
					continue
				if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
					message = parts[2][:len(parts[2])]
				usernamesplit = parts[1].split("!")
				username = usernamesplit[0]
				print(username + ": " + message)
				self.chatObj.addMensaje(username, message)
				rulesObj = Rules().getRules()
				for rule in rulesObj:
					if self.aplicarRegla(message, rule):
						self.send_message(rule.getResponse().replace("username", username), self.sock)
		self.botRun = False