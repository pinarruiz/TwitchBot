from os import listdir
from base64 import b64encode, b64decode

def detectFolders(where = "."):
	directories = []
	for file in listdir(where):
		if len(file.split(".")) == 1:
			if not file in directories and file != "__pycache__":
				directories.append(where + "/" + file)
	moredirs = []
	if directories != []:
		for direct in directories:
			moredirs += detectFolders(direct)
	return [*dict.fromkeys(directories + moredirs + ["."]).keys()]

def embedTo(output = "embed.py", target = None, args = None, where = None):
	with open(output, "w") as embededFile:
		embededFile.write("import base64\nfrom os import makedirs, remove\nfolders = " + str(detectFolders()) + "\nfor folder in folders:\n\tif folder != \".\":\n\t\ttry:\n\t\t\tremove(folder)\n\t\texcept:\n\t\t\tpass\n\t\ttry:\n\t\t\tmakedirs(folder)\n\t\texcept:\n\t\t\tpass\n")
		directories = detectFolders()
		for directorio in directories:
			for file in listdir(directorio):
				if file != output and len(file.split(".")) >= 2:
					if file.split(".")[0] not in ["embederUtil"]:
						with open(directorio + "/" + file, "r") as template:
							encoded = b64encode(template.read().encode()).decode()
							embededFile.write(file.split(".")[0] + " = base64.b64decode(\"" + encoded + "\".encode())\n")
							embededFile.write("open(\"" + str(directorio + "/" + file) + "\", \"w\").write(" + file.split(".")[0] + ".decode())\n")
		if where != None:
			embededFile.write("from " + str(where) + " import " + str(target) + "\n")
			if target != None:
				embededFile.write(target + "(")
				if args != None:
					embededFile.write(", ".join(list(map(str, args))))
				embededFile.write(")\n")

embedTo()