import Maze as mz
import Agent as ag
import Qtable as qt

user_input = input("Please enter 3 numbers and 1 character and possibly 1 additional number in [# # # X (#)] format!\n")
split_int = list(map(int, (x for x in user_input.split() if x.isdigit())))
split_char = list(map(str, (x for x in user_input.split() if x.isdigit() == False)))
# print(split_int)
# print(split_char)

goal = split_int[0]
forbidden = split_int[1]
wall = split_int[2]

# p---optimal policy
# q---optimal Q value
objective = split_char[0]
if objective == "q":
	additional = split_int[3]

# To generate a q tables
qtable = qt.Qtable()

# To set the maze with correct index and square types
maze = mz.Maze()
maze.update_square_index()
maze.update_square_type(goal, wall, forbidden)
maze.update_square_relations()

# This is the code to test the relationships for each square
# for i in range(0, 3):
# 	for j in range(0, 4):
# 		print(maze.matrix[i][j].location, maze.matrix[i][j].type)
# 		if (maze.matrix[i][j].up != None):
# 			print("UP:", maze.matrix[i][j].up.location)
# 		if (maze.matrix[i][j].down != None):
# 			print("DOWN:", maze.matrix[i][j].down.location)
# 		if (maze.matrix[i][j].left != None):
# 			print("LEFT:", maze.matrix[i][j].left.location)
# 		if (maze.matrix[i][j].right != None):
# 			print("RIGHT:", maze.matrix[i][j].right.location)
# 		print("-------------------------------------------------------------\n")

# Pull every square into a new dictionary for organizing
maze.update_square_dic()


# Create a new agent
agent = ag.Agent()
x = 0
first = 0

print("Program is processing! Please wait a few seconds.")
while (qtable.stop == 0) & (x < 10000):
	# agent = ag.Agent()
	# while x < 10000:
	if first == 0:
		first = 1
	else:
		qtable.dictionary_com = qtable.dictionary
	# agent.location = 1
	qtable.route.clear()
	qtable.route_location.clear()
	while agent.location != forbidden & agent.location != goal:
		# update the agent location based on actions
		# Agent will randomly generate actions, and if the corresponding square doesnt exist,
		# randomly generate again
		temp = agent.location
		flag = True
		# flag2 = True
		while flag:
			agent.generate_action()
			flag = maze.isNone(agent, temp)
		# flag2= maze.isWall(agent,temp,wall)
		if agent.location != wall:
			qtable.route_location.append(agent.location)
			qtable.route.append(agent.action)
			maze.squares[agent.location].update_q_value(agent, qtable)
		agent.make_action()
		if agent.location ==wall:
			qtable.route_location.pop(-1)
			qtable.route.pop(-1)
			agent.location=temp
			agent.action=0
		elif agent.location == goal | agent.location == forbidden:
			qtable.route_location.append(agent.location)
	qtable.isSame()
	# a = qtable.route
	# b = qtable.route_location
	# a.reverse()
	# b.reverse()
	# c = len(b)
	# for i in range(0,c-1):
	# 	maze.squares[b[i+1]].sec_update_q2(agent,qtable,b[i+1], a[i])
	agent.reset()
	# print("QTable: ", qtable.dictionary)
	# print("-------------------------------------------------------------\n")
	x += 1
print("STOPPED!, Iterated", x, "times")

# option "p" is to print the optimal policy
if objective == "p":
	qtable.optimal_policy(goal, forbidden, wall)
elif objective == "q":
	qtable.print_q_value(additional)
else:
	print("Please Enter Correct Information!")
	exit(0)
