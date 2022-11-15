import os 
import pygame
import random
import math
from pygame import mixer


# initializing pygame
pygame.init()

# creating screen
screen_width = 2000
screen_height = 2000

screen = pygame.display.set_mode((screen_width,
								screen_height))


# caption and icon
pygame.display.set_caption("Welcome to Space\
Invaders Game ")


# Score1
score_val = 0
scoreX = 5
scoreY = 5
font = pygame.font.Font('freesansbold.ttf', 20)



# Score2
score_val2 = 0
scoreX2 = 855
scoreY2 = 5
font = pygame.font.Font('freesansbold.ttf', 20)

# Game Over
game_over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y,score_count):
	score = font.render("Points: " + str(score_count),
						True, (255,255,255))
	screen.blit(score, (x , y ))




def game_over():
	if(score_val > score_val2):
	
		game_over_text = game_over_font.render("Player 1 WINS",
											True, (255,255,255))
		screen.blit(game_over_text, (650, 350))

	elif(score_val < score_val2):
	
		game_over_text = game_over_font.render("Player 2 WINS",
											True, (255,255,255))
		screen.blit(game_over_text, (650, 350))

	else:

		game_over_text = game_over_font.render("DRAW",
											True, (255,255,255))
		screen.blit(game_over_text, (750, 350))

	


# Background Sound
mixer.music.load('data/background.wav')
mixer.music.play(-1)

# GAME 1

#player
playerImage1 = pygame.image.load('data/spaceship.png')
player_X1 = 425
player_Y1 = 700
player_Xchange1 = 0

#player2
playerImage2 = pygame.image.load('data/spaceship.png')
player_X2 = 1275
player_Y2 = 700
player_Xchange2 = 0



# Invader
invaderImage1 = []
invader_X1 = []
invader_Y1 = []
invader_Xchange1 = []
invader_Ychange1 = []
no_of_invaders = 5
# Invader2
invaderImage2 = []
invader_X2 = []
invader_Y2 = []
invader_Xchange2 = []
invader_Ychange2 = []

for num in range(no_of_invaders):
	invaderImage1.append(pygame.image.load('data/alien.png'))
	invaderImage2.append(pygame.image.load('data/alien.png'))
	invader_X1.append(random.randint(75, 350))
	invader_Y1.append(random.randint(30, 180))
	
	invader_X2.append(random.randint(900, 1175))
	invader_Y2.append(random.randint(30, 180))
	invader_Xchange2.append(1.0)
	invader_Ychange2.append(40)
	invader_Xchange1.append(1.0)
	invader_Ychange1.append(40)
	


# Bullet
# rest - bullet is not moving
# fire - bullet is moving
bulletImage1 = pygame.image.load('data/bullet.png')
bullet_X1 = 0
bullet_Y1 = 700

bullet_Ychange1 = 3
bullet_state1 = "rest"

# Bullet
# rest - bullet is not moving
# fire - bullet is moving
bulletImage2 = pygame.image.load('data/bullet.png')
bullet_X2 = 0
bullet_Y2 = 700

bullet_Ychange2 = 3
bullet_state2 = "rest"

# Collision Concept
def isCollision(x1, x2, y1, y2):
	distance = math.sqrt((math.pow(x1 - x2,2)) +
						(math.pow(y1 - y2,2)))
	if distance <= 50:
		return True
	else:
		return False

def player(x, y,playerImage):
	screen.blit(playerImage, (x - 16, y + 10))



def invader(x, y, i, invaderImage):
	screen.blit(invaderImage[i], (x, y))

def bullet1(x, y):
	global bullet_state1
	screen.blit(bulletImage1, (x, y))
	bullet_state1 = "fire"


def bullet2(x, y):
	global bullet_state2
	screen.blit(bulletImage2, (x, y))
	bullet_state2 = "fire"
# game loop
running = True
while running:

	# RGB
	screen.fill((0, 0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		# Controlling the player movement
		# from the arrow keys
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_8:
				os.system('/home/user/Desktop/project/space-invaders-multiplayer/multi_spaceinvaders.py') 
			if event.key == pygame.K_a:
				player_Xchange1 = -1.2
			if event.key == pygame.K_d:
				player_Xchange1 = 1.2
			if event.key == pygame.K_w:
			
				# Fixing the change of direction of bullet
				if bullet_state1 == "rest":
					bullet_X1 = player_X1
					bullet1(bullet_X1, bullet_Y1)
					bullet_sound = mixer.Sound('data/bullet.wav')
					bullet_sound.play()
			if event.type == pygame.KEYUP:
				player_Xchange1 = 0


		# PLayer 2
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_j:
				player_Xchange2 = -1.2
			if event.key == pygame.K_l:
				player_Xchange2 = 1.2
			if event.key == pygame.K_i:
			
				# Fixing the change of direction of bullet
				if bullet_state2 == "rest":
					bullet_X2 = player_X2
					bullet2(bullet_X2, bullet_Y2)
					bullet_sound = mixer.Sound('data/bullet.wav')
					bullet_sound.play()
				if event.type == pygame.KEYUP:
						player_Xchange2 = 0

	# adding the change in the player position
	player_X1 += player_Xchange1
	for i in range(no_of_invaders):
		invader_X1[i] += invader_Xchange1[i]

	# adding the change in the player position
	player_X2 += player_Xchange2
	for i in range(no_of_invaders):
		invader_X2[i] += invader_Xchange2[i]

	# Controlling the player movement
	# from the arrow keys	

	# bullet movement
	if bullet_Y1 <= 0:
		bullet_Y1 = 900
		bullet_state1 = "rest"
	if bullet_state1 == "fire":
		bullet1(bullet_X1, bullet_Y1)
		bullet_Y1 -= bullet_Ychange1


	# bullet movement
	if bullet_Y2 <= 0:
		bullet_Y2 = 900
		bullet_state2 = "rest"
	if bullet_state2 == "fire":
		bullet2(bullet_X2, bullet_Y2)
		bullet_Y2 -= bullet_Ychange2



	# movement of the invader
	for i in range(no_of_invaders):
		
		if invader_Y1[i] >= 450:
			if abs(player_X1-invader_X1[i]) < 80:
				for j in range(no_of_invaders):
					invader_Y1[j] = 2000
					explosion_sound = mixer.Sound('data/explosion.wav')
					explosion_sound.play()
				game_over()
				break

		if invader_X1[i] >= 735 or invader_X1[i] <= 0:
			invader_Xchange1[i] *= -1
			invader_Y1[i] += invader_Ychange1[i]
		# Collision
		collision = isCollision(bullet_X1, invader_X1[i],
								bullet_Y1, invader_Y1[i])
		if collision:
			score_val += 1
			bullet_Y1 =600
			bullet_state1 = "rest"
			invader_X1[i] = random.randint(200, 650)
			invader_Y1[i] = random.randint(30, 180)
			invader_Xchange1[i] *= -1

		invader(invader_X1[i], invader_Y1[i], i, invaderImage1)


	# movement of the invader
	for i in range(no_of_invaders):
		
		if invader_Y2[i] >= 450:
			if abs(player_X2-invader_X2[i]) < 80:
				for j in range(no_of_invaders):
					invader_Y2[j] = 2000
					explosion_sound = mixer.Sound('data/explosion.wav')
					explosion_sound.play()
				game_over()
				break

		if invader_X2[i] >= 1600 or invader_X2[i] <= 850:
			invader_Xchange2[i] *= -1
			invader_Y2[i] += invader_Ychange2[i]
		# Collision
		collision = isCollision(bullet_X2, invader_X2[i],
								bullet_Y2, invader_Y2[i])
		if collision:
			score_val2 += 1
			bullet_Y2 =600
			bullet_state2 = "rest"
			invader_X2[i] = random.randint(1050, 1400)
			invader_Y2[i] = random.randint(30, 180)
			invader_Xchange2[i] *= -1

		invader(invader_X2[i], invader_Y2[i], i, invaderImage2)

	

	# restricting the spaceship so that
	# it doesn't go out of screen
	if player_X1 <= 100:
		player_X1 = 100
	elif player_X1 >= 800:
		player_X1 = 800

	# restricting the spaceship so that
	# it doesn't go out of screen
	if player_X2 <= 900:
		player_X2 = 900
	elif player_X2 >= 1600:
		player_X2 = 1600


	player(player_X1, player_Y1,playerImage1)
	player(player_X2,player_Y2,playerImage2)
	show_score(scoreX, scoreY,score_val)
	show_score(scoreX2,scoreY2,score_val2)
	pygame.display.update()



