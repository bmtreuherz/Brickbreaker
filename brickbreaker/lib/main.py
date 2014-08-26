import pygame, sys
import block
import random
import level
import highscore

## import android module
try:
	import android
except ImportError:
	android = None

## Import Audio
try: 
	import pygame.mixer as mixer
except ImportError:
	import android.mixer as mixer
	
## Initialize pygame
pygame.init()


blip=mixer.Sound('data/blip.wav')
lose=mixer.Sound('data/lose.wav')
win=mixer.Sound('data/win.wav')

## Set up window
screen_w=480
screen_h=640

if android:
	screensize=pygame.display.Info()
	screen_w = screensize.current_w
	screen_h = screensize.current_h
	
screen_size=(screen_w, screen_h)
screen=pygame.display.set_mode(screen_size)
pygame.display.set_caption("BrickBreaker!")

## Android keymapping
if android:
	android.init()
	android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

## Create image for backround
backround=pygame.Surface(screen_size).convert()
backround.fill((0,0,0))

## Create clock
clock = pygame.time.Clock()

## create border and font
level.start.create_border()
number_of_lives = 3
font_size = screen_w * .111
font=pygame.font.SysFont("calibri", int(font_size) )


## create ball
ball = block.Image("data/ball.png",screen_w/25, screen_w/25)
level.all_sprites_list.add(ball)
speedx = .000375 * screen_w
speedy = .000375 * screen_h
dt = 0 
dy=0
dx=0




## Begin loop
while True:	
	dt = clock.tick(60)
	
	screen.blit(backround, (0,0))
	
	## handles android pause mode
	if android:
		if android.check_pause():
			android.wait_for_resume()
			
	## handle quitting
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			pygame.quit()
			sys.exit()

	
	## create sprites
	level.start.create_sprites()
	

	
	## move ball
	ball.rect.x += dx
	ball.rect.y += dy
	
	## move paddle
	pos = pygame.mouse.get_pos()
	x = screen_w / 2 - int(level.start.paddle.rect[2]) 
	if pos[0] != 0:
		x = pos[0] - int(level.start.paddle.rect[2]) / 2
		level.start.paddle.rect.x = x
	

	## check for collisions between ball and objects
	level.start.check_collision()
	
	## Set up score
	lives_display = "Lives: %r" % number_of_lives
	level_display = "Level %r" % level.start.level_number
	
	lives = font.render(str(lives_display), True, (255,255,255))
	level_ = font.render(str(level_display), True, (255,255,255))
	screen.blit(lives, (.1 * screen_w, .8 * screen_h))
	screen.blit(level_, (screen_w/2 + .1 * screen_w, .8 * screen_h))
	
	
	## next level
	level.start.next_level()
	level.all_sprites_list.draw(screen)
	
	
	
	## losing
	if ball.rect.y > screen_h:
		number_of_lives -=1
		ball.rect.y = 0
		lose.play()
	if number_of_lives == 0:
		## handle highscore
		highscore.High_score.check_highscore()
		high_score = "high score: %r" % highscore.High_score.highscore
		font_high_score = font.render(high_score, True, (255,255,255))
		
		lose_font = font.render("YOU LOSE", True, (255,0,0))
		screen.blit(lose_font, (.3 * screen_w, .3*screen_h))
		screen.blit(font_high_score, (.25 * screen_w, .5 * screen_h))
		ball.rect.x=screen_w/2
		ball.rect.y=screen_h/2
		speedx=0
		speedy=0
		
		level.start.restart()
	pygame.display.update()
	