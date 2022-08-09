from ast import Yield
import enum


class Query():
	def __init__(self, path: str) -> None:
		if path[-4:] != ".sql":
			raise Exception("Wrong file type")
		self.path = path
		self.loaded = False
	
	def read(self):
		with open(self.path, 'r') as f:
			self.query = f.read()
		self.loaded = True
		return self # to allow shit like the line below

# q = Query("EXAMPLE/PATH").read()