class Qtable:
	def __init__(self):
		self.stop = 0
		self.dictionary = {
			1: {1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00},
			2: {1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00},
			3: {1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00},
			4: {1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00},
			5: {1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00},
			6: {1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00},
			7: {1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00},
			8: {1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00},
			9: {1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00},
			10: {1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00},
			11: {1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00},
			12: {1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00},
		}
		self.dictionary_com = {
			1: {1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00},
			2: {1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00},
			3: {1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00},
			4: {1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00},
			5: {1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00},
			6: {1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00},
			7: {1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00},
			8: {1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00},
			9: {1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00},
			10: {1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00},
			11: {1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00},
			12: {1: 0.00, 2: 0.00, 3: 0.00, 4: 0.00},
		}
		self.route = []
		self.route_location=[]

	def update_value(self, index, action, value):
		# if self.dictionary.get(index).get(action) != value:
		self.dictionary[index][action] = value

	def reset(self):
		for i in range(1, 13):
			for j in range(1, 5):
				self.dictionary[i][j] = 0.00

	def isSame(self):
		flag = 0
		stop = 0
		for i in range(1, 13):
			set1 = set(self.dictionary[i].items())
			set2 = set(self.dictionary_com[i].items())
			set3 = set2 - set1
			if len(set3) == 0:
				flag += 1
			if flag == 12:
				stop += 1
		if stop == 12:
			self.stop = 1

	def optimal_policy(self, goal, forbidden, wall):
		for i in range(1, 13):
			if i != goal:
				if i != forbidden:
					if i != wall:
						subdic = self.dictionary[i]
						b = max(subdic.items(), key=lambda k: k[1])
						c = b[0]
						symbol = self.symbol(c)
						temp = str(i)
						print(temp + ": " + symbol)

	def symbol(self, action):

		if action == 1:
			return "↑ (North)"
		elif action == 2:
			return "↓ (South)"
		elif action == 3:
			return "← (West)"
		elif action == 4:
			return "→ (East)"

	def print_q_value(self, object):
		subdic = self.dictionary[object]
		for i in range(1, 5):
			symbol = self.symbol(i)
			temp = round(subdic[i], 2)
			print(symbol + "  ", temp)

	def converse(self,route_r):
		route_new=[]
		if route_r !=None:
			for i in route_r:
				if i==1:
					temp= 2
					route_new.append(temp)
				elif i==2:
					temp=1
					route_new.append(temp)
				elif i==3:
					temp=4
					route_new.append(temp)
				elif i==4:
					temp=3
					route_new.append(temp)
		return route_new