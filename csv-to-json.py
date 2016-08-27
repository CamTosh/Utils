import csv
import json

class CsvToJson(object):
	"""Return CSV file in Json"""
	def __init__(self, file):
		self.file = file

	def toJson(self):

		with open(self.file) as f:
			reader = csv.reader(f, delimiter=',')
			out = json.dumps([row for row in reader])
		
			return out
