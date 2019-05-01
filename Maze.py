import Square as sq
import numpy as np
import Agent as ag


class Maze:
	def __init__(self):
		self.agent = ag.Agent()
		self.index = 9
		self.width = 4
		self.height = 3
		# To create a map with 4*3 size
		self.matrix = np.array([[sq.Square()] * self.width] * self.height)
		self.squares = {
			1: self.matrix[2][0],
			2: self.matrix[2][1],
			3: self.matrix[2][2],
			4: self.matrix[2][3],
			5: self.matrix[1][0],
			6: self.matrix[1][1],
			7: self.matrix[1][2],
			8: self.matrix[1][3],
			9: self.matrix[0][0],
			10: self.matrix[0][1],
			11: self.matrix[0][2],
			12: self.matrix[0][3]
		}


	def update_square_index(self):
		for i in range(0, self.height):
			if i > 0:
				self.index -= 8
			for j in range(0, self.width):
				# Initialization: Aim to make 12 independent squares
				temp = sq.Square()
				self.matrix[i][j] = temp
				self.matrix[i][j].pos_update(self.index)
				self.index += 1

	# To create connections between each independent square
	def update_square_relations(self):
		for i in range(0, self.height):
			for j in range(0, self.width):
				if self.matrix[i][j].location == 1:
					self.matrix[i][j].up = self.matrix[i - 1][j]
					self.matrix[i][j].right = self.matrix[i][j + 1]
				elif self.matrix[i][j].location == 2:
					self.matrix[i][j].up = self.matrix[i - 1][j]
					self.matrix[i][j].left = self.matrix[i][j - 1]
					self.matrix[i][j].right = self.matrix[i][j + 1]
				elif self.matrix[i][j].location == 3:
					self.matrix[i][j].left = self.matrix[i][j - 1]
					self.matrix[i][j].right = self.matrix[i][j + 1]
					self.matrix[i][j].up = self.matrix[i - 1][j]
				elif self.matrix[i][j].location == 4:
					self.matrix[i][j].up = self.matrix[i - 1][j]
					self.matrix[i][j].left = self.matrix[i][j - 1]
				elif self.matrix[i][j].location == 5:
					self.matrix[i][j].right = self.matrix[i][j + 1]
					self.matrix[i][j].up = self.matrix[i - 1][j]
					self.matrix[i][j].down = self.matrix[i + 1][j]
				elif self.matrix[i][j].location == 6:
					self.matrix[i][j].up = self.matrix[i - 1][j]
					self.matrix[i][j].down = self.matrix[i + 1][j]
					self.matrix[i][j].left = self.matrix[i][j - 1]
					self.matrix[i][j].right = self.matrix[i][j + 1]
				elif self.matrix[i][j].location == 7:
					self.matrix[i][j].up = self.matrix[i - 1][j]
					self.matrix[i][j].down = self.matrix[i + 1][j]
					self.matrix[i][j].left = self.matrix[i][j - 1]
					self.matrix[i][j].right = self.matrix[i][j + 1]
				elif self.matrix[i][j].location == 8:
					self.matrix[i][j].up = self.matrix[i - 1][j]
					self.matrix[i][j].down = self.matrix[i + 1][j]
					self.matrix[i][j].left = self.matrix[i][j - 1]
				elif self.matrix[i][j].location == 9:
					self.matrix[i][j].right = self.matrix[i][j + 1]
					self.matrix[i][j].down = self.matrix[i + 1][j]
				elif self.matrix[i][j].location == 10:
					self.matrix[i][j].down = self.matrix[i + 1][j]
					self.matrix[i][j].left = self.matrix[i][j - 1]
					self.matrix[i][j].right = self.matrix[i][j + 1]
				elif self.matrix[i][j].location == 11:
					self.matrix[i][j].down = self.matrix[i + 1][j]
					self.matrix[i][j].left = self.matrix[i][j - 1]
					self.matrix[i][j].right = self.matrix[i][j + 1]
				elif self.matrix[i][j].location == 12:
					self.matrix[i][j].left = self.matrix[i][j - 1]
					self.matrix[i][j].down = self.matrix[i + 1][j]

	def update_square_type(self, goal, wall, forbidden):
		for i in range(0, self.height):
			for j in range(0, self.width):
				# The start state always be 1
				# If the square's type is "Goal", its reward will be 100
				# If the square's type is "Forbidden", its reward will be -100
				if self.matrix[i][j].location == 1:
					self.matrix[i][j].type = "S"
					self.matrix[i][j].agent = True
				if self.matrix[i][j].location == goal:
					self.matrix[i][j].type = "G"
					self.matrix[i][j].reward = 100
				if self.matrix[i][j].location == wall:
					self.matrix[i][j].type = "W"
					self.matrix[i][j].access = False
				if self.matrix[i][j].location == forbidden:
					self.matrix[i][j].type = "F"
					self.matrix[i][j].reward = -100

	def update_square_dic(self):
		self.squares[1] = self.matrix[2][0]
		self.squares[2] = self.matrix[2][1]
		self.squares[3] = self.matrix[2][2]
		self.squares[4] = self.matrix[2][3]
		self.squares[5] = self.matrix[1][0]
		self.squares[6] = self.matrix[1][1]
		self.squares[7] = self.matrix[1][2]
		self.squares[8] = self.matrix[1][3]
		self.squares[9] = self.matrix[0][0]
		self.squares[10] = self.matrix[0][1]
		self.squares[11] = self.matrix[0][2]
		self.squares[12] = self.matrix[0][3]

	def isNone(self, agent, temp):
		tmp = False
		if agent.action == 1:
			if self.squares[temp].up == None:
					tmp = True
		elif agent.action == 2:
			if self.squares[temp].down == None:
					tmp = True
		elif agent.action == 3:
			if self.squares[temp].left == None:
					tmp = True
		elif agent.action == 4:
			if self.squares[temp].right == None:
					tmp = True
		return tmp


	def isWall(self, agent, temp,wall):
		tmp = False
		if agent.action == 1:
			if self.squares[temp].up.location == wall:
					tmp = True
		elif agent.action == 2:
			if self.squares[temp].down.location == wall:
					tmp = True
		elif agent.action == 3:
			if self.squares[temp].left.location == wall:
					tmp = True
		elif agent.action == 4:
			if self.squares[temp].right.location == wall:
					tmp = True
		return tmp