# Open and close a window

import pygame # Import pygame Module


pygame.init()	# Initialize Pygame Module


screen_width = 500	# Set screen window's width to 500 pixels
screen_height = 500	# Set screen window's height to 500 pixels
background_color = (255, 255, 255)	# Set background fill color to white with rgb code

game_window = pygame.display.set_mode((screen_width, screen_height))	# create the game window
pygame.display.set_caption('You CAN Close This Window')		#title the game window
game_window.fill(background_color)		# Set the background color
pygame.display.flip()		# Make the game windows changes actually appear

running = True
#below code closes game window when x button on window is pressed
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

