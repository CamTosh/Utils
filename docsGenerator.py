import re

class Docs(object):
	"""Get class name and docstring for generate Docs"""

	def __init__(self, f):
		self.file = open(f, 'r')

		self.listeClasses = []
		self.listeDocString = []
		self.listeLibrairies = []
		self.listeMethods = []
		

	def getClass(self):
				
		for f in self.file:
			l = re.search('(class)(.*)', f)
			
			if l:
				s = l.group(0)
				className = s.replace(' ', '').replace("class", '').split("(")
				self.listeClasses.append(className[0])

		return self.listeClasses


	def getDoc(self):
		
		for f in self.file:
			l = re.search('"""(.*?)"""', f)
			
			if l:
				s = l.group(0)
				doc = s.replace('"""', ' ')
				self.listeDocString.append(doc)

		return self.listeDocString


	def getLib(self):
		
		for f in self.file:

			if f.startswith('import'):
				self.listeLibrairies.append(f.replace("import", "").replace(' ', ""))

			if f.startswith('from'):
				rer = f.split("import")
				self.listeLibrairies.append(rer[1].replace("import", "").replace(' ', "").replace("\n", ""))

		return self.listeLibrairies


	def getMethod(self):

		for f in self.file:
			l = re.search('(def)(.*)', f)
			
			if l:
				s = l.group(0)
				methodName = s.replace(' ', '').replace("def", '').replace(")", '').split("(")
				self.listeMethods.append(methodName[0])

		return self.listeMethods
