import random as rand


class Agent:
	# alpha -- learning rate
	# gamma -- discount
	def __init__(self):
		self.action = 0
		self.alpha = 0.1
		self.gamma = 0.5
		# self.action_reward = -0.1
		self.location = 1

	def generate_action(self):
		# north--1
		# south--2
		# west--3
		# east--4
		self.action = rand.randint(1, 4)

	def reset(self):
		self.location = 1
		self.action = 0

	def make_action(self):
		if self.action == 1:
			self.location += 4
		elif self.action == 2:
			self.location -= 4
		elif self.action == 3:
			self.location -= 1
		elif self.action == 4:
			self.location += 1
