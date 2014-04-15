FOODS = ["candy apple", "power bar", "turkey jerky", "soda", "greens", "water"]
GAMES = ["checkers", "fetch", "bongos", "tag"]



class Pet(object):

	def __init__(self):
		self.max_health = 10

		self.health = 10
		self.happiness = 5
		self.love = 0
		
		self.strength = 3
		self.speed = 3
		self.smarts = 3

		self.get_faves(self)
		self.get_hated(self)

	def get_faves(self):
		pass

	def get_hated(self):
		pass

	def eat(self, item):
		pass

	def play(self, game):
		pass

	def train(self, item):
		pass

	def work(self, task):
		pass

class Food(object):

	def __init__(self, name, points={}):
		pass
