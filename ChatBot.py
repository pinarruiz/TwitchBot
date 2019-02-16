import socket
from threading import Thread

class ChatBot(Thread):
	def __init__(self, nick, password):
		super(ChatBot, self).__init__()
		self.HOST = "irc.twitch.tv"
		self.PORT = 6667
		self.NICK = nick
		self.PASS = password
		self.botRun = False

	def send_message(self, message, sock):
		sock.send(bytes("PRIVMSG #" + self.NICK + " :" + message + "\r\n", "UTF-8"))

	def isRunning(self):
		return self.botRun

	def stopBot(self):
		self.botRun = False

	def iniSocket(self):
		sock = socket.socket()
		sock.connect((self.HOST, self.PORT))
		sock.send(bytes("PASS " + self.PASS + "\r\n", "UTF-8"))
		sock.send(bytes("NICK " + self.NICK + "\r\n", "UTF-8"))
		sock.send(bytes("JOIN #" + self.NICK + " \r\n", "UTF-8"))

		while True:
			line = str(sock.recv(1024))
			if "End of /NAMES list" in line:
				break
		return sock

	def run(self):
		self.botRun = True
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
				if message == "Hola":
					self.send_message("Bienvenido a mi stream, " + username, self.sock)
		self.botRun = False