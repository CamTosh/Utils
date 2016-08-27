import csv
import json
from json import dumps

class CsvToJson(object):
	"""Return CSV file in Json"""
	def __init__(self, file):
		self.file = file

	def toJson(self):

		with open(self.file) as f:
			reader = csv.reader(f, delimiter=',')
			out = json.dumps([row for row in reader])
		
			return out


class toast(object):
	"""docstring for toast"""
	def __init__(self, arg):
		super(toast, self).__init__()
		self.arg = arg
	def __str__(self):
		return "ntm fdp"
		

class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		
	def blblbl(self):
		class ddddddddd(object):
			"""docstring for ddddddddd"""
			def __init__(self, arg):
				super(ddddddddd, self).__init__()
				self.arg = arg
				