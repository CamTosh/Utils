import re

class Docs(object):
	"""Get class name and docstring for generate Docs"""

	def __init__(self, fichier):
		self.file = open(fichier, 'r')

		self.listeClasses = []
		self.listeDocString = []
		self.listeLibrairies = []

		self.getClass()
		self.getDocString()
		self.getLib()


	def __str__(self):
		# Todo
		documentation = {}
		
		for k, c in self.listeClasses:
			documentation[c] = self.listeDocString[k]

		return documentation


	def getClass(self):

		for f in self.file:
			l = re.search('(class)(.*)', f)
			
			if str(l) != "None":
				s = l.group(0)
				className = s.replace(' ', '').replace("class", '').split("(")
				self.listeClasses.append(className[0])


	def getDocString(self):
		# Todo
		for f in self.file:
			l = re.search('(class)[^$](.*)', f)


	def getLib(self);
		# Todo
		for f in file:
			if f.startswith('import'):
				self.listeLibrairies.append(f.replace("import", "").replace(' ', ""))
			if f.startswith('from'):
				rer = f.split("import")
				self.listeLibrairies.append(rer[1].replace("import", "").replace(' ', ""))