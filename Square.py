class Square:
	def __init__(self):
		# type:
		#  R--- Regular path
		#  W--- Wall
		#  S--- Start
		#  G--- Goal
		#  F--- Forbidden
		self.type = "R"
		self.location = 1
		self.up = None
		self.down = None
		self.left = None
		self.right = None
		self.reward = -0.10
		self.q_value_up = 0.00
		self.q_value_down = 0.00
		self.q_value_left = 0.00
		self.q_value_right = 0.00
		self.agent = False
		# This attribute only for wall square
		self.access = True
		# 1---up
		# 2---down
		# 3---left
		# 4---right
		self.best_action = 0
		self.best_q_value = 0.00
		self.temp_list = []

	def pos_update(self, loc_index):
		self.location = loc_index

	def type_update(self, loc_type):
		self.type = loc_type

	def find_max_q_value(self, agent):
		if agent.action == 1:
			if self.up != None:
				if self.up.type != "W":
					# self.best_q_value = self.sup_find_q(self.up)
					self.sup_find_q(agent)
		elif agent.action == 2:
			if self.down != None:
				if self.down.type != "W":
					# self.best_q_value = self.sup_find_q(self.down)
					self.sup_find_q(agent)
		elif agent.action == 3:
			if self.left != None:
				if self.left.type != "W":
					# self.best_q_value = self.sup_find_q(self.left)
					self.sup_find_q(agent)
		elif agent.action == 4:
			if self.right != None:
				if self.right.type != "W":
					# self.best_q_value = self.sup_find_q(self.right)
					self.sup_find_q(agent)

	# To find the max q value
	# 1---up
	# 2---down
	# 3---left
	# 4---right
	def update_q_value(self, agent, qtable):
		self.find_max_q_value(agent)
		if agent.action == 1:
			self.q_value_up = ((1 - agent.alpha) * self.q_value_up + agent.alpha * (
					self.reward + agent.gamma * self.best_q_value))
			# self.q_value_up = round(self.q_value_up, 2)
			qtable.update_value(agent.location, agent.action, self.q_value_up)

		elif agent.action == 2:
			self.q_value_down = ((1 - agent.alpha) * self.q_value_down + agent.alpha * (
					self.reward + agent.gamma * self.best_q_value))
			# self.q_value_down = round(self.q_value_down, 2)
			qtable.update_value(agent.location, agent.action, self.q_value_down)

		elif agent.action == 3:
			self.q_value_left = ((1 - agent.alpha) * self.q_value_left + agent.alpha * (
					self.reward + agent.gamma * self.best_q_value))
			# self.q_value_left = round(self.q_value_left, 2)
			qtable.update_value(agent.location, agent.action, self.q_value_left)

		elif agent.action == 4:
			self.q_value_right = ((1 - agent.alpha) * self.q_value_right + agent.alpha * (
					self.reward + agent.gamma * self.best_q_value))
			# self.q_value_right = round(self.q_value_right, 2)
			qtable.update_value(agent.location, agent.action, self.q_value_right)

	# This is a support function for find_max_q_value
	def sup_find_q(self, agent):
		self.temp_list.clear()
		if agent.action == 1:
			tmp = self.up
		elif agent.action == 2:
			tmp = self.down
		elif agent.action == 3:
			tmp = self.left
		elif agent.action == 4:
			tmp = self.right

		if tmp.location == 1:
			self.temp_list.append(tmp.q_value_up)
			self.temp_list.append(tmp.q_value_right)
		elif tmp.location == 2 | tmp.location == 3:
			self.temp_list.append(tmp.q_value_up)
			self.temp_list.append(tmp.q_value_right)
			self.temp_list.append(tmp.q_value_left)
		elif tmp.location == 4:
			self.temp_list.append(tmp.q_value_up)
			self.temp_list.append(tmp.q_value_left)
		elif tmp.location == 5:
			self.temp_list.append(tmp.q_value_up)
			self.temp_list.append(tmp.q_value_right)
			self.temp_list.append(tmp.q_value_down)
		elif tmp.location == 6:
			self.temp_list.append(tmp.q_value_up)
			self.temp_list.append(tmp.q_value_down)
			self.temp_list.append(tmp.q_value_left)
			self.temp_list.append(tmp.q_value_right)
		elif tmp.location == 7:
			self.temp_list.append(tmp.q_value_up)
			self.temp_list.append(tmp.q_value_down)
			self.temp_list.append(tmp.q_value_left)
			self.temp_list.append(tmp.q_value_right)
		elif tmp.location == 8:
			self.temp_list.append(tmp.q_value_up)
			self.temp_list.append(tmp.q_value_left)
			self.temp_list.append(tmp.q_value_down)
		elif tmp.location == 9:
			self.temp_list.append(tmp.q_value_down)
			self.temp_list.append(tmp.q_value_right)
		elif tmp.location == 10:
			self.temp_list.append(tmp.q_value_down)
			self.temp_list.append(tmp.q_value_left)
			self.temp_list.append(tmp.q_value_right)
		elif tmp.location == 11:
			self.temp_list.append(tmp.q_value_down)
			self.temp_list.append(tmp.q_value_left)
			self.temp_list.append(tmp.q_value_right)
		elif tmp.location == 12:
			self.temp_list.append(tmp.q_value_down)
			self.temp_list.append(tmp.q_value_left)
		# print(self.temp_list, agent.action, agent.location)
		self.best_q_value = max(self.temp_list, default=0.00)


# This part only for iterating q value backwards once the agent reaches the goal or forbidden
# The code below can be ignore if q value dont need to be update backwards.
	def sup_find_q2(self, act):
		self.temp_list.clear()
		if act == 1:
			tmp = self.up
		elif act == 2:
			tmp = self.down
		elif act == 3:
			tmp = self.left
		elif act == 4:
			tmp = self.right

		if tmp.location == 1:
			self.temp_list.append(tmp.q_value_up)
			self.temp_list.append(tmp.q_value_right)
		elif tmp.location == 2 | tmp.location == 3:
			self.temp_list.append(tmp.q_value_up)
			self.temp_list.append(tmp.q_value_right)
			self.temp_list.append(tmp.q_value_left)
		elif tmp.location == 4:
			self.temp_list.append(tmp.q_value_up)
			self.temp_list.append(tmp.q_value_left)
		elif tmp.location == 5:
			self.temp_list.append(tmp.q_value_up)
			self.temp_list.append(tmp.q_value_right)
			self.temp_list.append(tmp.q_value_down)
		elif tmp.location == 6:
			self.temp_list.append(tmp.q_value_up)
			self.temp_list.append(tmp.q_value_down)
			self.temp_list.append(tmp.q_value_left)
			self.temp_list.append(tmp.q_value_right)
		elif tmp.location == 7:
			self.temp_list.append(tmp.q_value_up)
			self.temp_list.append(tmp.q_value_down)
			self.temp_list.append(tmp.q_value_left)
			self.temp_list.append(tmp.q_value_right)
		elif tmp.location == 8:
			self.temp_list.append(tmp.q_value_up)
			self.temp_list.append(tmp.q_value_left)
			self.temp_list.append(tmp.q_value_down)
		elif tmp.location == 9:
			self.temp_list.append(tmp.q_value_down)
			self.temp_list.append(tmp.q_value_right)
		elif tmp.location == 10:
			self.temp_list.append(tmp.q_value_down)
			self.temp_list.append(tmp.q_value_left)
			self.temp_list.append(tmp.q_value_right)
		elif tmp.location == 11:
			self.temp_list.append(tmp.q_value_down)
			self.temp_list.append(tmp.q_value_left)
			self.temp_list.append(tmp.q_value_right)
		elif tmp.location == 12:
			self.temp_list.append(tmp.q_value_down)
			self.temp_list.append(tmp.q_value_left)
		# print(self.temp_list, agent.action, agent.location)
		self.best_q_value = max(self.temp_list, default=0.00)

	def find_max_q_value2(self, act):
		if act == 1:
			if self.up != None:
				if self.up.type != "W":
					# self.best_q_value = self.sup_find_q(self.up)
					self.sup_find_q2(act)
		elif act == 2:
			if self.down != None:
				if self.down.type != "W":
					# self.best_q_value = self.sup_find_q(self.down)
					self.sup_find_q2(act)
		elif act == 3:
			if self.left != None:
				if self.left.type != "W":
					# self.best_q_value = self.sup_find_q(self.left)
					self.sup_find_q2(act)
		elif act == 4:
			if self.right != None:
				if self.right.type != "W":
					# self.best_q_value = self.sup_find_q(self.right)
					self.sup_find_q2(act)

	def sec_update_q2(self, agent, qtable, loc, act):
		self.find_max_q_value2(act)
		if agent.action == 1:
			self.q_value_up = ((1 - agent.alpha) * self.q_value_up + agent.alpha * (
					self.reward + agent.gamma * self.best_q_value))
			# self.q_value_up = round(self.q_value_up, 2)
			qtable.update_value(loc, act, self.q_value_up)

		elif agent.action == 2:
			self.q_value_down = ((1 - agent.alpha) * self.q_value_down + agent.alpha * (
					self.reward + agent.gamma * self.best_q_value))
			# self.q_value_down = round(self.q_value_down, 2)
			qtable.update_value(loc, act, self.q_value_down)

		elif agent.action == 3:
			self.q_value_left = ((1 - agent.alpha) * self.q_value_left + agent.alpha * (
					self.reward + agent.gamma * self.best_q_value))
			# self.q_value_left = round(self.q_value_left, 2)
			qtable.update_value(loc, act, self.q_value_left)

		elif agent.action == 4:
			self.q_value_right = ((1 - agent.alpha) * self.q_value_right + agent.alpha * (
					self.reward + agent.gamma * self.best_q_value))
			# self.q_value_right = round(self.q_value_right, 2)
			qtable.update_value(loc, act, self.q_value_right)
