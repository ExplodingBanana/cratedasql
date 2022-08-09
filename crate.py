from query import Query

class Crate():
	def __init__(self) -> None:
		self.container:list[Query] = []

	def pack(self, query: Query=None, querylist: list[Query]=None, read: bool=False):
		if query:
			self.container.append(query.read()) if read else self.container.append(query)

		if querylist:
			if read:
				for q in querylist:
					self.container.append(q.read())
			else:
				for q in querylist:
					self.container.append(q)

		if not query and not querylist:
			raise Exception("Nothing to pack")

		return self  # to allow method cascading

	def unpack(self):
		c = self.container
		self.container.clear()
		return c # whatever, when you unpack a crate you get all of its contents

	def find(self, path: str):
		for q in self.container:
			if q.path == path:
				return q
		
# q = Query("EXAMPLE/PATH")

# c = Crate().pack(q) <- cascading
# c.pack(Query("ANOTHER/PATH"))

# w = c.find("ANOTHER/PATH") <- returns None if not found