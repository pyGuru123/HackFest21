#maze game python 

from graph import Graph
from character import Character
import ui_file
import astar
import random
import pygame
import time
import queue
from collections import deque
import os

# function to set the position of the display window
def set_window_position(x, y):
	os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

# creates a grid of size (size)*(size)
def create_grid(size):

	# create a graph for the grid
	grid = Graph()

	# add the vertices of the grid
	for i in range(size):
		for j in range(size):
			grid.add_vertex((i,j))

	# return the constructed grid
	return grid

# creates a maze when a grid ad its vertices are passed in
def create_maze(grid, vertex, completed=None, vertices=None):
	
	if vertices is None:
		vertices = grid.get_vertices()
	if completed is None:
		completed = [vertex]

	# select a random direction
	paths = list(int(i) for i in range(4))
	random.shuffle(paths)

	# vertices in the direction from current vertex
	up = (vertex[0],vertex[1]-1)
	down = (vertex[0],vertex[1]+1)
	left = (vertex[0]-1,vertex[1])
	right = (vertex[0]+1,vertex[1])

	for direction in paths:
		if direction == 0:
			if up in vertices and up not in completed:
				# add the edges
				grid.add_edge((vertex,up))
				grid.add_edge((up,vertex))
				completed.append(up)
				create_maze(grid, up, completed, vertices)
		elif direction == 1:
			if down in vertices and down not in completed:
				grid.add_edge((vertex,down))
				grid.add_edge((down,vertex))
				completed.append(down)
				create_maze(grid, down, completed, vertices)
		elif direction == 2:
			if left in vertices and left not in completed:
				grid.add_edge((vertex,left))
				grid.add_edge((left,vertex))
				completed.append(left)
				create_maze(grid, left, completed, vertices)
		elif direction == 3:
			if right in vertices and right not in completed:
				grid.add_edge((vertex,right))
				grid.add_edge((right,vertex))
				completed.append(right)
				create_maze(grid, right, completed, vertices)

	return grid

# draw maze function
# takes in a (size)x(size) maze and prints a "colour" path
# side_length is the length of the grid unit and border_width is its border thickness
def draw_maze(screen, maze, size, colour, side_length, border_width):
	# for every vertex in the maze:
	for i in range(size):
		for j in range(size):
			# if the vertex is not at the left-most side of the map
			if (i != 0):
				# check if the grid unit to the current unit's left is connected by an edge
				if maze.is_edge(((i,j),(i-1,j))):
					# if connected, draw the grid unit without the left wall
					pygame.draw.rect(screen,colour,[(side_length+border_width)*i, border_width+(side_length+border_width)*j,\
									 side_length+border_width, side_length])
			# if the vertex is not at the right-most side of the map
			if (i != size-1):
				if maze.is_edge(((i,j),(i+1,j))):
					# draw the grid unit without the right wall (extend by border_width)
					pygame.draw.rect(screen,colour,[border_width+(side_length+border_width)*i,\
									 border_width+(side_length+border_width)*j, side_length+border_width, side_length])
			# if the vertex is not at the top-most side of the map
			if (j != 0):
				if maze.is_edge(((i,j),(i,j-1))):
					pygame.draw.rect(screen,colour,[border_width+(side_length+border_width)*i,\
									 (side_length+border_width)*j, side_length, side_length+border_width])
			# if the vertex is not at the bottom-most side of the map
			if (j != size-1):
				if maze.is_edge(((i,j),(i,j+1))):
					pygame.draw.rect(screen,colour,[border_width+(side_length+border_width)*i,\
									 border_width+(side_length+border_width)*j, side_length, side_length+border_width])

# draw position of grid unit
def draw_position(screen, side_length, border_width, current_point, colour):
	pygame.draw.rect(screen, colour, [border_width+(side_length+border_width)*current_point[0],\
					 border_width+(side_length+border_width)*current_point[1], side_length, side_length])

# takes in a player2 character, maze, vertices, cooldown, and timer
def playerTwo(player2, maze, vertices, cooldown, timer):
	# get the pressed keys
	keys = pygame.key.get_pressed()
	
	if (pygame.time.get_ticks() - timer > cooldown):
		current_point = player2.get_current_position()
		# move character right
		if keys[pygame.K_d]:
			# check if the next point is in the maze
			if (current_point[0]+1, current_point[1]) in vertices:
				next_point = (current_point[0]+1, current_point[1])
				# check if the next point is connected by an edge
				if (maze.is_edge((current_point,next_point))):
					player2.move_character_smooth(next_point,5)
			# restart cooldown timer
			timer = pygame.time.get_ticks()
		# move character left
		if keys[pygame.K_a]:
			if (current_point[0]-1,current_point[1]) in vertices:
				next_point = (current_point[0]-1, current_point[1])
				if (maze.is_edge((current_point,next_point))):
					player2.move_character_smooth(next_point,5)
			# restart cooldown timer
			timer = pygame.time.get_ticks()
		# move character up
		if keys[pygame.K_w]:
			if (current_point[0],current_point[1]-1) in vertices:
				next_point = (current_point[0], current_point[1]-1)
				if (maze.is_edge((current_point,next_point))):
					player2.move_character_smooth(next_point,5)
			# restart cooldown timer
			timer = pygame.time.get_ticks()
		# move character down
		if keys[pygame.K_s]:
			if (current_point[0],current_point[1]+1) in vertices:
				next_point = (current_point[0], current_point[1]+1)
				if (maze.is_edge((current_point,next_point))):
					player2.move_character_smooth(next_point,5)
			# restart cooldown timer
			timer = pygame.time.get_ticks()

	return timer

# update path function for chase mode
def update_path(next_point, deque):
	if len(deque) >= 2:
		# get the current point before the move
		first_pop = deque.pop()
		# get the previous point
		second_pop = deque.pop()
		# if the player backtracks (previous point == next point)
		if second_pop == next_point:
			# only append the previous point
			deque.append(second_pop)
		else:
			# add all the points back to the deque including the next point
			deque.append(second_pop)
			deque.append(first_pop)
			deque.append(next_point)
		# return the deque
		return deque
	else:
		# if the deque only has its initial point
		deque.append(next_point)
		# return the deque
		return deque

# astar update path function
def update_path_a(start_point, end_point, maze, deque):
	# get the shortest path using astar
	closest_path = astar.astar(start_point, end_point, maze)
	# starting point is not needed
	closest_path.remove(start_point)
	# if the current path has more points than the closest path by astar,
	# load the deque with the new set of points from a_star
	if len(deque)+1 > len(closest_path):
		# clear the existing deque
		deque.clear()
		# append the new edges
		for edge in closest_path:
			deque.append(edge)
		# return the new deque
		return deque
	# if not, update the path as usual
	else:
		# return the deque with the appended path, end_point acts as the next point
		return update_path(end_point, deque)

# break wall function just for escape mode
def break_wall(maze, current_point, next_point):
	# if there is no path from the current point to the next point, make one
	if not maze.is_edge((current_point,next_point)):
		maze.add_edge((current_point,next_point))
		maze.add_edge((next_point,current_point))
	# return the new maze
	return maze

# update console function for escape mode
def update_console(screen, screen_size, side_length, text_size, a_colour, na_colour, keys_left, wallBreaks):
	if keys_left == 0:
		text = "Escape! " + " WB: " + str(wallBreaks)
	else:
		text = "K: " + str(keys_left) + " WB: " + str(wallBreaks)
	# console rect
	console_rect = (0, screen_size[1]-side_length*3, screen_size[0], side_length*3)
	# clear console
	pygame.draw.rect(screen, na_colour,console_rect)
	# display the text
	displayText = pygame.font.SysFont("ubuntu", text_size)
	textSurface = displayText.render(text, True, a_colour)
	textRect = textSurface.get_rect()
	# center text
	textRect.center = (screen_size[0]/2,screen_size[1]-text_size*2)
	# display text on screen ("blit")
	screen.blit(textSurface,textRect)
	# update the screen
	pygame.display.update(console_rect)

# run the maze game
# takes in a game mode parameter along with grid size and side length for the maze
def runGame(grid_size, side_length, mode):
	# initialize the game engine
	pygame.init()

	# Defining colours (RGB) ...
	BLACK = (0,0,0)
	GRAY = (100,100,100)
	WHITE = (255,255,255)
	GOLD = (249,166,2)
	GREEN = (0,255,0)
	RED = (255,0,0)
	BLUE = (0,0,255)

	# set the grid size and side length of each grid
	# grid_size = 20 # this is the maximum size before reaching recursion limit on maze buidling function
	# side_length = 10

	# scale the border width with respect to the given side length
	border_width = side_length//5

	# initialize the grid for the maze
	grid = create_grid(grid_size)
	# create the maze using the grid
	maze = create_maze(grid, (grid_size//2,grid_size//2)) # use the starting vertex to be middle of the map

	# Opening a window ...
	# set the screen size to match the grid
	size = (grid_size*(side_length+border_width)+border_width,\
			grid_size*(side_length+border_width)+border_width)
	# re-size screen if it is escape mode
	if mode == 4:
		size = (size[0],size[1]+side_length*3)
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("\"Esc\" to exit")

	# set the continue flag
	carryOn = True

	# set the clock (how fast the screen updates)
	clock = pygame.time.Clock()

	# have a black background
	screen.fill(BLACK)

	# get all of the vertices in the maze
	vertices = maze.get_vertices()

	# draw the maze
	draw_maze(screen, maze, grid_size, WHITE, side_length, border_width)

	# initialize starting point of character and potential character 2
	start_point = (0,0)
	# opposing corner
	start_point2 = (grid_size-1,grid_size-1)

	# set end-point for the maze
	end_point = (grid_size-1,grid_size-1)
	# initialize opponent's end-point for two player mode
	end_point2 = (0,0)

	# randomize a start and end point
	choice = random.randrange(4)

	if choice == 0:
		start_point = (grid_size-1,grid_size-1)
		start_point2 = (0,0)
		end_point = (0,0)
		end_point2 = (grid_size-1,grid_size-1)
	elif choice == 1:
		start_point = (0,grid_size-1)
		start_point2 = (grid_size-1,0)
		end_point = (grid_size-1,0)
		end_point2 = (0,grid_size-1)
	elif choice == 2:
		start_point = (grid_size-1,0)
		start_point2 = (0,grid_size-1)
		end_point = (0,grid_size-1)
		end_point2 = (grid_size-1,0)

	# initialize winner variable
	winner = 0

	# initialize the character
	player1 = Character(screen, side_length, border_width, vertices,\
						start_point, end_point, start_point, GREEN, WHITE)
	
	# if the two player game mode is selected, initialize the other character
	if mode == 1:
		player2 = Character(screen, side_length, border_width, vertices,\
							start_point2, end_point2, start_point2, BLUE, WHITE)
	# if computer race mode is selected
	elif mode == 2:
		# initialize computer character
		computer_character = Character(screen, side_length, border_width, vertices,\
								 start_point2, end_point2, start_point2, GRAY, WHITE)
		# find the shortest path for the computer to get to the end sing astar
		path = astar.astar(start_point2, end_point2, maze)
		# initialize a queue to pop in edges to solve
		q = queue.Queue()
		# add the paths the computer has to take to the queue
		for edge in path:
			q.put(edge)
		# set the cooldown for how fast the computer moves (scales with maze size)
		computer_cooldown = grid_size*15
		# set the maximum cooldown for the computer
		if computer_cooldown > 350:
			computer_cooldown = 350
		# initialize timer
		computer_timer = pygame.time.get_ticks()
	# if computer chase mode is selected
	elif mode == 3:
		# initialize computer character
		computer_character = Character(screen, side_length, border_width, vertices,\
								 start_point, end_point, start_point, GRAY, WHITE)
		# create a deque for the paths to the player
		dq = deque()
		# put start_point for the deque
		dq.append(start_point)
		# set the cooldown for how fast the computer moves
		computer_cooldown = grid_size*10
		# set the maximum cooldown for the computer
		if computer_cooldown > 300:
			computer_cooldown = 300
		# set the initial wait time for the computer
		initial_wait = 3000
		# initialize timers
		computer_timer = pygame.time.get_ticks()
		initial_wait_timer = pygame.time.get_ticks()
	# if escape mode is selected
	elif mode == 4:
		# set random key points (from 1 to grid_size-2)
		# 8 keys in total
		x_coords = random.sample(range(1,grid_size-1),8)
		y_coords = random.sample(range(1,grid_size-1),8)
		# initialize empty key list
		unlock_keys = []
		# append coordinates to the key list
		for i in range(8):
				unlock_keys.append((x_coords[i],y_coords[i]))
		# re-initialize character
		player1 = Character(screen, side_length, border_width, vertices, start_point,\
							end_point, start_point, GREEN, WHITE, True, unlock_keys, GOLD)
		# initialize computer character
		computer_character = Character(screen, side_length, border_width, vertices,\
								 start_point, end_point, start_point, GRAY, WHITE)
		# create a deque for the paths to the player
		dq = deque()
		# put start_point for the deque
		dq.append(start_point)
		# set the cooldown for how fast the computer moves
		computer_cooldown = grid_size*100
		# set the maximum cooldown for the computer
		if computer_cooldown > 3000:
			computer_cooldown = 3000
		# set the initial wait time for the computer
		initial_wait = 3000
		# initialize timers
		computer_timer = pygame.time.get_ticks()
		initial_wait_timer = pygame.time.get_ticks()

	# draw the end-point
	draw_position(screen, side_length, border_width, end_point, RED)
	# if two player mode, draw endpoints
	if mode == 1:
		draw_position(screen, side_length, border_width, end_point, GREEN)
		draw_position(screen, side_length, border_width, end_point2, BLUE)
	# if computer mode, draw gray endpoint for computer
	elif mode == 2:
		draw_position(screen, side_length, border_width, end_point, GREEN)
		draw_position(screen, side_length, border_width, end_point2, GRAY)
	# if escape mode, draw keys
	elif mode == 4:
		player1.draw_keys()
		# update console
		update_console(screen, size, side_length, size[0]//grid_size, WHITE, BLACK, player1.get_keys_left(), player1.get_wallBreaks())
		

	# update the screen
	pygame.display.flip()

	# set cooldown for key presses
	cooldown = 100

	# initialize the cooldown timer
	start_timer = pygame.time.get_ticks()

	# if the two player mode is selected, initialize the cooldown timer for second player
	if mode == 1:
		start_timer2 = pygame.time.get_ticks()

	# initialize game timer for solo mode
	game_timer = 0
	# if solo mode is selected, start game timer
	if mode == 0:
		game_timer = time.time()

	# main loop
	while carryOn:
		# action (close screen)
		for event in pygame.event.get():# user did something
			if event.type == pygame.QUIT:
				carryOn = False
				# mode = -1 means just exit
				mode = -1
			elif event.type == pygame.KEYDOWN:
				#Pressing the Esc Key will quit the game
				if event.key == pygame.K_ESCAPE:
					carryOn = False
					mode = -1

		# get the pressed keys
		keys = pygame.key.get_pressed()
		
		if (pygame.time.get_ticks() - start_timer > cooldown):
			# get the current point of character
			current_point = player1.get_current_position()
			# move character right
			if keys[pygame.K_RIGHT]:
				# check if the next point is in the maze
				if (current_point[0]+1,current_point[1]) in vertices:
					next_point = (current_point[0]+1,current_point[1])
					# check if the next point is connected by an edge
					if (maze.is_edge((current_point,next_point))):
						player1.move_character_smooth(next_point,5)
						# if the current mode is chase mode or escape mode
						if mode == 3:
							# update the shortest path for the computer to use
							dq = update_path(next_point, dq)
						elif mode == 4:
							dq = update_path_a(computer_character.get_current_position(), next_point, maze, dq)
					else:
						# if it is escape mode
						if mode == 4:
							# if the player pressed the space key, break the wall in the direction they are moving in
							if keys[pygame.K_SPACE] and player1.get_wallBreaks() > 0:
								maze = break_wall(maze, current_point, next_point)
								# move the player to that point
								player1.move_character_smooth(next_point,5)
								# decrement the player's number of wallBreaks
								player1.use_wallBreak()
								# update the shortest path for the computer to use
								dq = update_path_a(computer_character.get_current_position(), next_point, maze, dq)
				# restart cooldown timer
				start_timer = pygame.time.get_ticks()
			# move character left
			elif keys[pygame.K_LEFT]:
				if (current_point[0]-1,current_point[1]) in vertices:
					next_point = (current_point[0]-1, current_point[1])
					if (maze.is_edge((current_point,next_point))):
						player1.move_character_smooth(next_point,5)
						# if the current mode is chase mode or escape mode
						if mode == 3:
							dq = update_path(next_point, dq)
						elif mode == 4:
							dq = update_path_a(computer_character.get_current_position(), next_point, maze, dq)
					else:
						# if it is escape mode
						if mode == 4:
							# if the player pressed the space key, break the wall in the direction they are moving in
							if keys[pygame.K_SPACE] and player1.get_wallBreaks() > 0:
								maze = break_wall(maze, current_point, next_point)
								# move the player to that point
								player1.move_character_smooth(next_point,5)
								# decrement the player's number of wallBreaks
								player1.use_wallBreak()
								# update the shortest path for the computer to use
								dq = update_path_a(computer_character.get_current_position(), next_point, maze, dq)
				# restart cooldown timer
				start_timer = pygame.time.get_ticks()
			# move character up
			elif keys[pygame.K_UP]:
				if (current_point[0],current_point[1]-1) in vertices:
					next_point = (current_point[0], current_point[1]-1)
					if (maze.is_edge((current_point,next_point))):
						player1.move_character_smooth(next_point,5)
						# if the current mode is chase mode or escape mode
						if mode == 3:
							dq = update_path(next_point, dq)
						elif mode == 4:
							dq = update_path_a(computer_character.get_current_position(), next_point, maze, dq)
					else:
						# if it is escape mode
						if mode == 4:
							# if the player pressed the space key, break the wall in the direction they are moving in
							if keys[pygame.K_SPACE] and player1.get_wallBreaks() > 0:
								maze = break_wall(maze, current_point, next_point)
								# move the player to that point
								player1.move_character_smooth(next_point,5)
								# decrement the player's number of wallBreaks
								player1.use_wallBreak()
								# update the shortest path for the computer to use
								dq = update_path_a(computer_character.get_current_position(), next_point, maze, dq)
				# restart cooldown timer
				start_timer = pygame.time.get_ticks()
			# move character down
			elif keys[pygame.K_DOWN]:
				if (current_point[0],current_point[1]+1) in vertices:
					next_point = (current_point[0], current_point[1]+1)
					if (maze.is_edge((current_point,next_point))):
						player1.move_character_smooth(next_point,5)
						# if the current mode is chase mode or escape mode
						if mode == 3:
							dq = update_path(next_point, dq)
						elif mode == 4:
							dq = update_path_a(computer_character.get_current_position(), next_point, maze, dq)
					else:
						# if it is escape mode
						if mode == 4:
							# if the player pressed the space key, break the wall in the direction they are moving in
							if keys[pygame.K_SPACE] and player1.get_wallBreaks() > 0:
								maze = break_wall(maze, current_point, next_point)
								# move the player to that point
								player1.move_character_smooth(next_point,5)
								# decrement the player's number of wallBreaks
								player1.use_wallBreak()
								# update the shortest path for the computer to use
								dq = update_path_a(computer_character.get_current_position(), next_point, maze, dq)
				# restart cooldown timer
				start_timer = pygame.time.get_ticks()

		# PLAYER 2 MOVEMENT HERE (if gamemode selected)
		if mode == 1:
			# update the start timer for player 2
			start_timer2 = playerTwo(player2, maze, vertices, cooldown, start_timer2)

			# redraw the finish points
			draw_position(screen, side_length, border_width, end_point, GREEN)
			draw_position(screen, side_length, border_width, end_point2, BLUE)
			# redraw the characters
			player2.draw_position()
			player1.draw_position()
			# update screen
			pygame.display.update()

		# computer movement for race mode
		elif mode == 2:
			if (pygame.time.get_ticks() - computer_timer > computer_cooldown):
				computer_character.move_character_smooth(q.get(),5)
				# reset the cooldown timer for computer
				computer_timer = pygame.time.get_ticks()

			# redraw the finish points
			draw_position(screen, side_length, border_width, end_point, GREEN)
			draw_position(screen, side_length, border_width, end_point2, GRAY)
			# redraw the characters
			computer_character.draw_position()
			player1.draw_position()
			# update screen
			pygame.display.update()

		# computer movement for chase mode and escape mode
		elif mode == 3 or mode == 4:
			if mode == 4:
				# redraw the keys
				player1.draw_keys()
				# check if all keys are collected
				if player1.collected_all():
					draw_position(screen, side_length, border_width, end_point, GREEN)
				else:
					draw_position(screen, side_length, border_width, end_point, RED)
				# increase the computer speed if got another 2 keys
				if player1.increase_computer_speed():
					computer_cooldown = computer_cooldown/2
				# update console
				update_console(screen, size, side_length, size[0]//grid_size, WHITE, BLACK, player1.get_keys_left(), player1.get_wallBreaks())

			# update the wait condition
			waitCondition = pygame.time.get_ticks() - initial_wait_timer > initial_wait
			# check if the wait condition is met
			if (waitCondition):
				if (pygame.time.get_ticks() - computer_timer > computer_cooldown):
					# make sure that the deque is not empty
					if dq:
						computer_character.move_character_smooth(dq.popleft(),5)
					# reset the cooldown timer for computer
					computer_timer = pygame.time.get_ticks()

			# redraw the characters
			computer_character.draw_position()
			player1.draw_position()
			# update screen
			pygame.display.update()

		# win conditions for the different modes
		if mode == 0:
			if player1.reached_goal():
				carryOn = False
		elif mode == 1:
			if player1.reached_goal():
				winner = 1
				carryOn = False
			elif player2.reached_goal():
				winner = 2
				carryOn = False
		elif mode == 2:
			if player1.reached_goal():
				winner = 1
				carryOn = False
			elif computer_character.reached_goal():
				winner = 2
				carryOn = False
		elif mode == 3:
			if player1.reached_goal():
				winner = 1
				carryOn = False
			elif computer_character.get_current_position() == player1.get_current_position() and waitCondition:
				winner = 2
				carryOn = False
		elif mode == 4:
			if player1.escaped():
				winner = 1
				carryOn = False
			elif computer_character.get_current_position() == player1.get_current_position() and waitCondition:
				winner = 2
				carryOn = False

		# limit to 60 frames per second (fps)
		clock.tick(60)

	# stop the game engine once exited the game
	pygame.quit()

	# solo mode
	if mode == 0:
		timer = int(time.time() - game_timer)
		return mode, timer
	# other modes
	else:
		return mode, winner

# main function
if __name__ == "__main__":

	# set the window display position
	set_window_position(50,50)

	# initialize states
	states = {0:"Main Menu", 1:"Gameplay"}
	current_state = states[0]

	# initialize variables
	grid_size = 0
	side_length = 0
	mode = 0

	# flag for main loop
	Run = True

	while Run:
		if current_state == states[0]:
			Run, grid_size, side_length, mode = ui_file.startScreen()
			current_state = states[1]
		elif current_state == states[1]:
			mode, value = runGame(grid_size, side_length, mode)
			if mode != -1:
				ui_file.endGame(mode, value)

			current_state = states[0]

	# just in case lol
	quit()
